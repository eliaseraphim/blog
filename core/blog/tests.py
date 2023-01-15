import hashlib
import os
import shutil

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from .models import Post
from .forms import PostForm
from .views import IndexView, DetailView


TEST_DIR = 'test_data'
TEST_IMAGES_PATH = os.path.join(settings.BASE_DIR, 'test_data', 'test_images')
TEST_DIR_MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'test_data', 'media')


class BlogPostModelTests(TestCase):
    """Test the :py:class:`blog.models.Post` model."""
    @classmethod
    def setUpClass(cls):
        """
        Set up the testing data for testing the :py:class:`blog.models.Post` model.

        .. py:attribute:: super_user
            :type: ``django.contrib.auth.models.User``

            A super user.

        .. py:attribute:: staff_user
            :type: ``django.contrib.auth.models.User``

            A staff user.

        .. py:attribute:: user
            :type: ``django.contrib.auth.models.User``

            A user.

        ..py:attribute:: title
            :type: ``str``

            Title for posts.

        .. py:attribute:: text
            :type: ``str``

            Text for posts.
        """
        # set up users
        cls.super_user = User(username='super_user', is_active=True, is_staff=True, is_superuser=True)
        cls.staff_user = User(username='staff_user', is_active=True, is_staff=True)
        cls.user = User(username='user', is_active=True)

        # create default data for posts
        cls.title = 'Lorem Ipsum'
        cls.text = (
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et ' +
            'dolore magna aliqua. In fermentum et sollicitudin ac. Nisl tincidunt eget nullam non nisi.'
        )

        # must call super, since django has its own implementation
        super().setUpClass()

    def setUp(self):
        """Sets up the database for each test. Currently, it saves the three users from setUpClassData."""
        self.super_user.save()
        self.staff_user.save()
        self.user.save()

    def test_create_post(self):
        """Test creation of a :py:class:`blog.models.Post` in the database as user."""
        Post(author=self.user, title=self.title, text=self.text).save()

        self.assertIs(Post.objects.all().count(), 1)

    def test_create_post_staff(self):
        """Test creation of a :py:class:`blog.models.Post` in the database as staff."""
        Post(author=self.staff_user, title=self.title, text=self.text).save()

        self.assertIs(Post.objects.all().count(), 1)

    def test_create_post_super_user(self):
        """Test creation of a :py:class:`blog.models.Post` in the database as superuser."""
        Post(author=self.super_user, title=self.title, text=self.text).save()

        self.assertIs(Post.objects.all().count(), 1)

    def test_post_author(self):
        """Test that a :py:class:`blog.models.Post` retains py:attr:`blog.models.Post.author` from model object."""
        Post(author=self.user, title=self.title, text=self.text).save()
        post = Post.objects.last()

        self.assertEqual(self.user, post.author)

    def test_post_title(self):
        """Test that a :py:class:`blog.models.Post` retains py:attr:`blog.models.Post.title` from model object."""
        Post(author=self.user, title=self.title, text=self.text).save()
        post = Post.objects.last()

        self.assertEqual(self.title, post.title)

    def test_post_text(self):
        """Test that a :py:class:`blog.models.Post` retains py:attr:`blog.models.Post.text` from model object."""
        Post(author=self.user, title=self.title, text=self.text).save()
        post = Post.objects.last()

        self.assertEqual(self.text, post.text)

    @override_settings(MEDIA_ROOT=(os.path.join(TEST_DIR_MEDIA_ROOT, 'test_post_image')))
    def test_post_image(self):
        """Test that a :py:class:`blog.models.Post` retains py:attr:`blog.models.Post.image` from model object."""
        path = os.path.join(TEST_IMAGES_PATH, 'test.png')
        image = SimpleUploadedFile(name='test.png', content=open(path, 'rb').read(), content_type='image/png')

        Post(author=self.user, title=self.title, text=self.text, image=image).save()
        post = Post.objects.last()

        with open(path, 'rb') as file:
            original_image_hash = hashlib.sha256(file.read()).hexdigest()
        with open(post.image.path, 'rb') as file:
            post_image_hash = hashlib.sha256(file.read()).hexdigest()

        self.assertIsNotNone(post.image)
        self.assertEqual(original_image_hash, post_image_hash)

    def test_post_date_created(self):
        """
        Test that a :py:class:`blog.models.Post` retains py:attr:`blog.models.Post.date_created` from model object.
        """
        now = timezone.now()
        Post(author=self.user, title=self.title, text=self.text, date_created=now).save()
        post = Post.objects.last()

        self.assertIsInstance(post.date_created, datetime)
        self.assertEqual(now, post.date_created)

    def test_post_date_created_default(self):
        """
        Test that a Post without py:attr:`blog.models.Post.date_created` set initially will default to
        ``django.utils.timezone.now()``.
        """
        Post(author=self.user, title=self.title, text=self.text).save()
        post = Post.objects.last()

        ten_seconds_ago = timezone.now() - timedelta(seconds=10)

        self.assertIsInstance(post.date_created, datetime)
        self.assertTrue(timezone.now() >= post.date_created >= ten_seconds_ago)

    def test_post_date_published(self):
        """
        Test that a :py:class:`blog.models.Post` retains :py:attr:`blog.models.Post.date_published` from model object.
        """
        now = timezone.now()
        Post(author=self.user, title=self.title, text=self.text, date_published=now).save()
        post = Post.objects.last()

        self.assertIsInstance(post.date_published, datetime)
        self.assertEqual(now, post.date_published)

    def test_post_date_published_blank(self):
        """
        Test that a Post without :py:attr:`blog.models.Post.date_published` set initially will default to ``None``.
        """
        Post(author=self.user, title=self.title, text=self.text).save()
        post = Post.objects.last()

        self.assertIs(None, post.date_published)


class BlogViewTests(TestCase):
    """Test the views of the blog application. See :py:mod:`blog.views`."""
    @classmethod
    def setUpClass(cls):
        """
        Set up the testing data for testing the views in :py:mod:`blog.views`.

        .. py:attribute:: anonymous_client
            :type: ``django.test.Client``

            An anonymous user client.

        .. py:attribute:: user
            :type: ``django.contrib.auth.models.User``

            An user.

        .. py:attribute:: posts
            :type: ``tuple``

            A tuple of Post objects to be saved to the database.
        """
        now = timezone.now()
        future = now + timedelta(days=30)

        # create anonymous client
        cls.anonymous_client = Client()

        # create and save user
        cls.user = User(username='user', is_active=True)

        # create posts
        cls.posts = (
            Post(author=cls.user, title='Post 1', text='Text 1.', date_published=now),
            Post(author=cls.user, title='Post 2', text='Text 2.', date_published=now),
            Post(author=cls.user, title='Post 3', text='Text 3.', date_published=now),
            Post(author=cls.user, title='Future Post', text='Future text.', date_published=future),
            Post(author=cls.user, title='Unpublished Post', text='Unpublished text.'),
        )

        super().setUpClass()


class BlogIndexViewTests(BlogViewTests):
    """Test the :py:class:`blog.views.IndexView` class view."""
    def setUp(self):
        """Set up the database for each test. Currently, it saves the user and posts to the database."""
        self.user.save()
        for post in self.posts:
            post.save()

        self.user_client = Client()
        self.user_client.force_login(self.user)

    def test_index_view(self):
        """Test that the index url returns an :py:class:`blog.views.IndexView`."""
        response = self.anonymous_client.get('')
        response_view = response.context_data['view']
        self.assertIsInstance(response_view, IndexView)

    def test_index_view_posts(self):
        """
        Test that py:class:`blogs.views.IndexView` returns only posts that have been published before
        ``timezone.now()``.
        """
        response = self.anonymous_client.get('')
        response_posts = response.context_data['posts']
        posts = Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')

        self.assertEqual(len(posts), len(response_posts))
        for post, response_post in zip(posts, response_posts):
            self.assertEqual(post, response_post)

class BlogDetailViewTests(BlogViewTests):
    """Test the :py:class:`blog.views.DetailView` class view."""
    def setUp(self):
        """
        Set up the database for each test. Currently, it saves the user and posts to the database, and makes a user
        client.

        .. py:attribute:: user_client
            :type: ``django.test.Client``

            A user client.
        """
        self.user.save()
        for post in self.posts:
            post.save()

        self.user_client = Client()
        self.user_client.force_login(self.user)

    def test_detail_view(self):
        """Test that the detail url for a post returns a :py:class:`blog.views.DetailView`."""
        post = Post.objects.get(title__exact='Post 1')

        url = reverse('detail', kwargs={'pk': post.pk})
        response = self.anonymous_client.get(url)
        response_view = response.context_data['view']

        self.assertIsInstance(response_view, DetailView)

    def test_detail_view_post(self):
        """Test that detail view for a post matches the post in the database."""
        post = Post.objects.get(title__exact='Post 1')

        url = reverse('detail', kwargs={'pk': post.pk})
        response = self.anonymous_client.get(url)
        response_post = response.context_data['post']

        self.assertEqual(post, response_post)

    def test_detail_view_action_buttons_anonymous_user(self):
        """
        Test that a response from the detail view for a post does not contain action buttons for an anonymous user.
        """
        post = Post.objects.get(title__exact='Post 1')

        detail_url = reverse('detail', kwargs={'pk': post.pk})
        response = self.anonymous_client.get(detail_url)

        edit_url = reverse('edit_post', kwargs={'pk': post.pk})
        delete_url = reverse('delete_post', kwargs={'pk': post.pk})
        edit_button_content = bytes(f'<a class="btn btn-primary" href="{edit_url}">Edit</a>', encoding='utf-8')
        delete_button_content = bytes(f'<a class="btn btn-secondary" href="{delete_url}">Delete</a>', encoding='utf-8')

        self.assertNotIn(edit_button_content, response.content)
        self.assertNotIn(delete_button_content, response.content)

    def test_detail_view_action_buttons_user(self):
        """Test that a response from the detail view for a post does contain action buttons for a user."""
        post = Post.objects.get(title__exact='Post 1')

        detail_url = reverse('detail', kwargs={'pk': post.pk})
        response = self.user_client.get(detail_url)

        edit_url = reverse('edit_post', kwargs={'pk': post.pk})
        delete_url = reverse('delete_post', kwargs={'pk': post.pk})
        edit_button_content = bytes(f'<a class="btn btn-primary" href="{edit_url}">Edit</a>', encoding='utf-8')
        delete_button_content = bytes(f'<a class="btn btn-secondary" href="{delete_url}">Delete</a>', encoding='utf-8')

        self.assertIn(edit_button_content, response.content)
        self.assertIn(delete_button_content, response.content)


def tearDownModule():
    """Clean the test directory's media directory. This directory contained images created for posts during testing."""
    try:
        shutil.rmtree(TEST_DIR_MEDIA_ROOT)
    except OSError:
        pass

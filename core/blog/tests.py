import hashlib
import os
import shutil

from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings, TestCase
from django.utils import timezone

from .models import Post

TEST_DIR = 'test_data'
TEST_IMAGES_PATH = os.path.join(os.path.join(settings.BASE_DIR, 'test_data'), 'test_images')

class PostModelTests(TestCase):
    @classmethod
    def setUpClass(cls):
        # set up users
        cls.super_user = User(username='super_user', password='password', is_active=True, is_staff=True, is_superuser=True)
        cls.staff_user = User(username='staff_user', password='password', is_active=True, is_staff=True)
        cls.user = User(username='user', password='password', is_active=True)

        # create default data for posts
        cls.title = 'Lorem Ipsum'
        cls.text = (
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et ' +
            'dolore magna aliqua. In fermentum et sollicitudin ac. Nisl tincidunt eget nullam non nisi.'
        )

        # save users to database
        cls.super_user.save()
        cls.staff_user.save()
        cls.user.save()

        # must call super, since django has its own implementation
        super().setUpClass()

    def test_create_post(self):
        """Test creation of a Post in the database as user. No image."""
        Post(author=self.user, title=self.title, text=self.text).save()
        self.assertIs(Post.objects.all().count(), 1)

    def test_create_post_staff(self):
        """Test creation of a Post in the database as staff. No image."""
        Post(author=self.staff_user, title=self.title, text=self.text).save()
        self.assertIs(Post.objects.all().count(), 1)

    def test_create_post_super_user(self):
        """Test creation of a Post in the database as superuser. No image."""
        Post(author=self.super_user, title=self.title, text=self.text).save()
        self.assertIs(Post.objects.all().count(), 1)

    def test_post_author(self):
        Post(author=self.user, title=self.title, text=self.text).save()
        author, post = User.objects.get(username='user'), Post.objects.last()
        self.assertEqual(author, post.author)

    def test_post_title(self):
        Post(author=self.user, title=self.title, text=self.text).save()
        post = Post.objects.last()
        self.assertEqual(self.title, post.title)

    def test_post_text(self):
        Post(author=self.user, title=self.title, text=self.text).save()
        post = Post.objects.last()
        self.assertEqual(self.text, post.text)

    @override_settings(MEDIA_ROOT=(os.path.join(TEST_DIR, 'media')))
    def test_post_image(self):
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

        #os.remove(post.image.path) # clean up image

    def test_post_date_created(self):
        dt = timezone.now()
        Post(author=self.user, title=self.title, text=self.text, date_created=dt).save()
        post = Post.objects.last()
        self.assertIsInstance(post.date_created, datetime)
        self.assertEqual(dt, post.date_created)

    def test_post_date_created_default(self):
        Post(author=self.user, title=self.title, text=self.text).save()
        post = Post.objects.last()
        self.assertIsInstance(post.date_created, datetime)

    def test_post_date_published_blank(self):
        Post(author=self.user, title=self.title, text=self.text).save()
        post = Post.objects.last()
        self.assertIs(None, post.date_published)

    def test_post_date_published(self):
        dt = timezone.now()
        Post(author=self.user, title=self.title, text=self.text, date_published=dt).save()
        post = Post.objects.last()
        self.assertIsInstance(post.date_published, datetime)
        self.assertEqual(dt, post.date_published)


def tearDownModule():
    try:
        shutil.rmtree(os.path.join(TEST_DIR, 'media'))
    except OSError:
        pass

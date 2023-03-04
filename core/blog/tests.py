import hashlib
import os
import shutil

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from .forms import PostForm
from .models import Post
from .views import DetailView, IndexView

TEST_DIR = "_test_data"
TEST_IMAGES_PATH = os.path.join(settings.BASE_DIR, "_test_data", "test_images")
TEST_DIR_MEDIA_ROOT = os.path.join(settings.BASE_DIR, "_test_data", "media")

_User = get_user_model()


def build_user(username):
    user = _User(username=username, is_active=True)
    user.save()

    return _User.objects.last()


def get_sha256(path: str) -> str:
    with open(path, "rb") as file:
        image_hash = hashlib.sha256(file.read()).hexdigest()
    return image_hash


@override_settings(MEDIA_ROOT=(os.path.join(TEST_DIR_MEDIA_ROOT, "test_post_image")))
class BlogPostModelTests(TestCase):
    """Test the :py:class:`blog.models.Post` model."""

    step = 0

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

        .. py:attribute:: title
            :type: ``str``

            Title for posts.

        .. py:attribute:: text
            :type: ``str``

            Text for posts.
        """

        # set up users
        cls.user = _User(username="user", is_active=True)

        # create default data for posts
        cls.title = "Lorem Ipsum"
        cls.text = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et "
            + "dolore magna aliqua. In fermentum et sollicitudin ac. Nisl tincidunt eget nullam non nisi."
        )

        # must call super, since django has its own implementation
        super().setUpClass()

    def setUp(self):
        """
        Sets up the database for each test. Creates and idea for test, and saves the three users from setUpClassData.
        """

        self.id = self.step
        self.step += 1

        self.image = None
        self.image_path = None
        self.image_deleted = False

        self.user.save()

    def assert_integrity(self, post, data=None):
        if data is None:
            data = {}

        self.assertEqual(post.author, data.get("author", self.user))
        self.assertEqual(post.title, data.get("title", self.title))
        self.assertEqual(post.text, data.get("text", self.text))
        self.assertEqual(bool(post.image), bool(self.image and not self.image_deleted))
        self.assertLess(post.created, timezone.now())
        self.assertLess(post.last_edited, timezone.now())

    def assert_image_integrity(self, post):
        original_file_name = self.image.name[:-4]  # remove extension
        original_sha256 = get_sha256(self.image_path)
        post_file_path = post.image.file.name
        post_sha256 = get_sha256(post.image.path)

        self.assertTrue(os.path.exists(post_file_path))
        self.assertIn(original_file_name, post_file_path)
        self.assertEqual(original_sha256, post_sha256)

    def assert_edits(self, data, initial=None):
        post = self.build_post(data=initial)
        original_last_edited = post.last_edited

        post = self.edit_post(post, data)
        new_last_edited = post.last_edited

        self.assert_integrity(post, data=data)

        self.assertNotEqual(new_last_edited, original_last_edited)
        self.assertGreater(new_last_edited, original_last_edited)

        if data.get("image"):
            self.assert_image_integrity(post)

    def build_post(self, data=None):
        if data is None:
            data = {}

        Post(
            author=data.get("author", self.user),
            title=data.get("title", self.title),
            text=data.get("text", self.text),
            image=data.get("image", None),
        ).save()

        return Post.objects.last()

    def edit_post(self, post: Post, data: dict):
        post_id = post.id

        post.author = data.get("author", post.author)
        post.title = data.get("title", post.title)
        post.text = data.get("text", post.text)
        post.image = data.get("image", post.image)
        post.save()

        if "image" in data.keys() and data["image"] is not None:
            post.image = data["image"]
        if "image" in data.keys() and data["image"] is None:
            post.image.delete()
            self.image_deleted = True

        return Post.objects.get(id=post_id)

    def create_image(self):
        self.image_path = os.path.join(TEST_IMAGES_PATH, f"test.png")
        self.image = SimpleUploadedFile(
            name=f"test{self.id}.png",
            content=open(self.image_path, "rb").read(),
            content_type="image/png",
        )

    def test_save_post(self):
        post = self.build_post()

        self.assert_integrity(post)

    def test_save_post_image(self):
        """Test that a :py:class:`blog.models.Post` retains py:attr:`blog.models.Post.image` from model object."""
        self.create_image()
        post = self.build_post({"image": self.image})

        self.assert_integrity(post)
        self.assert_image_integrity(post)

    def test_post_edit_author(self):
        author = build_user(f"user{self.id}")
        data = {"author": author}

        self.assert_edits(data)

    def test_post_edit_title(self):
        title = "Updated Title"
        data = {"title": title}

        self.assert_edits(data)

    def test_post_edit_text(self):
        text = "Updated text body."
        data = {"text": text}

        self.assert_edits(data)

    def test_post_edit_new_image(self):
        self.create_image()
        data = {"image": self.image}

        self.assert_edits(data)

    def test_post_edit_remove_image(self):
        self.create_image()
        initial = {"image": self.image}
        data = {"image": None}

        self.assert_edits(data, initial=initial)


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

            A user.

        .. py:attribute:: posts
            :type: ``tuple``

            A tuple of Post objects to be saved to the database.
        """
        now = timezone.now()
        future = now + timezone.timedelta(days=30)

        # create anonymous client
        cls.anonymous_client = Client()

        # create and save user
        cls.user = _User(username="user", is_active=True)

        # create posts
        cls.posts = (
            Post(author=cls.user, title="Post 1", text="Text 1."),
            Post(author=cls.user, title="Post 2", text="Text 2."),
            Post(author=cls.user, title="Post 3", text="Text 3."),
            Post(
                author=cls.user,
                title="Future Post",
                text="Future text.",
                created=future,
            ),
            Post(author=cls.user, title="Unpublished Post", text="Unpublished text."),
        )

        super().setUpClass()


class BlogIndexViewTests(BlogViewTests):
    """Test the :py:class:`blog.views.IndexView` class view."""

    def setUp(self):
        """Set up the database for each test. Currently, it saves the user and posts to the database."""
        self.user.save()
        for post in self.posts:
            post.save()


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


class BlogNewPostView(BlogViewTests):
    def setUp(self):
        self.user.save()
        self.user_client = Client()
        self.user_client.force_login(self.user)


def tearDownModule():
    """Clean the test directory's media directory. This directory contained images created for posts during testing."""
    try:
        shutil.rmtree(TEST_DIR_MEDIA_ROOT)
    except OSError as exception:
        pass

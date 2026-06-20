from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    """Test the Post model."""

    def setUp(self):
        """"Set up test data for Post model tests."""
        # Create a Post object for testing
        Post.objects.create(title='Test Sticky Note',
                            content='This is a test sticky note.')

    def test_post_has_title(self):
        """Test that a Post object has the expected title."""
        # Test that a Post object has the expected title
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Sticky Note')

    def test_post_has_content(self):
        """Test that a Post object has the expected content."""
        # Test that a Post object has the expected content
        post = Post.objects.get(id=1)
        self.assertEqual(post.content, 'This is a test sticky note.')


class PostViewTest(TestCase):
    """Test the views for the Post model."""
    def setUp(self):
        # Create a Post object for testing views
        Post.objects.create(title='Test Sticky Note',
                            content='This is a test sticky note.')

    def test_post_list_view(self):
        """Test the post-list view."""
        # Test the post-list view
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Sticky Note')

    def test_post_detail_view(self):
        """Test the post-detail view."""
        # Test the post-detail view
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('post_detail', args=[str(post.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Sticky Note')
        self.assertContains(response, 'This is a test sticky note.')

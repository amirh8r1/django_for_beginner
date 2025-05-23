from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username = 'testuser', email = 'test@email.com', password = 'secret'
        )

        cls.post = Post.objects.create(
            title = 'a good title',
            body = 'nice body content',
            author = cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, 'a good title')
        self.assertEqual(self.post.body, 'nice body content')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(str(self.post), 'a good title')
        self.assertEqual(self.post.get_absolute_url(), '/post/1')

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get('/post/1')
        self.assertEqual(response.status_code, 200)
    
    def test_post_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'nice body content')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_post_detailview(self):
        response = self.client.get(reverse('post_detail', kwargs = {'pk': self.post.pk}))
        no_response = self.client.get('post/1000000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'a good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_createview(self):
        response = self.client.post(
            reverse('post_new'),
            {
                'title': 'new title',
                'body': 'new body',
                'author': self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'new title')
        self.assertEqual(Post.objects.last().body, 'new body')

    def test_post_updateview(self):
        response = self.client.post(
            reverse('post_edit', args='1'),
            {
                'title': 'updated title',
                'body': 'updated body',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'updated title')
        self.assertEqual(Post.objects.last().body, 'updated body')

    def test_post_deleteview(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)

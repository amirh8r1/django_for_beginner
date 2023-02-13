from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.
class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.post = Post.objects.create(text='this is a test!')
    
    def test_model_content(self):
        self.assertEqual(self.post.text, 'this is a test!')

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'this is a test!')

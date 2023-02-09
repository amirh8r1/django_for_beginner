from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomepageTest(SimpleTestCase):
    def test_url_exists_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("pages:home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, "<h1>Home Page</h1>")

class AboutpageTest(SimpleTestCase):
    def test_url_exists_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("pages:about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("pages:about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("pages:about"))
        self.assertContains(response, "<h1>About Page</h1>")

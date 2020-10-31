from django.urls import resolve,reverse
from django.test import TestCase
from blog.views import *
# Blog unit tests to determine if the Blog app's urls are locatable!
class TestViews(TestCase):
    # Test to determine if the url to the blog list page is findable!
    def test_root_url_to_blog_list_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)
    # Test to determine if the blog_list url is callable by name!
    def test_url_to_blog_list_is_callable_by_name(self):
        response = self.client.get(reverse('Blog:blog_list'))
        self.assertEqual(response.status_code,200)

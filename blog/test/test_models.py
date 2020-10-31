from django.urls import resolve,reverse
from django.test import TestCase
from blog.models import Blog
from datetime import date
class TestModels(TestCase):
    #Functional test to ensure that the Blog Model is operational.
    def test_blog_model(self):
        blog = Blog()
        blog.title = "I went for a walk"
        blog.description = "The weather was bone chilling and the air is heavy, but I enjoyed my time outside."
        blog.pub_date = date.today()
        blog.save()
        response = Blog.objects.get(pk=1)
        self.assertEqual(response, blog)
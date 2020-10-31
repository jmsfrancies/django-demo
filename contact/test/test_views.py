from django.urls import resolve,reverse
from django.test import TestCase
from contact.views import *
#Contact unit tests to test the views of the contact list app!
class TestViews(TestCase):
    # test to determine if the url to the contact list page is visible
    def test_root_url_to_contact_list_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)
    # test to determine if the contact list is callable by name
    def test_url_to_contact_list_is_callable_by_name(self):
        response = self.client.get(reverse('Contact:contact_list'))
        self.assertEqual(response.status_code,200)
from django.urls import resolve,reverse
from django.test import TestCase
from contact.models import Contact

class TestModels(TestCase):
    #Functional test to ensure that the Contact Model is operational.
    def test_contact_model(self):
        contact = Contact()
        contact.first_name = "James"
        contact.last_name = "Francies"
        contact.email = "jmsfrancies@yahoo.com"
        contact.save()
        response = Contact.objects.get(pk=1)
        self.assertEqual(response, contact)
    
from django.test import TestCase
from addressbook.contacts.models.contact import Contact
from addressbook.contacts.models.group import Group
from django.contrib.auth.models import User
from addressbook.contacts.controllers.home import *

"""
Test Contact Model
"""
class ContactTest(TestCase):
    """ Create a test object """
    def setUp(self):
        self.contact = Contact.objects.create(first_name="first", last_name="last", mobile_phone="4167778990", facebook="testaccount")
        
    """ Check if object contains correct phone numbers """
    def testPhoneNumber(self):
        self.assertEqual(self.contact.mobile_phone, "4167778990")
        self.assertEqual(self.contact.home_phone, "")
        
    """ Check if social IDs are correct """
    def testSocialID(self):
        self.assertEqual(self.contact.facebook, "testaccount")
       
"""
Test Group Model
"""
class GroupTest(TestCase):
    """ Create a test object """
    def setUp(self):
        self.user = User.objects.get()
        self.group = Group.objects.create(name="testGroup", owner=user)
        
    """ Test if group name is correct """
    def testGroupName(self):
        self.assertEqual(self.group.name, "testGroup")
        
    """ Test if owner name is correct """
    def testOwner(self):
        self.assertEqual(self.group.owner.username, self.user.username)
        
"""
Test Helper methods
"""
class TestHelperMethods(TestCase):
    """ Test if email validator works """
    def testEmailValidator(self):
        self.assertEqual(is_valid_email("test123@test.com"),True)
        self.assertEqual(is_valid_email("test_123@test.com"),True)
        self.assertEqual(is_valid_email("test@test"),False)
        self.assertEqual(is_valid_email("test"),False)
        
    """ Testing whether unique username check works """ 
    def testUniqueUsername(self):
        user = User.objects.get()
        self.assertEqual(is_unique_user(user.username), False)
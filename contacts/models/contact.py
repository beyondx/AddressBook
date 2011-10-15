from django.contrib.auth.models import User
from django.db.models import *
from addressbook.contacts.models.group import Group
import datetime

class Contact(Model):
    first_name = CharField(max_length=50, null=False)
    last_name = CharField(max_length=50, null=False)
    image = ImageField(blank=True, null=True)
    email = EmailField(blank=True)
    home_phone = CharField(max_length=20,blank=True)
    office_phone = CharField(max_length=20, blank=True)
    office_phone_extn = CharField(max_length=5,blank=True)
    mobile_phone = CharField(max_length=20,blank=True)
    facebook = CharField(max_length=100,blank=True)
    twitter = CharField(max_length=100,blank=True)
    owner = ForeignKey(User)
    group = ForeignKey(Group, blank=True, null=True)
    
    def __unicode__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        app_label = "contacts"

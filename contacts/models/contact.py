from django.contrib.auth.models import User
from django.db.models import *
from addressbook.contacts.models.group import Group
import datetime

"""
Model to store contacts

CREATE TABLE `contacts_contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `image` varchar(200) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `home_phone` varchar(20) DEFAULT NULL,
  `mobile_phone` varchar(20) DEFAULT NULL,
  `office_phone` varchar(20) DEFAULT NULL,
  `office_phone_extn` varchar(5) DEFAULT NULL,
  `facebook` varchar(100) DEFAULT NULL,
  `twitter` varchar(100) DEFAULT NULL,
  `owner_id` int(11) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 
"""
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

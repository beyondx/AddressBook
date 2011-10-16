from django.db.models import *
from django.contrib.auth.models import User

"""
Users can create groups and categorize their contacts

CREATE TABLE `contacts_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8
"""
class Group(Model):
    name = CharField(max_length=100, null=False)
    owner = ForeignKey(User)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        app_label = "contacts"

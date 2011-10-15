from django.db.models import *
from django.contrib.auth.models import User

"""
Users can create groups and categorize their contacts
"""
class Group(Model):
    name = CharField(max_length=100, null=False)
    owner = ForeignKey(User)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        app_label = "contacts"

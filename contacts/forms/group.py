from django.forms import ModelForm
from addressbook.contacts.models.group import Group

"""
Form to handle creation of new group
"""
class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ('owner')

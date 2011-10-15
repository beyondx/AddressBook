from django.forms import ModelForm
from addressbook.contacts.models.group import Group

class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ('owner')

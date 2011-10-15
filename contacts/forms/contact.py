from django.forms import ModelForm
from addressbook.contacts.models.contact import Contact
from addressbook.contacts.models.group import Group

"""
Form to create new contacts or edit existing contacts
"""
class ContactForm(ModelForm):
    """
    Customize group list to display only user specific groups
    """
    def __init__(self,user,*args,**kwargs):
        super (ContactForm,self ).__init__(*args,**kwargs)
        self.fields['group'].queryset = Group.objects.filter(owner=user)
    class Meta:
        model = Contact
        exclude = ('owner')
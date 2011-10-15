from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from addressbook.contacts.models.group import Group
from addressbook.contacts.models.contact import Contact
from addressbook.contacts.forms.group import GroupForm
from addressbook.contacts.controllers.home import construct_page

"""
"""
@login_required
@csrf_exempt
def group(request):
    user = request.user
    message = ''
    
    if request.method == 'POST':
        if request.POST.get('name').strip() != "":
            group_form = GroupForm(request.POST, instance=Group(owner=user))
            if group_form.is_valid():
                group_form.save()
                group_form = GroupForm(instance=Group())
        else:
            message = 'Group name cannot be empty.'
            group_form = GroupForm(instance=Group())
            
    else:
        group_form = GroupForm(instance=Group())
    
    groups = Group.objects.filter(owner=user)
    values = {'groups':groups, 'group_form':group_form, 'message':message}
    
    return HttpResponse(construct_page(request, render_to_string('group.html', values)))
 
"""
Delete a group from list
"""
@login_required
def delete(request):
    user = request.user
    if 'group' in request.GET:
        group = Group.objects.filter(pk=request.GET.get('group'),owner=user)
        for contact in Contact.objects.filter(group=group,owner=user):
            contact.group = None
            contact.save()
            
        group.delete()
        
    return HttpResponseRedirect("/groups/")
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from addressbook.contacts.controllers.home import construct_page
from addressbook.contacts.models.contact import Contact
from addressbook.contacts.forms.contact import ContactForm

@login_required
@csrf_exempt
def list(request):
    user = request.user
    
    contacts = Contact.objects.filter(owner=user)
    
    values = {'contacts':contacts}
    
    return HttpResponse(construct_page(request, render_to_string('contact/list.html', values)))

@login_required
@csrf_exempt
def show(request):
    user = request.user
    
    if 'contact' in request.GET:
        contact = Contact.objects.get(pk=request.GET.get('contact'),owner=user)
    else:
        return HttpResponseRedirect('/contacts/')
        
    values = {'contact':contact}
    
    return HttpResponse(construct_page(request, render_to_string('contact/show.html', values)))
    
@login_required
@csrf_exempt
def create(request):
    user = request.user
    message = ''
    
    if request.method == "POST":
        contact_form = ContactForm(user,request.POST, request.FILES, instance=Contact(owner=user))
        if contact_form.is_valid():
            contact = contact_form.save()
            return HttpResponseRedirect("/contacts/show/?contact="+str(contact.pk))
            
    else:
        contact_form = ContactForm(user, instance=Contact())
        
    values = {'contact_form':contact_form,'message':message,'is_new':True}
    
    return HttpResponse(construct_page(request, render_to_string('contact/edit.html', values)))

@login_required
@csrf_exempt
def edit(request):
    user = request.user
    message = ''
    
    contact = Contact(owner=user)
    
    if 'contact' in request.GET:
        contact = Contact.objects.get(pk=request.GET.get('contact'),owner=user)
        
    if request.method == "POST":
        contact_form = ContactForm(user,request.POST, request.FILES, instance=contact)
        if contact_form.is_valid():
            contact = contact_form.save()
            return HttpResponseRedirect("/contacts/show/?contact="+str(contact.pk))
    else:
        contact_form = ContactForm(user, instance=contact)
        
    values = {'contact_form':contact_form,'message':message}
    
    return HttpResponse(construct_page(request, render_to_string('contact/edit.html', values)))

@login_required
def delete(request):
    user = request.user
    if 'contact' in request.GET:
        Contact.objects.filter(pk=request.GET.get('contact'),owner=user).delete()
        
    return HttpResponseRedirect("/contacts/")
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from addressbook.contacts.controllers.home import construct_page

"""
User can change its first name,last name and password
"""
@login_required
@csrf_exempt
def account(request):
    user = request.user
    message = ''
    
    if request.method == 'POST':
        if 'password' in request.POST:
            
            if request.POST.get('password').strip() == "":
                message = "Password cannot be blank."
            elif request.POST.get('password') != request.POST.get('cpassword'):
                message = 'Password missmatch.'
            else:
                user.set_password(request.POST.get('password'))
                user.save()
                message = 'Password successfully changed.'
        elif 'first_name' in request.POST:
            if request.POST.get('first_name').strip() != "":
                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.save()
                message = "Name successfully changed."
            
            else:
                message = "First name cannot be blank."
    
    values = {'user':user, 'message':message}
    
    return HttpResponse(construct_page(request, render_to_string('setting.html', values)))
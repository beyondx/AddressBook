from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

@csrf_exempt
def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard')
        
    values = {}
    if request.method == 'POST':
        if 'signin' in request.POST:
            result = signin(request)
            
            if not result['error']:
                return HttpResponseRedirect('/dashboard')
            else:
                values['error_message'] = result['message']
                
        if 'signup' in request.POST:
            result = signup(request)
        
            if result['error']:
                values['error_message'] = result['message']     
            else:
                values['error_message'] = "New Account created. Please Signin."
            
    return HttpResponse(construct_page(request,render_to_string('home.html',values)))

def signin(request):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None:
        if user.is_active:
            login(request, user)
            request.session['user'] = user
            return {'error':False, 'message':'Success!!!'}
        else:
            return {'error':True, 'message':"Your account has been disabled!"}
    else:
        if is_unique_user(request.POST.get('username')):
            return {'error':True, 'message':"Username doesn't exist."}
        return {'error':True, 'message':"Your username and password were incorrect."}

def signup(request):
    if not is_unique_user(request.POST.get('username')):
        return {'error':True, 'message':"Username already exist."}
      
    if request.POST.get('username').strip() == "" or request.POST.get('password').strip() == "":
        return {'error':True, 'message':"Username and password cannot be blank."}
      
    if request.POST.get('first_name').strip() == "" or request.POST.get('last_name').strip() == "":
        return {'error':True, 'message':"First and last name cannot be blank."}
    if not is_valid_email(request.POST.get('username').strip()):
        return {'error':True, 'message':"Invalid email."}
    if request.POST.get('password') != request.POST.get('cpassword'):
        return {'error':True, 'message':"Passwords did not match."}
        
    user = User(first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
                username=request.POST.get("username"),
                email=request.POST.get("username"),
                is_active=True)
    
    user.set_password(request.POST.get("password"))
    user.save()
    
    return {'error':False,'message':'Success!!!!'}
    

def signout(request):
    if request.user.is_authenticated():
        logout(request)
    
    if 'user' in request.session:
        del request.session['user']

    return HttpResponseRedirect('/')
    
def is_unique_user(username):
    try:
        user = User.objects.get(username=username)
        return False
    except User.DoesNotExist:
        return True
    
def is_valid_email(email):
    try:
        f = forms.EmailField()
        f.clean(email)
        return True
    except ValidationError:
        return False
    
def construct_page(request,html=''):
    if request.user.is_authenticated():
        html = render_to_string('sidebar.html',{}) + html
    return get_page_header(request) + html

def get_page_header(request):
    values = {'loggedin':False}
    if request.user.is_authenticated():
        values['loggedin'] = True
        values['name'] = (request.user.first_name).capitalize()
    return render_to_string("header.html",values)

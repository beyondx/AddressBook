from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

"""
Create homepage with Sign In and Sign Up options
"""
@csrf_exempt
def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard') 
    values = {}
    if request.method == 'POST':
        """ Check if signin button pressed """
        if 'signin' in request.POST:
            result = signin(request)

            """ On error return error message"""
            if result['error']:
                values['error_message'] = result['message']
            else:
                return HttpResponseRedirect('/dashboard')
                
        """ Check if sign up button pressed """   
        if 'signup' in request.POST:
            result = signup(request)
            
            """ On error return error message"""
            if result['error']:
                values['error_message'] = result['message']     
            else:
                values['error_message'] = "New Account created. Please Signin."
            
    return HttpResponse(construct_page(request,render_to_string('home.html',values)))

"""
Method to authenticate user for signining into the system
"""
def signin(request):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None:
        if user.is_active:
            login(request, user)
            
            return {'error':False, 'message':'Success!!!'}
        else:
            return {'error':True, 'message':"Your account has been disabled!"}
    else:
        if is_unique_user(request.POST.get('username')):
            return {'error':True, 'message':"Username doesn't exist."}
        return {'error':True, 'message':"Your username and password were incorrect."}

"""
Method to signup new users if they provide valid email and password
"""
def signup(request):
    
    """ Check if username and password are not blank """
    if request.POST.get('username').strip() == "" or request.POST.get('password').strip() == "":
        return {'error':True, 'message':"Username and password cannot be blank."}
        
    """ Check if username is valid email """
    if not is_valid_email(request.POST.get('username').strip()):
        return {'error':True, 'message':"Invalid email."}
        
    """ Check if username is available """
    if not is_unique_user(request.POST.get('username')):
        return {'error':True, 'message':"Username already exist."}
      
    """ Check if first_name and last_name are not blank """
    if request.POST.get('first_name').strip() == "" or request.POST.get('last_name').strip() == "":
        return {'error':True, 'message':"First and last name cannot be blank."}
    
    """ Check if both password entires match """
    if request.POST.get('password') != request.POST.get('cpassword'):
        return {'error':True, 'message':"Passwords did not match."}
        
    """
    SQL Query: INSERT INTO user('first_name','last_name','username','email','is_active','password')
               VALUES (first_name, last_name, username, username, 1,MD5(password))
    """
    user = User(first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
                username=request.POST.get("username"),
                email=request.POST.get("username"),
                is_active=True)
    
    user.set_password(request.POST.get("password"))
    user.save()
    
    return {'error':False,'message':'Success!!!!'}
    
"""
Method to signout user
"""
def signout(request):
    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect('/')
    
"""
Helper method to check whether the email is unique for signup
"""
def is_unique_user(username):
    try:
        """
        SQL Query: SELECT *
                   FROM user
                   WHERE username=username
        """
        user = User.objects.get(username=username)
        return False
    except User.DoesNotExist:
        return True
   
"""
Helper method to vaidate email
"""
def is_valid_email(email):
    try:
        f = forms.EmailField()
        f.clean(email)
        return True
    except ValidationError:
        return False
 
"""
Helper method to construct page with header and footer
"""
def construct_page(request,html=''):
    if request.user.is_authenticated():
        html = render_to_string('sidebar.html',{}) + html
    return get_page_header(request) + html + render_to_string('footer.html',{})

"""
Helper method to return header part of webpage
"""
def get_page_header(request):
    values = {'loggedin':False}
    if request.user.is_authenticated():
        values['loggedin'] = True
        values['name'] = (request.user.first_name).capitalize()
    return render_to_string("header.html",values)

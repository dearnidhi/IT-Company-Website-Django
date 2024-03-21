from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import About, Service, Project, Testimonial, Team, Contact,Blog,User
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse


# Create your views here.

def index(request):
    about_data = About.objects.first()
    services = Service.objects.all()
    projects = Project.objects.all()
    teams = Team.objects.all()
    testimonials = Testimonial.objects.all()
    blogs = Blog.objects.all()  

    
    context = {
        'about_data': about_data,
        'services': services,
        'projects': projects,
        'teams': teams,
        'blogs': blogs,
        'testimonials': testimonials,
    }
    
    if request.method == "POST":
        context.update(handle_contact_form(request))
        if 'message' in context:
            return render(request, 'index.html', context)
    
    return render(request, 'index.html', context)

def handle_contact_form(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        num = request.POST.get("number")
        msz = request.POST.get("message")
        obj = Contact(name=name, email=em, number=num, message=msz)
        obj.save()
        context['message'] = f"Dear {name}, Thanks For Your Time!"
    return context

def about(request):
    about_data = About.objects.first()  
    teams= Team.objects.all()  
    return render(request, 'about.html', {'about_data': about_data, 'teams': teams})

def service(request):
    services = Service.objects.all()  
    return render(request, 'service.html', {'services': services})

def project(request):
    projects = Project.objects.all()  
    return render(request, 'project.html',{'projects': projects})

def team(request):
    teams= Team.objects.all()  
    return render(request, 'team.html', { 'teams': teams})

def testimonial(request):
    testimonials = Testimonial.objects.all()  
    return render(request, 'testimonial.html',{'testimonials': testimonials})

def blog(request):
    blogs = Blog.objects.all()  
    return render(request, 'blog.html',{'blogs': blogs})

def contact(request):
    if request.method == "POST":
        context = handle_contact_form(request)
        return render(request, 'contact.html', context)
    return render(request, 'contact.html')


from django.shortcuts import render, redirect
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        # Check if user already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request, 'registration.html', {'error': 'User with this username or email already exists.'})
        else:
            # Create new user
            user = User.objects.create(username=username, password=password, email=email)
            user.save()
            return redirect('/login')
    return render(request, 'registration.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Changed the login method name to avoid conflict
            return redirect('index')   # Assuming you've defined the URL name for index page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

from django.shortcuts import render, redirect
from .models import Story, StoryForm, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username) or User.objects.get(email=username) or None
            if user:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, ("Name and Password do not match."))
                    return redirect('login')
            else:
                messages.error(request, ("User does not exist!"))
                return redirect('login')
        except:
            messages.error(request, ("User does not exist!"))
            return redirect('login')

    context = {}
    return render(request, 'base/loginPage.html', context)

def logoutPage(request):
    logout(request)
    return render(request, 'base/home.html')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        if p1 != p2:
            messages.error(request, ("Passwords do not match"))
            return redirect('register')
        try:
            user = User.objects.get(username=username) or User.objects.get(email=email)
            messages.error(request, ("User already exists"))
        except:
            user = User.objects.create_user(username, email, p1)
            user.save()
            login(request, user)
            return redirect('home')

    return render(request, 'base/register.html', {'form': form})

def profile(request, pk):
    stories = Story.objects.filter(author=pk)
    context = {'stories': stories}
    return render(request, 'base/profileMain.html', context)

def home(request):
    stories = Story.objects.all()
    context = {'stories': stories}
    return render(request, 'base/home.html', context)

def sample(request):
    return render(request, 'base/post.html')

@login_required(login_url='login')
def createPost(request):
    if request.method == "POST":
        title = request.POST['title']
        summary = request.POST['summary']
        content = request.POST['content']
        author = request.user

        obj = Story.objects.create(author=author, summary=summary, title=title, content=content)
        obj.save()
        return redirect('home')

    context = {}
    return render(request, 'base/create.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']

        send_mail(
            "Mail from {}".format(name),
            "Received a message:\n{}.\nContact No. {}.\nContact Email: {}".format(msg, phone, email),
            email,
            ['adityamallick90aa@gmail.com'],
        )

    return render(request, 'base/contact.html')

def viewPost(request, pk):
    story = Story.objects.get(id=pk)
    context = {'story': story}
    return render(request, 'base/viewPost.html', context)
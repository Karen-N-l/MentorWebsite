from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required


@login_required
def about(request):
    return render(request,'about.html')

@login_required
def contact(request):
    return render(request,'contact.html')

@login_required
def details(request):
    return render(request,'course-details.html')

@login_required
def courses(request):
    return  render(request,'courses.html')

@login_required
def events(request):
    return  render(request,'events.html')

@login_required
def home(request):
    return render(request,'index.html')

@login_required
def pricing(request):
    return  render(request,'pricing.html')

@login_required
def trainers(request):
    return  render(request,'trainers.html')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect("register")
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html',{'form':form})


from email import message
from django.shortcuts import render,redirect
from .forms import ReportingForm
from django.contrib.auth import login, authenticate,logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.

def home(request):
    form=ReportingForm(request.POST or None,request.FILES or None)
    files=request.FILES.getlist("screenshot")
    if request.method=="POST":
        # print(form)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            for f in files:
                form.screenshot=f
                form.save()
            
            messages.success(request,'Your complaint have been registered')
            return redirect('home')
    else:
        form=ReportingForm()
    context={'form':form}
    return render(request,'home.html',context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("home")
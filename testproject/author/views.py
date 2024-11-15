from django.shortcuts import render,HttpResponse,redirect
from .forms import RegistrationForm,EditForm,BlogForm
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib.auth import authenticate,update_session_auth_hash,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Blog
def home(r):
    blogs=Blog.objects.all()
    print(blogs)
    return render(r,'home.html',{'blogs':blogs})

@login_required
def profile(r):
    blogs=Blog.objects.filter(author=r.user)
    print(blogs)
    return render(r,'profile.html',{'blogs':blogs})

def signUp(r):
    if r.user.is_authenticated:
        return HttpResponse("Profile")
    if r.method=='POST':
        form1=RegistrationForm(r.POST)
        if form1.is_valid():
            form1.save()
            messages.success(r, 'Sign Up successfully. Now, you can log in.')
            return redirect('home')
    return render(r,'form.html',{'form':RegistrationForm(),'type':'Sign Up'})


def logIn(r):
    if r.user.is_authenticated:
        return redirect('home')
    if r.method=='POST':
        form1=AuthenticationForm(request=r,data=r.POST)
        if form1.is_valid():
            username=form1.cleaned_data['username']
            userpassword=form1.cleaned_data['password']
            user=authenticate(username=username,password=userpassword)
            if user is not None:
                login(r,user)
                messages.success(r, 'Log in successfully')
                
                return redirect('home')
            else:
                return HttpResponse("Wrong Credential")
        messages.warning(r,'Failed')
        return redirect('logIn')
    return render(r,'form.html',{'form':AuthenticationForm(),'type':'Log In'})

@login_required
def logOut(r):
    logout(r)
    messages.success(r, 'Log out successfully')
    return redirect('home')
    
@login_required
def editProfile(request):
  if request.user.is_authenticated:
      if request.method == 'POST':
          form1 =EditForm(request.POST,instance=request.user)
          if form1.is_valid():
              messages.success(request, 'Account updated successfully')
              
              form1.save()
              return redirect('home')
      else:
          form1 =EditForm(instance=request.user)
          return render(request, 'form.html', {'form': form1,'type':'Edit Profile'})
  else:
      return redirect('home')
  


@login_required
def postBlog(r):
    if r.method=='POST':
        form1=BlogForm(r.POST)
        form1.instance.author=r.user
        form1.instance.date=datetime.now()
        if form1.is_valid():
            form1.save()
            return redirect('home')
    return render(r,'form.html',{'form':BlogForm(),'type':'Blog'})


@login_required
def editpost(r,id):
    post=Blog.objects.get(pk=id)
    form1=BlogForm(instance=post)
    if r.method=='POST':
        form1=BlogForm(r.POST,instance=post)
        if form1.is_valid():
            form1.save()
            return redirect('profile')
    return render(r,'form.html',{'form':form1,'type':'Done'})

from django.shortcuts import redirect, render
from .forms import SignupForm,Userform,Profileform
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse


# Create your views here.

def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid:
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=user, passwoed=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form}) 


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})




def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform = Userform(request.POST,instance=request.user)
        profileform = Profileform(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = Userform(instance=request.user)
        profileform = Profileform(instance=profile)
    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})
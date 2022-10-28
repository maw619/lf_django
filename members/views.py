from tkinter.messagebox import NO
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,
                            password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'There was a problem logging in, try again ')
            return redirect('login')    
    else:
        return render(request, 'authenticate/login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out ')
    return redirect('login')

def register_user(request):
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user = form.save()
            
            if user is not None:
                login(request, user)
                return redirect('home')
        
    return render(request, 'authenticate/register.html', {'form': form})

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomForm
# Create your views here.
def register(request):
    if request.method=="POST":
        register_form=CustomForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'New user was created')
        return redirect('register')
    register_form=CustomForm()
    return render(request,'register.html',{'register_form':register_form})
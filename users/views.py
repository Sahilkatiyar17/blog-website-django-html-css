from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # ready made forms
from django.contrib import messages # it is used to display different flash messages like - debug,info,success,warnign,error
from .forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
  #      form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username') #we are retriving the username from the cleaned_data dict.
            messages.success(request, f"{username}Your account has been created! you are now able to login ") #f method works in only 3.6 version
            return redirect('login')
    else:
        form=UserRegisterForm()
#        form = UserCreationForm()
    return render(request,'register.html',{'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.views import View
from user.forms import UserForm,ProfileUpdateForm
from user.models import User
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class ProfileView(View):
    def get(self, request):
        user = request.user
        return render(request, 'profile.html', context={'user': user})


class ProfileUpdateView(View):
    def get(self, request):
        u = ProfileUpdateForm(instance=request.user)
        return render(request, 'profile_update.html', context={'u': u})

    def post(self, request):
        u = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if u.is_valid():
            u.save()
            return redirect('user:profile')
        else:
            return render(request, 'profile_update.html', context={'u': u})

class RegisterView(View):
    def get(self, request):
        create_forms = UserForm()
        context = {
            'form': create_forms,
        }
        return render(request, 'register.html', context=context)

    def post(self, request):
        create_forms = UserForm(request.POST, request.FILES)
        if create_forms.is_valid():
            create_forms.save()
            return redirect('user:login')
        else:
            context = {
                'form': create_forms
            }
            return render(request, 'register.html', context=context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'form': login_form,
        }
        return render(request, 'login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('massages:home')
        else:
            context = {
                'form': login_form,
            }
            return render(request, 'login.html', context=context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user:login')


class RegisterLoginPage(View):
    def get(self, request):
        return render(request, 'page.html')
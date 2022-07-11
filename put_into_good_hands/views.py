from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View


class LandingPageView(View):
    def get(self, request):
        return render(request, "index.html", {})


class AddDonationView(View):
    def get(self, request):
        return render(request, "form.html",  {})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html", {})

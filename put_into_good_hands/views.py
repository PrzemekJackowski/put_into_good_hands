from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from put_into_good_hands.models import Donation


class LandingPageView(View):
    def get(self, request):
        gifts = Donation.objects.all()
        quantity = 0
        institutions = []
        for gift in gifts:
            quantity += gift.quantity
            if gift.institution not in institutions:
                institutions.append(gift.institution.name)
        count_institutions = len(institutions)
        return render(request, "index.html", {"quantity": quantity, "count_institutions": count_institutions})


class AddDonationView(View):
    def get(self, request):
        return render(request, "form.html",  {})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html", {})

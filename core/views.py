from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout


from .mixins import AnonymousMixin
from .forms import SignupCapthaForm, CustomRegisterForm

class RegisterationView(AnonymousMixin, View):

	def post(self, request, *args, **kwargs):
		form = CustomRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("campaing:profile")
		else:
			messages.redirect(request, form.erros)
			return redirect("/signup/")

	def get(self, request, *args, **kwargs):
		form = SignupCapthaForm()
		return render(request, "registration/registration.html", context={"form": form})


# class LoginView(AnonymousMixin, View):

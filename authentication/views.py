from django.shortcuts import render, redirect
from .models import DaemonStar_User
from django.views.generic import FormView, View
from .forms import (CustomUserCreationForm,
						  LoginForm,
						  ProfileEditForm)
from django.contrib.auth import (
		authenticate,
		login,
		logout,
      get_user_model,
	)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

class SignUp(FormView):
	form_class = CustomUserCreationForm

	template_name = 'registration.html'

	def form_valid(self, form):
		form.save()

		username = self.request.POST['username']
		password2 = self.request.POST['password2']

		user = authenticate(username=username, password=password2)
		login(self.request, user)

		return redirect('authentication:profile')

class LoginView(View):
	form_class = LoginForm
	template_name = 'login.html'

	def get(self, request):
		form = self.form_class(None)
		print (form.errors)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid:

			username = request.POST['username']
			password = request.POST['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:

				login(request, user)
				print (form.errors)
				return redirect('item_view:welcome_page')
			elif user is None:
				print("no user found")
		return render(request, self.template_name, {'form': form})


def logout_view(request):
	logout(request)

	return redirect('item_view:welcome_page')

@login_required(login_url='authentication:sign_in')
def profile(request):
	if request.method == 'POST':
			instance = get_object_or_404(DaemonStar_User, username=request.user)
			profile_form = ProfileEditForm(
												instance=instance,
												data=request.POST,
												files=request.FILES)
			if profile_form.is_valid():
				profile_form.save()

			else:
					profile_form = ProfileEditForm(
											instance=instance)
					return render(request,
												'profile_change.html',
									       {'profile_form': profile_form})
	return render(request, "profile.html")

@login_required
def edit(request):
	instance = get_object_or_404(DaemonStar_User, username=get_user_model)
	if request.method == 'POST':

			profile_form = ProfileEditForm(
												instance=instance,

												files=request.FILES)
			if profile_form.is_valid():
				profile_form.save()

			else:
					profile_form = ProfileEditForm(
											instance=instance)
					return render(request,
												'profile_change.html',
									       {'profile_form': profile_form}, {'instance': instance})




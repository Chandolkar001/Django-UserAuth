from django.http import request
from django.shortcuts import  render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Profile

def index(request):
	if request.method == 'POST':

		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		 
		if password1 != password2:
			messages.error(request, 'Password don\'t match.')
			return render(request, 'task3/home.html')
		
		email = request.POST.get('email')
		username = request.POST.get('username')

		if User.objects.filter(email = email).exists():
			messages.error(request, 'This email already exists in the database')
			return render(request, 'task3/home.html')
        
		if User.objects.filter(username = username).exists():
			messages.error(request, 'This username already exists')
			return render(request, 'task3/home.html')

		phone = request.POST.get('phone')

		if len(str(phone)) != 10:
			messages.error(request, 'Please enter a valid phione number')
			return render(request, 'task3/home.html')
		
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		gender = request.POST.get('gender')

		newUser = User.objects.create_user(username = username, email = email, first_name = fname, last_name = lname, password = password1)

		profile = Profile(user = newUser, phone = phone, gender = gender)
        
		profile.save()
		

		messages.success(request, 'Your account has been created successfully')

		return redirect ('login')

	return render(request, 'task3/home.html')
		
def login(request):
	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		user = auth.authenticate(request, username = username, password = password)

		if user is not None:
			auth.login(request, user)
			return redirect('userHome')
		else:
			messages.error(request, 'Invalid credentials. ')
			return redirect('login')

	return render(request, 'task3/login.html')

def userHome(request):
	return render(request, 'task3/user-home.html')
	

def logout(request):
	auth.logout(request)
	messages.info(request, 'You have logged out successfully')
	return redirect('login')

def search(request):
	if request.method == 'POST':

		email = request.POST.get('email')

		if email == '':
			messages.error(request, 'Please enter an email address to search.')
			return redirect('search')

		user = User.objects.filter(email = email)

		if len(user) == 0:
			messages.info(request, 'No user found with the entered email ID.')
			return redirect('search')
		else:
			params = {'user': user}
			return render(request, 'task3/result.html', params)

	return render(request, 'task3/search.html')




		

from django.shortcuts import render,redirect 
from .models import List
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm, ChangePwdForm
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request, 'home.html')

def about(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']

		send_mail('Message from'+' ' + name + ' ' + ' about'+ ' ' + subject ,email+ ' \n\n' + message,email,['nj999988@gmail.com'],)
		messages.success(request,('THANKS! Your Message Has been sent'))
		return render(request, 'about.html',{})

	else:
		return render(request, 'about.html',{})

def delete(request, list_id):
	try:
		item = List.objects.get(pk=list_id)
	except List.DoesNotExist:
		messages.error(request,'You are not authorised to delete that item')
	if item.user != request.user:
		messages.error(request,'You are not authorised to cross_off that item')
		return redirect('list')	
	else:
		item.delete()
		messages.success(request,('The item has been deleted'))
		return redirect('list')

def cross_off(request,list_id):
	try:
		item = List.objects.get(pk=list_id)
	except List.DoesNotExist:
		messages.error(request,'You are not authorised to cross_off that item')
	if item.user != request.user:
		messages.error(request,'You are not authorised to cross_off that item')
		return redirect('list')	
	else:
		item.completed = True
		item.save()
		return redirect('list')	


def uncross(request,list_id):	
	try:
		item = List.objects.get(pk=list_id)
	except List.DoesNotExist:
		messages.error(request,'You are not authorised to uncross that item')
	if item.user != request.user:
		messages.error(request,'You are not authorised to uncross that item')
		return redirect('list')	
	else:
		item.completed = False
		item.save()
		return redirect('list')	

def edit(request,list_id):
	if request.method == 'POST':
		try:
			item = List.objects.get(pk=list_id)
		except List.DoesNotExist:
			messages.error(request,'You are not authorised to edit that item')
		if item.user == request.user:
			form = item
			form.item = request.POST.get("item")
			form.save()
			messages.success(request, 'Items has been edited')
			return redirect('list')
		else:
			messages.error(request,'You are not authorised to edit that item')
			return redirect('list')		

	else:
		try:
			item = List.objects.get(pk=list_id)
		except List.DoesNotExist:
			messages.error(request,'You are not authorised to edit that item')
			return redirect('list')	
		if item:
			if item.user != request.user:
				messages.error(request,'You are not authorised to edit that item')
				return redirect('list')	
			else:
				return render(request, 'edit.html',{'item':item})
		else:
			messages.error(request,'You are not authorised to edit that item')
			return redirect('list')	


def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,('You have successfully Logged IN!'))
			return redirect('home')
		else:
			messages.error(request,('Error Login! Please retry...'))
			return redirect('login')

	else:
		return render(request,'login.html',{})

def logout_user(request):
	logout(request)
	messages.success(request,('You Have been Logged OUT!'))
	return redirect ('home')


def td_list(request):

	if request.user.is_authenticated:
		if request.method == 'POST':
			form = List()
			form.item = request.POST.get("item")
			form.user = request.user
			
			if form:
				form.save()
				messages.success(request, 'Item Has been Added!')
				return redirect('list')

			else:
				messages.error(request,('Error Adding ! Please retry...'))
				messages.error(request,(form.errors))
				return redirect('list')
	

		else:
			name = request.user 
			all_items = List.objects.filter(user=name.id)
			return render(request, 'list.html',{'all_items':all_items})
	else:
		messages.info(request, 'You must login first')
		return redirect('login')



def  register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()		
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request,('You have successfully Registered...'))
			return redirect('home')
	else:
		form = SignUpForm()

	context = {'form':form}	
	return render(request, 'register.html',context)


def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request,('You have made changes to your Profile...'))
			return redirect('home')
	else:
		form = EditProfileForm(instance=request.user)

	context = {'form':form}	
	return render(request,'edit_profile.html',context)


def change_password(request):
	if request.method == 'POST':
		form = ChangePwdForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			messages.success(request,('You have made changed your Password...'))
			return redirect('home')
	else:
		form = ChangePwdForm(user=request.user)

	context = {'form':form}	
	return render(request,'change_password.html',context)


def r_login(request):
	return redirect('login')
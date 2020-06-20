from django.shortcuts import render,redirect 
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html',{})

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request,('The item has been deleted'))
	return redirect('home')

def cross_off(request,list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home')

def uncross(request,list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home')	

def edit(request,list_id):
	if request.method== 'POST':
		item = List.objects.get(pk=list_id)

		form = ListForm(request.POST or none,instance=item)

		if form.is_valid():
			form.save()
			messages.success(request, 'Items has been edited')
			return redirect('home')

	else:
		item = List.objects.get(pk=list_id)
		return render(request, 'edit.html',{'item':item})


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
			messages.success(request,('Error Login! Please retry...'))
			return redirect('login')

	else:
		return render(request,'login.html',{})

def logout_user(request):
	logout(request)
	messages.success(request,('You Have been Logged OUT!'))
	return redirect ('home')


def td_list(request):

	if request.method== 'POST':
		form = ListForm(request.POST or none)

		if form.is_valid():
			form.save()
			messages.success(request, 'Item Has been Added!')
			return HttpResponseRedirect(request.path_info)

	else:
		all_items = List.objects.all
		return render(request, 'list.html',{'all_items':all_items})
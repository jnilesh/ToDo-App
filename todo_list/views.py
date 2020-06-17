from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):

	if request.method== 'POST':
		form = ListForm(request.POST or none)

		if form.is_valid():
			form.save()
			messages.success(request, 'Your password has been changed successfully!')
			return HttpResponseRedirect(request.path_info)

	else:
		all_items = List.objects.all
		return render(request, 'home.html',{'all_items':all_items})

def about(request):
	return render(request, 'about.html',{})
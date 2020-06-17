from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def home(request):

	if request.method== 'POST':
		form = ListForm(request.POST or none)

		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request, ('Item Added to the List!'))
			return render(request, 'home.html',{'all_items':all_items , 'messages':'Item Added to the List!' })

	else:
		all_items = List.objects.all
		return render(request, 'home.html',{'all_items':all_items})

def about(request):
	return render(request, 'about.html',{})
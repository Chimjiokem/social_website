from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm


@login_required
def image_create(request):
	if request.method == 'POST':
		#form is sent
		form = ImageCreateForm(data=request.POST)
		if form.is_valid():
			#form data is valid
			cd = form.cleaned_data
			new_image = form.save(commit=False)
			#assign current user to the item
			new_image.user = request.user
			#save new item
			new_image.save()
			messages.success(request,'Image added successfully')
			#redirect to new created item detail view
			return redirect(new_image.get_absolute_url())
	else:
		#create a blank form with data provided by the bookmarklet via GET
		form = ImageCreateForm(data=request.GET)
	return render(request,'images/image/create.html', {'section':'images','form':form})


# Create your views here.

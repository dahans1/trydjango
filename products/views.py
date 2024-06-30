from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product

# Create your views here.
# def product_create_view(request):
# 	my_form = RawProductForm()
# 	if request.method == "POST":
# 		my_form = RawProductForm(request.POST)
# 		if my_form.is_valid():
# 			print(my_form.cleaned_data)
# 			Product.objects.create(**my_form.cleaned_data)
# 		else:
# 			print(my_form.errors)
# 	context = {
# 		'form': my_form
# 	}
# 	return render(request, "products/product_create.html", context)


# def product_create_view(request):
# 	title = request.POST.get('title')
# 	context = {}
# 	return render(request, "products/product_create.html", context)
def product_list_view(request):
	queryset = Product.objects.all() # list of objects
	context = {
		"object_list": queryset
	}
	return render(request, "products/product_list.html", context)

def product_delete_view(request, id):
	obj = get_object_or_404(Product, id=id)
	if request.method == "POST":
		# confirming delete
		obj.delete()
		return redirect('../../')
	context = {
		"object": obj
	}
	return render(request, "products/product_delete.html", context)

def render_initial_data(request):
	initial_data = {
		'title': "This is my awesome title"
	}
	obj = Product.objects.get(id=1)
	form = ProductForm(request.POST or None, instance=obj)
	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
		'form': form
	}

	return render(request, "products/product_create.html", context)
 

def product_detail_view(request, id):
	obj = get_object_or_404(Product, id=id)
	# context = {
	# 	'title': obj.title,
	# 	'description': obj.description,
	# 	'price': obj.price
	# }

	context = {
		'object': obj
	}

	return render(request, "products/product_detail.html", context)

def product_update_view(request, id):
	obj = get_object_or_404(Product, id=id)
	# context = {
	# 	'title': obj.title,
	# 	'description': obj.description,
	# 	'price': obj.price
	# }

	context = {
		'object': obj
	}

	return render(request, "products/product_detail.html", context)
 
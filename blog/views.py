from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	ListView,
	DeleteView
)

from .forms import ArticleForm
from .models import Article
# Create your views here.

class ArticleListView(ListView):
	template_name = 'blog/article_list.html'
	queryset = Article.objects.all() # <blog>/<modelname>_list.html>

class ArticleDetailView(DetailView):
	template_name = 'blog/article_detail.html'
	# queryset = Article.objects.all() # <blog>/<modelname>_detail.html>

	def get_object(self):
		id = self.kwargs.get("id")
		return get_object_or_404(Article, id=id)

class ArticleCreateView(CreateView):
	template_name = 'blog/article_create.html'
	form_class = ArticleForm
	queryset = Article.objects.all()

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

class ArticleUpdateView(UpdateView):
	template_name = 'blog/article_create.html'
	form_class = ArticleForm
	queryset = Article.objects.all()

	def get_object(self):
		id = self.kwargs.get("id")
		return get_object_or_404(Article, id=id)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

class ArticleDeleteView(DeleteView):
	template_name = 'blog/article_delete.html'

	def get_object(self):
		id = self.kwargs.get("id")
		return get_object_or_404(Article, id=id)

	def get_success_url(self):
		return reverse('blog:article-list')

# def article_create_view(request):
# 	form = ArticleForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = ArticleForm()

# 	context = {
# 		'form': form
# 	}
# 	return render(request, "blog/article_create.html", context)

# def article_detail_view(request, id):
# 	obj = get_object_or_404(Article, id=id)

# 	context = {
# 		'object': obj
# 	}
# 	return render(request, "blog/article_detail.html", context)

# def article_list_view(request):
# 	queryset = Article.objects.all()
# 	context = {
# 		"object_list": queryset
# 	}
# 	return render(request, "blog/article_list.html", context)
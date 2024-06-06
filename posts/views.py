from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostCreationForm, PostUpdateForm




class TempView(TemplateView):
    template_name = 'posts/home.html'

class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/post_base.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user = self.request.user)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'title_asc':
            queryset = queryset.order_by('title')
        elif sort_by == 'title_desc':
            queryset = queryset.order_by('-title')
        elif sort_by == 'created_at_asc':
            queryset = queryset.order_by('created_at')
        elif sort_by == 'created_at_desc':
            queryset = queryset.order_by('-created_at')
        elif sort_by == 'completed_desc':
            queryset = queryset.order_by('-completed')
        elif sort_by == 'completed_asc':
            queryset = queryset.order_by('completed')
        elif sort_by == 'target_date_desc':
            queryset = queryset.order_by('-target_date')
        elif sort_by == 'target_date_asc':
            queryset = queryset.order_by('target_date')
        return queryset



class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'

    def get_queryset(self):
        base_qs = super(PostDetail, self).get_queryset()
        return base_qs.filter(user=self.request.user)
    


class PostCreate(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_form.html'
    model = Post
    form_class = PostCreationForm
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'The Post created!')
        return super(PostCreate, self).form_valid(form)
    
class PostUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'posts/post_update.html'
    model = Post
    success_url = reverse_lazy('posts')
    form_class = PostUpdateForm

    def form_valid(self, form):
        messages.success(self.request, 'Post Updated!')
        return super(PostUpdate, self).form_valid(form)
    
    def get_queryset(self):
        base_qs = super(PostUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)
    

class PostDelete(LoginRequiredMixin, DeleteView):
    template_name = 'posts/post_delete.html'
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        messages.success(self.request, 'Post Deleted!')
        return super(PostDelete, self).form_valid(form)
    
    def get_queryset(self):
        base_qs = super(PostDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)
    

    
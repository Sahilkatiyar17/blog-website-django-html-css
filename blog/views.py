from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView ,DetailView , CreateView , UpdateView , DeleteView 

# Create your views here.

'''POSTS=[
    {'author':'sahil katiyar',
     'title':'tree',
     'content':'first post content',
     'date_posted':'august 23, 2023'},
    {'author':'kashish katiyar',
     'title':'sun',
     'content':'second post content',
     'date_posted':'august 30, 2023'
        
    }
]'''

def home(request):
    context={
        'POSTS':Post.objects.all(),
        'title':"Home"
        
    }
    return render(request,'home.html',context)

class PostListView(ListView):
    model=Post 
    template_name='home.html'
    context_object_name='POSTS'
    ordering=['-date_posted']
    
class PostDetailView(DetailView):
    model=Post 
    template_name='post_detail.html'
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post 
    fields=['title','content']
    template_name='post_form.html'
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
            
           
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post 
    fields=['title','content']
    template_name='post_form.html'
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
            
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):  
    model=Post 
    template_name='post_confirm_delete.html'
    success_url='/blog'
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False         
        
            
    
def about(request):
    context_1={
        
        'title':"About"
    }
    return render(request,'about.html',context_1)

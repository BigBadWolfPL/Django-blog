from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # do functionBasedView
from django.contrib.auth.forms import UserCreationForm





##################################################################

class PostListView(ListView):
    model = Post                                              # <----------
    template_name = 'blog/home.html'                          # blog/post_list.html (error domyslna nazwa templatu post_list)  <app>/<model>_<viewtype>.html
    context_object_name = 'posts'                             # domyslna nazwa obiektu to'object'
    ordering = ['-date_posted']                               # - zmiana kolejności
    paginate_by = 10


def to_samo_co_posts_list_view(request):                      # <----------
    posts = Post.objects.all().order_by('-date_posted')

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/to_samo_co_posts_list_view.html', {'posts': posts})

#def home(request):                                           # <----------
#    context = {
#        'posts': Post.objects.all().order_by('-date_posted')                         
#    }
#    return render(request, 'blog/home.html', context)

##################################################################


class UserPostListView(ListView):
    model = Post                                              # <----------
    template_name = 'blog/user_posts.html'                          # blog/post_list.html (error domyslna nazwa templatu post_list)  <app>/<model>_<viewtype>.html
    context_object_name = 'posts'                             # domyslna nazwa obiektu to'object'
    #ordering = ['-date_posted']                               # - zmiana kolejności
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):                             # Zachowane domyślne nazwy (w tamplacie nazwa zmiennej object)
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):         # Zachowane domyślne nazwy
    model = Post                                              # Dla Create oczekiwana nazwa obiektu to 'form'
    fields = ['title', 'content']                             # LoginRequiredMixin nowe posty tylko przez zalogowanych
    
    def form_valid(self, form):                               # Your PostCreateView creates instances of Post and you have set fields = ['title','content'] meaning only these fields would show up in the form. 
        form.instance.author = self.request.user              # But you have a field author which is non-nullable and without a default, hence you need to set a value for this field too.
        messages.success(self.request, f'Post Successfully Created!')            
        return super().form_valid(form)                       # If you want to set it to the current logged in user you can override the form_valid method of the form and do it there

    def get_success_url(self):                                # dodatkowo stworzyć metode get_absolute_url w models.py aby przekierować do strony nowego posta      
        return reverse('blog-home')                           # lub tutaj metode get_success_url aby przekierowac do str głównej >>  bo wywala błąd o przekierowaniu


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):   # Używa tego samego tamplatu co PostCreateView , dodatkowo UserPassesTestMixin aby edycja tylko przez autora posta
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Post Updated!')      # w modelu należy dodać self.request! pamiętać o tym!
        return super().form_valid(form)

    def test_func(self):                                      # Sprawdzenie czy osoba chcąca edytować jest autorem
        post = self.get_object()
        return self.request.user == post.author               # Można zrobić z if self.request.user == post.author: return True, else: False

    def get_success_url(self):
        return reverse('blog-home')


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    #success_url = '/'                                         # Wystarczy success = '<adres_strony>' zamiast metody get_success_url
        
    def test_func(self):                                      # Sprawdzenie czy osoba chcąca usunąć jest autorem.
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    def get_success_url(self):
        messages.success(self.request, f'Post Deleted!')
        return reverse('blog-home')


def index(request):
    return render(request, 'blog/index.html', {'title': 'About'})


#class GTemeView(LoginRequiredMixin, ListView):
#    model = Post
#    template_name = 'blog/index.html'


class TestTemplateView(TemplateView):
    template_name = 'blog/test.html'



def search(request):
    if request.method == 'POST':
        wyszukanie = request.POST['searched']
        posty = Post.objects.filter(content__contains=wyszukanie)   # xxx__contains=wyszukanie   (xxx=np title z modelu Post, moze być content itd)  
        if len(wyszukanie) > 0:
            return render(request, 'blog/search.html', 
            {'wyszukanie': wyszukanie,
            'posty': posty})
        else:
            return render(request, 'blog/search.html')






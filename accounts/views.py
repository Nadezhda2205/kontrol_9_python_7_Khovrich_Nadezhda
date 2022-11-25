from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.urls import reverse 
from django.contrib.auth.mixins import LoginRequiredMixin




from accounts.forms import LoginForm, CustomUserСreationForm, AccountUpdateForm
from accounts.models import Account



class LoginView(TemplateView):
    template_name = 'accounts/login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')

        username: str = form.cleaned_data.get('username')
        password: str = form.cleaned_data.get('password')
        user = authenticate(request=request, username=username, password=password)

        if not user:
            return redirect('login')

        login(request, user)

        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')
    

class RegisterView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CustomUserСreationForm
    succes_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class IndexView(TemplateView):
    template_name = 'index.html'

    
class AccountDetailView(DetailView):
    '''детальный просмотр аккаунта'''
    model = get_user_model()
    context_object_name = 'account'

    def get_object(self, queryset=None):
        return get_object_or_404(get_user_model(), username=self.kwargs.get('slug'))


class AccountUpdateView(UpdateView):
    '''редактирование аккаунта'''
    template_name = 'accounts/account_update.html'
    model = get_user_model()
    form_class = AccountUpdateForm

    def get_object(self, queryset=None):
        return get_object_or_404(Account, username=self.kwargs.get('slug'))
    
    def get_success_url(self):
        return reverse('account_detail', kwargs={'slug': self.object.username})

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.get_object() == request.user:
    #         return self.handle_no_permission()
    #     return super().dispatch(request, *args, **kwargs)


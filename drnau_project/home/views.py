from django.shortcuts import render
from django.views.generic import FormView,View, TemplateView
from .forms import SimpleForm
from django.conf import settings
from django.contrib.auth import login as auth_login, logout as auth_logout
import django.contrib.auth
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth import authenticate as auth
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.forms.util import ErrorList
from django.forms.forms import NON_FIELD_ERRORS
# Create your views here.
class Login(FormView):
    form_class=SimpleForm
    template_name ='home/login.html'

    def form_valid(self, form):
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            #verifica si el navegador acepta cookies si las acepta luego borra
            redirect_to=settings.LOGIN_REDIRECT_URL
            auth_login(self.request, user)
            if self.request.session.test_cookie_worked():
                self.request.session.delete_test_cookie()
        else:
            redirect_to=settings.LOGIN_URL
            #para agregar un error a una cierta etiqueta
            # errors=form._errors.setdefault("username", ErrorList())
            # errors.append("Please correct the errors below and resubmit.")
            #para mostrar un error no relacionado a ninguna etiqueta
            errors=form._errors.setdefault("__all__", ErrorList())
            errors.append("Parece que algo no esta bien!!.")
            #messages.error(self.request, "Please correct the errors below and resubmit.")
            return self.render_to_response(self.get_context_data(form=form))
        return HttpResponseRedirect(redirect_to)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(Login,self).dispatch(request,*args,**kwargs)

class Logout(View):
    def get(self,request,*args,**kwargs):
        auth_logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)


# from django.conf import settings
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.http import HttpResponseRedirect
# from django.utils.decorators import method_decorator
# from django.views.decorators.debug import sensitive_post_parameters
# from django.views.generic import FormView, View
# from .forms import SimpleForm
#
# class Login(FormView):
#     form_class = SimpleForm
#     template_name ='home/login.html'
#     def form_valid(self, form):
#         redirect_to = settings.LOGIN_REDIRECT_URL
#         auth_login(self.request, form.get_user())
#         if self.request.session.test_cookie_worked():
#             self.request.session.delete_test_cookie()
#         return HttpResponseRedirect(redirect_to)
#
#     def form_invalid(self, form):
#         print(form.get_user(self))
#         return self.render_to_response(self.get_context_data(form=form))
#
#     @method_decorator(sensitive_post_parameters('password'))
#     def dispatch(self, request, *args, **kwargs):
#         request.session.set_test_cookie()
#         return super(Login, self).dispatch(request, *args, **kwargs)
#
# class Logout(View):
#     def get(self, request, *args, **kwargs):
#         auth_logout(request)
#         return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
#     #
#     #success_url="/"

# class Login(TemplateView):
#     template_name = 'home/login.html'
#     def post(self, request):
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = auth.authenticate(username=username, password=password)
#
#         if user is not None:
#             if user.is_active:
#                 auth.login(request, user)
#                 return redirect('dr:index')
#             else:
#                 return render(request, 'dru/home.html', {
#                     'not_active':('Please Contact The Service Provider.'),
#                     })
#         else:
#             return render(request, 'dru/home.html', {
#                 'error_message': _('Invalid Login'),
#                 })
# from django.core.urlresolvers import reverse
# class Login(FormView):
#
#     form_class = SimpleForm
#     template_name = 'home/login.html'
#
#     def get_success_url(self):
#         return reverse("<url to redirect after login>")
#
#     def get_context_data(self, **kwargs):
#         context = super(Login, self).get_context_data(**kwargs)
#         form_class = self.get_form_class()
#         form       = self.get_form(form_class)
#         context['form'] = form
#         # code for other objects to pass to the template
#         return context
#
#     def form_valid(self, form):
#
#         form.save(commit=False)
#         # code to use login form values
#         form.save()
#         return super(Login, self).form_valid(form)
#
#     def form_invalid(self, form):
#         print("no valido")
#         error = "Incorrect Access Key provided. Try again !!"
#         return self.render_to_response(self.get_context_data(form=form, error=error))
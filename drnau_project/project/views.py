from pathlib import _Accessor
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView,DeleteView, FormView
from django.core.urlresolvers import reverse, reverse_lazy
from .forms import ProjectForm,ShowTVForm,PrototypeForm,ScheduleForm, proyectoForm
from .models import Project,Schedule,ShowTv
from django.shortcuts import get_object_or_404
# Create your views here.
def add_project(request):
    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            new_project=form.save()
            return HttpResponseRedirect('/list-project')
    else:
        form=ProjectForm()

    return render_to_response("project_form.html",locals(), context_instance=RequestContext(request))


class ProjectListing(ListView):
    model = Project

class ProjectCreate(CreateView):
    model = Project
    success_url = '/'

class ProjectDetail(DetailView):
    model = Project

class ProjectUpdate(UpdateView):
    model = Project
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse('detail', kwargs={'pk':self.object.pk, })

class ProjectDelete(DeleteView):
    model = Project
    success_url = '/'


class Prototype(CreateView):
    template_name = 'project_form.html'
    project = ProjectForm(prefix="projectForm")
    showtv= ShowTVForm(prefix="showTVForm")
    succes_url=reverse_lazy('success')

    def get_context_data(self, **kwargs):
        context=super(Prototype,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.project(initial={'some_field':context['model'].some_field})
        if 'form2' not in context:
            context['form2']=self.showtv(initial={'another_field':context['model'].some_field})
        return context

    def get_object(self):
        return get_object_or_404(Project, pk=self.request.session['someval'])

    def from_invalid(self,**kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()

        if 'form' in request.POST:
            project=self.get_project()
            form_name='form'
        else:
            project=self.showtv
            from_name='form2'
        form=self.get_form_class(project)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(**{form_name:form})


def add_project2(request):

    if request.method=='POST':
        form=ProjectForm(request.POST,prefix="projectForm")
        sub_form=ShowTVForm(request.POST,prefix="showTVForm")
        if form.is_valid() and sub_form.is_valid():
            new_project=form.save(commit=False)
            new_ShowTV=sub_form.save()
            new_project.save()
            return HttpResponseRedirect('/list-project')
    else:
        form=ProjectForm(prefix="projectForm")
        sub_form=ShowTVForm(prefix="showTVForm")

    return render_to_response("project_form2.html",locals(), context_instance=RequestContext(request))



class MainView(FormView):
    template_name = "your_template.html"

    def get_context_data(self, *args, **kwargs):
        request = kwargs['request']
        user = self.request.user

        try:
            project_instance = user.project
        except:
            project_instance = Project(user=self.request.user)

        try:
            showtv_instance = user.showtv
        except:
            showtv_instance = ShowTv(user=self.request.user)

        try:
            prototype_instance = user.prototype
        except:
            prototype_instance = Prototype(user=self.request.user)

        try:
            schedule_instance = user.schedule
        except:
            schedule_instance = Schedule(user=self.request.user)

        context = super(MainView, self).get_context_data(**kwargs)
        context['project'] = ProjectForm(instance='project_instance')
        context['showtv'] = ShowTVForm(instance='showtv_instance')
        context['prototype'] = PrototypeForm(instance='prototype_instance')
        context['schedule'] = ScheduleForm(instance='schedule_instance')

        return context

    def get(self, request, *args, **kwargs):
        user = request.user
        context = self.get_context_data(request=request, **kwargs)
        return self.render_to_response(context)

class SaveProject(FormView):
    template_name = "new_project.html"

    def post(self, request, *args, **kwargs):
        print("guardado")
        #some logic to save the SaveForm

class Prueba(FormView):
    template_name = 'project/prueba.html'
    form_class = proyectoForm
    success_url="/"
    #def get_success_url(self):
     #   return reverse('project/prueba.html')

  #  def get(self, *args, **kwargs):
        #return HttpResponse(self.template_name)

    def form_valid(self, form):
        print(self.request.POST['nameProject'])
        print(self.request.POST['version'])
        name=form.cleaned_data['nameChannel']
        live=form.cleaned_data['typeTrans']
        station= ShowTv(st_channel=name,st_live=live)
        station.save()
        time=form.cleaned_data['scheduleTime']
        schedule=Schedule(sch_st_id=station,sch_time=time)
        schedule.save()
        print ("id " + str(station.id))
        print(station.st_channel)
        print(station.st_live)
        return super(Prueba, self).form_valid(form)
__author__ = 'Franco'
from django import forms
from .models import Project,ShowTv,Prototype,Schedule
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProjectForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        self.helper=FormHelper(self)
        self.helper.form_method='POST'
        #agrega el boton
        self.helper.add_input(Submit('submit','Submit'))

    class Meta:
        model=Project
        #cuales fields queremos
        fields=('proj_name',)

class ShowTVForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(ShowTVForm,self).__init__(*args,**kwargs)
        self.helper=FormHelper(self)
        self.helper.form_method='POST'
        self.helper.add_input(Submit('submit','Submit'))

    class Meta:
        model=ShowTv

class PrototypeForm(forms.Form):
    class Meta:
        model = Prototype
        fields = '__all__' # if you are going to use all the fields


class ScheduleForm(forms.Form):
    class Meta:
        model = Schedule
        fields = '__all__' # if you are going to use all the fields

TRANSMISSION = (('1','Vivo'),('2','Grabado'))
CHOICES = (('si', 'True'), ('no', 'False'))
class proyectoForm(forms.Form):
    nameProject=forms.CharField(label="Nombre del Proyecto",max_length=30,required=True)
    nameChannel=forms.CharField(label="Nombre del Canal",max_length=30)
    typeTrans=forms.ChoiceField(label="Tipo de Transmisión",choices=TRANSMISSION)
    version=forms.IntegerField(label="Version")
    #relacionado=forms.CheckboxSelectMultiple(choices=CHOICES)
    linkContent=forms.BooleanField(label="Relacionado con el contenido",widget=forms.CheckboxInput(),required=False)
   # my_date = forms.DateField(initial=date.today(), widget=forms.DateInput(format = '%d.%m.%Y'), input_formats=('%d.%m.%Y',))
    #hora=forms.DateField(widget=forms.DateInput(format = '%m/%d/%Y'), input_formats=('%d/%m/%Y',))
    scheduleTime=forms.TimeField(label="Hora de Emisión",input_formats=['%H:%M','%I:%M %p'],
                      widget=forms.TimeInput(attrs={'size':'8','class':'time_field'},format=["%H:%M","%I:%M %p"]),required=False)
    def __init__(self,*args,**kwargs):
        self.helper=FormHelper()
        self.helper.add_input(Submit('submit','Enviar'))
        super(proyectoForm,self).__init__(*args,**kwargs)



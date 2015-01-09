from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TRANSMISSION = (('1','Vivo'),('2','Grabado'))

class Project(models.Model):
    proj_name = models.CharField(max_length=30, unique=True, verbose_name='Nombre del Proyecto')
    proj_date = models.DateField(auto_now_add=True)
    proj_user = models.ForeignKey(User, related_name="project_user", verbose_name='Usuario')
    proj_description = models.CharField(max_length=150, verbose_name="Descripción", blank=True)
    def __str__(self):
        return self.proj_name

class ShowTv(models.Model):
    st_channel = models.CharField(max_length=30)
    st_name = models.CharField(max_length=30, blank=True)
    st_live = models.CharField(max_length=1, default='2', choices=TRANSMISSION)
    def __str__(self):
        return self.st_channel

class Prototype(models.Model):
    pro_proj_id = models.ForeignKey(Project, related_name="prototype_project")
    pro_version = models.IntegerField()
    pro_link_content = models.BooleanField(default=True)
    pro_sho_id = models.ForeignKey(ShowTv, related_name="prototype_showtv")
    pro_date = models.DateField(auto_now_add=True)
    pro_date_update = models.DateField(auto_now=True)
    pro_name = models.CharField(max_length=30,verbose_name='Nombre del Prototipo')
    pro_description = models.CharField(max_length=150, verbose_name="Descripción", blank=True)
    def __str__(self):
        return self.pro_version

class Schedule(models.Model):
    sch_st_id = models.ForeignKey(ShowTv, related_name="schedule_showtv")
    sch_time = models.TimeField()

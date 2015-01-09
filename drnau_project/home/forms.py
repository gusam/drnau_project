__author__ = 'Franco'
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field,Button
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

class SimpleForm(forms.Form):
    username = forms.CharField(label="Usuario", required=True)
    password = forms.CharField(
        label="Contraseña", required=True, widget=forms.PasswordInput)
    remember = forms.BooleanField(label="Remember Me?",required=False)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-4'
    helper.field_class = 'col-lg-7'
    helper.layout = Layout(
        PrependedText('username',
                      '<span class="glyphicon glyphicon-user"></span> ',
                      css_class='input-lg'),
        PrependedText('password',
                      '<span class="glyphicon glyphicon-asterisk"></span> ',
                      css_class='input-lg'),
        FormActions(
            #/*Submit('login', 'Ingresar ', css_class="btn-primary btn-lg"),*/
           Submit('login', 'Ingresar', css_class="btn-primary"),
           Button('cancel', 'Cancel',onclick="window.history.back()"),

        ),

    )





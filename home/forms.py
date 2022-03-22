
from django.forms import ModelForm, MultiValueField
from .models import VictimUser
#Creating Registration
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class DateInput(forms.DateInput):
    input_type = 'date'



class ReportingForm(ModelForm):
    screenshots = forms.FileField(widget=forms.FileInput(
        attrs={'class':'form-control','multiple':True}
    ))
    class Meta:
        model = VictimUser
        fields = "__all__"
        exclude=['screenshots_obj']
       
        widgets = { 
            'user':forms.HiddenInput(),
            'screenshot':forms.ClearableFileInput(
                attrs={'class':'form-control','multiple':True}
            ),
            'date_crime': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'datetime-local'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
            'user_adhar' : forms.TextInput(attrs={'class':'form-control'}), 
             'category_crime' : forms.Select(attrs={'class':'form-control'}),
             'suspected_person' : forms.TextInput(attrs={'class':'form-control'}),
             'suspected_email' : forms.TextInput(attrs={'class':'form-control'}),
             'mobile' : forms.TextInput(attrs={'class':'form-control'}), 
            #  'date_crime' :forms.DateInput(format='%d-%m-%Y', label='Date effet'),   
             'suspected_mobile' : forms.TextInput(attrs={'class':'form-control'}),      
              'crime_source' : forms.TextInput(attrs={'class':'form-control'}), 
              'id_usedby_criminal' :forms.TextInput(attrs={'class':'form-control'}),
            }    




class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts= {'password1':None,
            'password2':None,
            'username': None,
            'email': None,
            
            }

            
        


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
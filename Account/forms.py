from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserForm(UserCreationForm):
	phonenumber = forms.IntegerField(max_value=9999999999,label="Phone Number")
	Address =forms.CharField(max_length=100,label="Address")
	first_name=forms.CharField(max_length=30,label="firstname")
	last_name=forms.CharField(max_length=30,label="lastname")
	class Meta():
		
		model = User
		fields =['username','first_name','last_name','email','phonenumber','Address','password1','password2',]

		def save(self,commit=True):
			user=super(UserForm,self).save(commit=False)
			phonenumber=self.cleaned_data['phonenumber']
			Address=self.cleaned_data['Address']
			first_name=self.cleaned_data['first_name']
			last_name=self.cleaned_data['last_name']
			if commit:	
				user.save()
			return user

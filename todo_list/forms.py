from django import forms
from .models import List
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
#from .forms import SignUpform

class ChangePwdForm(PasswordChangeForm):

	class Meta:
		model = User
		fields = ('old_password','new_password1','new_password2',)

	def __init__(self, *args,**kwargs):
		super(ChangePwdForm,self).__init__(*args,**kwargs)

		self.fields['old_password'].widget.attrs['class'] = 'form-control'
		self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
		self.fields['old_password'].label = ''
		
		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
		self.fields['new_password1'].label = ''
		
		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['new_password2'].label = ''
			


		


class EditProfileForm(UserChangeForm):
	password = forms.CharField(label="",widget=forms.TextInput(attrs={'type':'hidden'}))
	email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
	first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
	last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password')

	def __init__(self, *args,**kwargs):
		super(UserChangeForm,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['username'].label = ''






class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder':'Email Address'}))
	first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'placeholder':'First Name'}))
	last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2',)

	def __init__(self, *args,**kwargs):
		super(SignUpForm,self).__init__(*args,**kwargs)

		# self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['username'].label = ''
		
		# self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		
		# self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
			
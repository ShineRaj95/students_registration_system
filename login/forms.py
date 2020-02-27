from django import forms



"""Class to create login form """ 

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=250,widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label='Password', max_length=250,widget=forms.PasswordInput(attrs={"class":"form-control"}))

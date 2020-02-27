from django import forms


"""Class to create student registration form"""

class RegistrationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=250,widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(label='Email', max_length=250,widget=forms.TextInput(attrs={"class":"form-control"}))
    age = forms.CharField(label='Age', max_length=10,widget=forms.NumberInput(attrs={"class":"form-control","min":"16","max":"50"}))
    phone_number=forms.CharField(label="Mobile",widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Address",widget=forms.Textarea(attrs={"row":2,"class":"form-control"}))
    GENDERCHOICES = (('Male', 'Male'),('female', 'Female'),)
    gender = forms.ChoiceField(choices=GENDERCHOICES,widget=forms.Select(attrs={'class':'form-control '})) 
    DEGREECHOICES = (('BCA', 'BCA'),('BCOM', 'BCOM'),('Bsc', 'Bsc'),('BTech', 'BTech'),('BA', 'BA'),('BBA', 'BBA'))
    course = forms.ChoiceField(choices=DEGREECHOICES,widget=forms.Select(attrs={'class':'form-control'})) 

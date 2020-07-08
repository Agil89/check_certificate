from django import forms

class HomeForm(forms.Form):
    verification = forms.CharField(label='verification' , widget=forms.TextInput(attrs={
        'class':'form-control',
    }),max_length=40)

    recaptcha_input = forms.CharField(label='verification' , widget=forms.TextInput(attrs={
        'class':'form-control',
    }),max_length=40)
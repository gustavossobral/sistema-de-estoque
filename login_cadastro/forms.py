from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(max_length=255, required=True)
    senha = forms.CharField(max_length=255, required=True)

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    senha_1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    senha_2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)


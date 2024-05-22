from django import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(label='Usuario', 
                                 max_length=100, 
                                 required=True, 
                                 widget=forms.TextInput(
                                     attrs={"class": "form-control", 
                                            "placeholder": "Digite o seu usuario"}))
    
    senha = forms.CharField(label="Senha", 
                            required=True, 
                            max_length=50, 
                            widget=forms.PasswordInput(
                                attrs={"class": "form-control", 
                                       "placeholder": "Digite sua senha"}))
    

class CadastroForms(forms.Form):
    nome_usuario = forms.CharField(label="Usuario",
                                    max_length=100,
                                    required=True,
                                    widget=forms.TextInput(
                                        attrs={"class": "form-control",
                                               "placeholder": "Crie um nome de usuario"}))
    
    email = forms.EmailField(label="E-mail", max_length=100,
                             required=True,
                             widget=forms.EmailInput(
                                 attrs= {"class": "form-control",
                                         "placeholder": "Insira o seu e-mail"}))
    
    senha = forms.CharField(label="Senha",
                            max_length=50,
                            required=True,
                            widget=forms.PasswordInput(
                                attrs={"class": "form-control",
                                       "placeholder": "Crie uma senha"}))
    
    confirma_senha = forms.CharField(label="Confirmação de senha",
                                     max_length=50,
                                     required=True,
                                     widget=forms.PasswordInput(
                                         attrs={"class": "form-control",
                                                "placeholder": "Confirme sua senha"}))
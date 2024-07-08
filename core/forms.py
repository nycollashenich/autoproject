from django import forms
from django.core.mail.message import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']

        content = f'Name:{name}\nE-mail: {email}\nMessage: {message}'  
        
        mail = EmailMessage(
            subject=message,
            body=content,
            from_email='contact@htop.com.br',
            to=['contact@htop.com.br'],
            headers={'Replay-To': email},
        )
        mail.send()
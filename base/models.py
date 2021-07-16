from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=12)
    whatsapp = models.CharField(max_length=14)
    texto = models.TextField()

    def save(self,*args,**kwargs):
        super(Contato, self).save(*args,**kwargs)
        data = {'cliente':self.nome,'email':self.email,'telefone':self.telefone,'whatsapp':self.whatsapp,'mensagem':self.texto}
        plain_text = render_to_string('email/email.txt',data)
        plain_html = render_to_string('email/email.html',data)
        send_mail(
            'Messagem de clientes do site!',
            plain_text,
            'contato@asaturismo.com',
            ['contato@asaturismo.com'],
            html_message=plain_html,
            fail_silently=False,)


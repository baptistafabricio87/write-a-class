from django.views.generic import TemplateView


# apresenta pagina home
class HomeTemplateView(TemplateView):
    template_name = 'index.html'


# apresenta pagina sobre
class AboutTemplateView(TemplateView):
    template_name = 'about-us.html'


# apresenta pagina contato
class ContactTemplateView(TemplateView):
    template_name = 'contacts.html'

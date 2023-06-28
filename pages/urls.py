from django.urls import path

from pages.views import (
    HomeTemplateView,
    AboutTemplateView,
    ContactTemplateView,
)

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('sobre/', AboutTemplateView.as_view(), name='sobre'),
    path('contato/', ContactTemplateView.as_view(), name='contato'),
]

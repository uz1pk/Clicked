from django.urls import path
from django.views.generic import TemplateView

app_name = 'clicked'

urlpatterns = [
    path('', TemplateView.as_view(template_name="clicked/index.html"))
]

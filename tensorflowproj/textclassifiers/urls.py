#from django.conf.urls import url
#from . import views
#
#urlpatterns = [
#    url(r'^$', views.home),
#]

from django.conf.urls import url
from textclassifiers.views import ClassifyView

urlpatterns = [
    url('classify/', ClassifyView.as_view(template_name="textclassifiers/classify.html")),
]
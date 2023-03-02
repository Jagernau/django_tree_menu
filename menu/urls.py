from django.urls import path
from .views import index, url_path


urlpatterns = [
     path('', index, name='index'),
     path('<str:menu_name>/', url_path, )
]


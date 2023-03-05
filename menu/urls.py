from django.urls import path
from .views import index, url_path


urlpatterns = [
     path('', index,),
     path('<path:menu_name>/', url_path),   
]


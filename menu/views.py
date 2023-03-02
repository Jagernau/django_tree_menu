
from django.shortcuts import render
 
def index(request):
    return render(request, "index.html")

def url_path(request, menu_name):
    return render(request, "index.html", {"menu_name": menu_name})

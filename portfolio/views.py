from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    projects = Project.objects.all()  # grabs info(objects) from the db
    return render(request, 'portfolio/home.html', {'projects':projects})  # pass into template a dictionary
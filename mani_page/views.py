from django.shortcuts import render
from .models import skillset
# Create your views here.
def main_index(request):
    skills = skillset.objects.all()
    return render(request,'index.html',{'skills':skills})

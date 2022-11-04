from django.shortcuts import render
from app.forms import *
# Create your views here.
def home(request):
    return render(request,'home.html')

def registration(request):
    uf=UserForm()
    pf=ProfileForm()
    d={'uf':uf,'pf':pf}
    return render(request,'registration.html',d)
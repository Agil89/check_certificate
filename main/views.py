from django.shortcuts import render
from main.forms import HomeForm

def home(request):
    
    if request.method == 'POST':
        form = HomeForm(request.POST)
    else:
        form = HomeForm()
    context = {
        'form': form
    }
    return render(request,'index.html',context)

def login(request):
    return render(request,'login.html')
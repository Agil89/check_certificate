from django.shortcuts import render
from main.forms import HomeForm
from main.models import Certificate

def home(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
    else:
        form = HomeForm()
    context = {
        'form': form
    }
    return render(request,'index.html',context)


def info(request):
    # a= '123'
    # certificate = Certificate.objects.get(certificade_number=a)
    # context = {
    #     'certificate' : certificate
    # }
    return render(request,'info.html')

    
def login(request):
    return render(request,'login.html')


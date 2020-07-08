from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def info(request):
    certificates = Certificate.objects.all()
    context = {
        'certificates' : certificates
    }
    return render(request,'info.html',context)
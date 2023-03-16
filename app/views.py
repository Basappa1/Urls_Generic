from django.shortcuts import render

# Create your views here.

def ok(request):
    return render(request,'ok.html')

def hmm(request):
    return render(request,'hmm.html')
    

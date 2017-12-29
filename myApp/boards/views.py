from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
def get( request):
        return render(request, 'login.html', context=None)
def disp(request):
    name=request.GET.get('uname')
    return HttpResponse("hello "+ name)


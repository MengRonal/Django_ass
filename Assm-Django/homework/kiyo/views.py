from django.shortcuts import render
from django.http import HttpResponse
from .models import BookList


# Create your views here.
def index(request):
    return render(request=request,template_name='index.html')
def home(request):
    return render(request=request,template_name='home.html')
def about(request):
    return render(request=request,template_name='about.html')
def contact(request):
    return render(request=request,template_name='contact.html')
def bookList(request):
    bkl = BookList.objects.all()
    return render(request=request,template_name='bookList.html',context={'b_list':bkl})

def buy(request , id):
    dt = BookList.objects.get(id=id)
    return render(request=request , template_name='buy.html' , context={'buy':dt})
def detail(request , id):
    dt = BookList.objects.get(id=id)
    return render(request=request , template_name='detail.html' , context={'detail':dt})
def searchresult(request):
    kw = request.GET.get('kw', '').strip()
    query = BookList.objects.filter(name__icontains=kw)
    return render(request, 'search-result.html', {
        'item': query,
        'query': kw,
    })

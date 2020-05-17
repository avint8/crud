from django.shortcuts import render
from django.http import HttpResponse
from app.models import table
from app.forms import formtable
from django.shortcuts import get_object_or_404

def index(request):
    form = formtable()
    if request.method == 'POST':
        name = request.POST['name']
        text = request.POST['text']
        s = table(name=name,text=text) 
        s.save()


    data = table.objects.all()
    return render(request,'index.html',{'form':form,'data':data})


def edit(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        text = request.POST['text']
        data = get_object_or_404(table,pk=id)
        data.name = name
        data.text = text
        data.save()
    data = table.objects.all()
    form = formtable()
    return render(request,'index.html',{'form':form,'data':data})

def delete(request):
    if request.method == "POST":
        id = request.POST['id']
        table.objects.get(pk=id).delete()
    data = table.objects.all()
    form = formtable()
    return render(request,'index.html',{'form':form,'data':data})


    
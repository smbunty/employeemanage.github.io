from django.shortcuts import render
from django.shortcuts import redirect
from . forms import EmpForm
from . models import Employe

# Create your views here.
def e(request):
    empForm=EmpForm()
    return render(request,'e.html',{'empForm':empForm})


def insert(request):
    if request.method=='POST':
        empForm=EmpForm(request.POST)
        if empForm.is_valid():
            empForm.save()
            return render(request,'show.html')
        else:
             return render(request,'signin.html')
    else:
         return render(request,'signin.html')

def get (request):
    employees=Employe.objects.all()
    return render (request,'show.html',{'employees':employees})
def edit (request,eid):
    emp=Employe.objects.get (eid=eid) 
    return render(request,'edit.html',{'emp':emp})
def update(request,eid):
    if request.method=='POST':
        emp=Employe.objects.get(eid=eid)
        form=EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect ('get')
            
        else:
            return render(request,'edit.html',{'emp':emp,'msg':'Details not update.....!!!'})
    else:
        return render(request,'edit.html',{'emp':emp,'msg':'Details not update.....!!!'})
           

def delete(request,eid):
        emp=Employe.objects.get(eid=eid)
        emp.delete()
        return redirect ('get')
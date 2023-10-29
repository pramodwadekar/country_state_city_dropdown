from django.shortcuts import render,redirect

from .models import *

# Create your views here.
def index(request):
    countries = Country.objects.all()
    states = State.objects.all()
    citys = City.objects.all()
    context ={"countries":countries, "states":states, "citys":citys}
    return render(request, "countries.html", context = context)


def add_data(request):
    if request.method == "POST":
        name = request.POST['fname']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        add_details = Member(name = name, country = country, state= state, city = city )
        add_details.save()
        return redirect('show_page')
    
def show_data(request):
    all_data = Member.objects.all()
    return render(request,"show_page.html",{'key1':all_data})

def edit_page(request,pk):
    countries = Country.objects.all()
    states = State.objects.all()
    citys = City.objects.all()
    udata = Member.objects.get(id=pk)
    return render(request,"update.html",{'key2':udata,"countries":countries, "states":states, "citys":citys})

def Updatedata(request,pk):
    udata= Member.objects.get(id = pk)
    udata.name = request.POST['fname']
    udata.country = request.POST['country']
    udata.state = request.POST['state']
    udata.city = request.POST['city']
    # Query for Update
    udata.save()
    # render on ShowPage 
    return redirect('show_page')

def deletedata(request,pk):
    ddata = Member.objects.get(id=pk)
    ddata.delete()
    return redirect('show_page')


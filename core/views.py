from django.shortcuts import redirect, render
from .models import Country,City,District,Event

# Create your views here.


def home(request):
    ## this is for printing the current locations
    events = Event.objects.all()
    countries = Country.objects.all()
#    citys = City.objects.all()
    
    ## if the value is post what shall we do
    if request.method == 'POST':
        event = Event()
        event.name = request.POST.get("event")
        event.location = District.objects.get(id=(request.POST.get("district")))
        #event.location = request.POST('district')
        #event.location = request.POST('district')
        print(event.name)
        print(event.location)
        event.save()
        return redirect('home')

    context = {
        'countries': countries,
        'events': events,
    }
    return render(request,'core/home.html',context)


def citys(request):
    country = str(request.GET.get('country'))
    citys = City.objects.filter(country=country)
    context = {
        'citys': citys,
    }
    return render(request, 'core/selection/citys.html', context)

def districts(request):
    city = str(request.GET.get('city'))
    districts = District.objects.filter(city=city)
    context = {
        'districts': districts,
    }
    return render(request, 'core/selection/districts.html', context)
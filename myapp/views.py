from django.shortcuts import render

# Create your views here.
def index(request):
    temp=38.7
    humidity=23.5
    wind=15
    city="zanzibar"
    is_sunny=True
    users=["jane","jack","Mohammad"]
    #package
    context={
        'temperature':temp,
        'humidity':humidity,
        'windspeed':wind,
        'city':city,
        'is_sunny':is_sunny,
        'users':users

    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
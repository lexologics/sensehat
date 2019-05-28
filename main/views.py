from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import ListView, TemplateView

from .models import SensorHeat
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response

from sense_hat import SenseHat

import os

#from django.http import HttpResponse
#from sense_hat import SenseHat

User = get_user_model()

p = (204, 0, 204)  # pink
g = (0, 102, 102)  # Green
w = (200, 200, 200) # White
#y = (204, 204, 0) # yellow
y = (255, 255, 0) # yellow
r = (255, 0, 0) # red
e = (0, 0,0 )     # Empty


PET1 = [
        e, e, e, e, e, e, e, e,
        p, e, e, e, e, e, e, e,
        e, p, e, e, p, e, p, e,
        e, p, g, g, p, y, y, e,
        e, g, g, g, y, w, y, g,
        e, g, g, g, g, y, y, e,
        e, g, e, g, e, g, e, e,
        e, e, e, e, e, e, e, e
    ]

PET2 = [
        e, e, e, e, e, e, e, e,
        p, e, e, e, e, e, e, e,
        e, p, e, e, p, e, p, e,
        e, p, g, g, p, y, y, e,
        e, g, g, g, y, w, y, g,
        e, g, g, g, g, y, y, e,
        e, e, g, e, g, e, e, e,
        e, e, e, e, e, e, e, e
    ]


def homepage(request):
    return render(request, 'main/home.html')


#class ShowTextView(TemplateView):
#    template_name = 'show_text.html'
#    @method_decorator(login_required)    
#    return render(request, 'main/show_text.html')

def show_text(request):
    return render(request, 'main/show_text.html')

def save_sensors(request):
    #@login_required
    user = User.objects.get(id=3)
    sense = SenseHat()
    
    sensor = sense.get_temperature()
    title = 'Sense Hat - CPU Temp'
    create_record = SensorHeat(title=title, sensor_data=sensor, author_id=user.id)
    create_record.save()
    return redirect('/sensors/', {'user': user, "title": title})

def sensors(request):

    from sense_hat import SenseHat
    import os

    # RPi CPU
    pitemp = os.popen("vcgencmd measure_temp").readline()
    pitemp = pitemp.replace("temp=", "")
    sense = SenseHat()
    temp = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    get_mem_arm = os.popen("vcgencmd get_mem arm").readline()
    get_mem_gpu = os.popen("vcgencmd get_mem gpu").readline()

    measure_volts_core = os.popen("vcgencmd measure_volts core").readline()
    measure_volts_sdram_c = os.popen("vcgencmd measure_volts sdram_c").readline()
    measure_volts_sdram_i = os.popen("vcgencmd measure_volts sdram_i").readline()
    measure_volts_sdram_p = os.popen("vcgencmd measure_volts sdram_p").readline()

    sensor = SensorHeat.objects.all().order_by('-date_posted')
    
    #print("Temperature: %s C" % temp)

    # alternatives
    #print(sense.temp)
    #print(sense.temperature)

    context = {
        'pitemp': pitemp,
        'temp': temp,
        'sense': sense,
        'pressure': pressure,
        'humidity': humidity,
        'get_mem_arm': get_mem_arm,
        'get_mem_gpu': get_mem_gpu,

        'measure_volts_core': measure_volts_core,
        'measure_volts_sdram_c': measure_volts_sdram_c,
        'measure_volts_sdram_i': measure_volts_sdram_i,
        'measure_volts_sdram_p':  measure_volts_sdram_p,

        'sensor': sensor,
        
        'title': 'Temperature'
        }
    return render(request, 'main/sensors.html', context)

#class SensorHeatListView(ListView):
#    model = SensorHeat
#    template_name = 'main/sensors.html'
#    context_object_name = 'sensor'#
#    ordering = ['-date_posted']

#@login_required
def rgbmod(request):

    from sense_hat import SenseHat
    import time

    sense = SenseHat()

    p = (204, 0, 204)  # pink
    g = (0, 102, 102)  # Green
    w = (200, 200, 200) # White
    #y = (204, 204, 0) # yellow
    y = (255, 255, 0) # yellow
    r = (255, 0, 0) # red
    e = (0, 0,0 )     # Empty

    pet1 = [
	e, e, e, e, e, e, e, e,
	p, e, e, e, e, e, e, e,
	e, p, e, e, p, e, p, e,
	e, p, g, g, p, y, y, e,
	e, g, g, g, y, w, y, g,
	e, g, g, g, g, y, y, e,
	e, g, e, g, e, g, e, e,
	e, e, e, e, e, e, e, e
    ]

    pet2 = [
	e, e, e, e, e, e, e, e,
	p, e, e, e, e, e, e, e,
	e, p, e, e, p, e, p, e,
	e, p, g, g, p, y, y, e,
	e, g, g, g, y, w, y, g,
	e, g, g, g, g, y, y, e,
	e, e, g, e, g, e, e, e,
	e, e, e, e, e, e, e, e
    ]

    love = [
	e,e,e,e,e,e,e,e,
	e,r,r,e,e,r,r,e,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	e,r,r,r,r,r,r,e,
	e,e,r,r,r,r,e,e,
	e,e,e,r,r,e,e,e,
	e,e,e,e,e,e,e,e
    ]

    pacman = [
	e,e,y,y,y,y,e,e,
	e,y,y,y,y,y,y,e,
	y,y,y,y,y,y,y,y,
	y,y,y,y,y,y,e,e,
	y,y,y,y,y,y,e,e,
	y,y,y,y,y,y,y,y,
	e,y,y,y,y,y,y,e,
	e,e,y,y,y,y,e,e
    ]

#    pacman2 = [
#        e,e,y,y,y,y,e,e,
#        e,y,y,y,y,y,y,e,
#        y,y,y,y,y,y,y,y,
#        y,y,y,y,y,y,y,e,
#        y,y,y,y,y,y,e,e,
#        y,y,y,y,y,y,y,y,
#        e,y,y,y,y,y,y,e,
#        e,e,y,y,y,y,e,e
#    ]

    sense.set_pixels(pet1)
    time.sleep(1)
    sense.set_pixels(pet2)
    time.sleep(1)
    sense.set_pixels(love)
    time.sleep(1)
    sense.set_pixels(pacman)
    time.sleep(1)
#    sense.set_pixels(pacman2)
#    time.sleep(5)

    sense.clear()

    return render(request, 'main/rgb.html')

#@login_required
def walking(request):
    
    from sense_hat import SenseHat
    import time

    global PET1
    global PET2

    sense = SenseHat()

    for i in range(10):
        sense.set_pixels(PET1)
        time.sleep(0.5)
        sense.set_pixels(PET2)
        time.sleep(0.5)

    sense.clear()

    return render(request, 'main/walking.html')

# JavaScript Graph
def get_data(request, *args, **kwargs):
    data = {
        'sales': 100,
        'customers': 10,
        }
    return JsonResponse(data)

# REST Framework
#@login_required
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            'sales': 100,
            'customers': 10,
            'users': User.objects.all().count(),
        }
        return Response(data)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:sensors')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request, 'main/register.html', context={'form':form})

#@login_required
def logout_request(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect('main:sensors')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, 'You are now logged in as {user}')
                return redirect('main:sensors')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')

    form = AuthenticationForm()
    return render(request, 'main/login.html', {'form':form})



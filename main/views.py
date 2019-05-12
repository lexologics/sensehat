from django.shortcuts import render

#from django.http import HttpResponse
#from sense_hat import SenseHat

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

def sensors(request):

    from sense_hat import SenseHat

    sense = SenseHat()
    temp = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    #print("Temperature: %s C" % temp)

    # alternatives
    #print(sense.temp)
    #print(sense.temperature)

    context = {
        'temp': temp,
        'sense': sense,
        'pressure': pressure,
        'humidity': humidity,
        'title': 'Temperature'
        }
    return render(request, 'main/sensors.html', context)

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


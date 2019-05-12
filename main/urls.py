from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('walking/', views.walking, name='walking'),
    path('rgb/', views.rgbmod, name='rgbmod'),
    path('sensors/', views.sensors, name='sensors'),
]


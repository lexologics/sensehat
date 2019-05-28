from django.urls import path
#from .views import SensorHeatListView
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('walking/', views.walking, name='walking'),
    path('rgb/', views.rgbmod, name='rgbmod'),
    path('sensors/', views.sensors, name='sensors'),
    #path('sensors/', SensorHeatListView.as_view(), name='sensors'),
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('create/', views.save_sensors, name='save_sensors'),
    path('show_text/', views.show_text, name='show_text'),
    path('api/data/', views.get_data, name='get_data'),
    path('api/', views.ChartData.as_view()),
]


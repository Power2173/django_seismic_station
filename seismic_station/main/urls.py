from django.urls import path
from . import views


urlpatterns = [
    path("", views.main_page, name = "home"),
    path("about/", views.about),
    path("list_sensor/", views.CreateSensorView.as_view()),
    path("list_sensor/<int:ind>/", views.sensor_info, name = 'monitor-list_station'),
]
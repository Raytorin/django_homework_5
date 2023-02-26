from django.urls import path

from measurement.views import SensorView, SensorChangeView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorChangeView.as_view()),
    path('measurements/', MeasurementView.as_view())
]

from django.conf.urls import url
from . import views

app_name = 'sensor_owner'

urlpatterns = [
    url(r'^overview$', views.ShowSensorsView.as_view(), name='ownerDashboard'),
    url(r'^manage$', views.AddSensorView.as_view(), name='ownerManage'),
]

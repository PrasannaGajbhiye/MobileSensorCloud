from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [

    url(r'^dashboard$', views.ShowDashboardView.as_view(), name='dashboard'),
    #url(r'^(?P<pk>[0-9]+)/$', views.sensorDataView, name='sensor-data'),
]

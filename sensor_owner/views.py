from django.shortcuts import render
from django.views.generic import View

from sensor_owner.forms import AddSensorForm
from sensor_owner.models import SensorDetails



def OwnerDashboard(request):
    return render(request, 'sensor_owner_home.html', {})

def OwnerManage(request):
    return render(request, 'sensor_owner_manage.html', {})

class ShowSensorsView(View):
    template_name='sensor_owner_home.html'

    def get(self,request):
        available_sensors = SensorDetails.objects.all()
        return render(request, 'sensor_owner_home.html', {'available_sensors':available_sensors})


class AddSensorView(View):
    form_class = AddSensorForm
    template_name = 'sensor_owner_manage.html'

    # Display a blank form
    def get(self, request):
        form = self.form_class(None)
        available_sensors = SensorDetails.objects.all()
        return render(request, self.template_name, {'form': form,'available_sensors':available_sensors})

    # Submit form
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            sensor = SensorDetails()

            # cleaned (normalized) data
            sensor.station = form.cleaned_data['station']
            sensor.station_desc = form.cleaned_data['station_desc']
            sensor.sensor_type = form.cleaned_data['sensor_type']
            sensor.latitude = form.cleaned_data['latitude']
            sensor.longitude = form.cleaned_data['longitude']
            sensor.url = form.cleaned_data['url']
            sensor.active=1
            sensor.sensorOwner='cencoos'
            sensor.save()
            available_sensors = SensorDetails.objects.all()
        return render(request, self.template_name, {'form': form,'isSuccess':'yes','available_sensors':available_sensors})
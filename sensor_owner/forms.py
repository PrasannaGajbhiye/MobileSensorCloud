from django import forms
from sensor_owner.models import SensorDetails


class AddSensorForm(forms.ModelForm):
    station = forms.CharField(max_length=400)
    station_desc=forms.CharField(max_length=800)
    sensor_type=forms.CharField(max_length=100)
    latitude = forms.CharField(max_length=10)
    longitude = forms.CharField(max_length=10)
    url = forms.CharField(max_length=800)

    class Meta:
        model = SensorDetails
        fields = ['station', 'station_desc', 'sensor_type', 'latitude','longitude','url']
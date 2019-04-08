from django import forms

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    departure_city = forms.CharField(
        label='Город отправления',
        widget=AjaxInputWidget(url='api/city_ajax', attrs={'class': 'inline right-margin'})
    )
    arrival_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label='Город прибытия'
    )
    data = forms.DateField(
        label='Дата',
        widget=forms.SelectDateWidget()
    )

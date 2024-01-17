# from tokens.tokens import mapbox_token
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

from django.shortcuts import render
from .models import Receivers
from django.forms import ModelForm
from django.views.generic import (
    CreateView,
)

from .extract_data_influxdb import extract
from .extract_data_sql import get_data


# Create your views here.

mapbox_token = 'pk.eyJ1Ijoicm9tYW4tcGF2bG92aWNoIiwiYSI6ImNscmZmNnA2ODA0azYyam9iY2hqZXprcmwifQ.bWWa83TRkdE_LOWxHC0bHw'

def main_page(request):
    px.set_mapbox_access_token(mapbox_token)
    data = get_data()
    fig = px.scatter_mapbox(data, lat="lat", lon="lon", hover_name="name", zoom=1, mapbox_style='satellite')
    layout = {'title': 'Сейсмические станции России'}
    fig.update_layout(title='Сейсмические станции России',
                      width=1500,
                      height=1000,
                      paper_bgcolor="rgba(0,0,0,0)",
                      plot_bgcolor="rgba(0,0,0,0)")
    graph = fig.to_html()
    context = {'graph': graph}

    # return render(request, 'monitor/home.html', context=context)
    return render(request, 'main/main_page.html', context=context)

def sensor_info(request, ind = None):
    df = get_data()
    name = df.iloc[ind]['name']
    trace = extract(name)
    # print(len(trace))
    fig = go.Figure()
    time = np.linspace(0, 1, len(trace))
    fig.add_trace(go.Scatter(x=time, y=trace))
    title = 'Сейсмостанция: ' + str(name)
    fig.update_layout(title=title,
                      width=1200,
                      height=800,
                      paper_bgcolor="rgba(0,0,0,0)",
                      plot_bgcolor="rgba(0,0,0,0)")
    graph = fig.to_html()
    context = {'graph': graph}
    return render(request, 'main/sensor.html', context=context)

class ReceiversForm(ModelForm):
    class Meta:
        model = Receivers
        fields = ['receiver_name']

class CreateSensorView(CreateView):
    model = Receivers
    form_class = ReceiversForm
    template_name = 'main/list_sensor.html'
    success_url = 'main/sensor.html'

    def form_valid(self, form):
        return super().form_valid(form)

def about(request):
    return render(request, 'main/about_page.html')
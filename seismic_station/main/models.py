from django.db import models
from .extract_data_sql import get_data

# Create your models here.

df = get_data()
STATION_CHOICES = tuple((df.iloc[i]['name'],df.iloc[i]['name']) for i in range(len(df)))

class Receivers(models.Model):
    receiver_name = models.CharField(max_length=500, choices = STATION_CHOICES, default = 'Андозеро')

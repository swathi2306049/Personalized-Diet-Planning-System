from django.urls import path
from .views import diet_chart_view

urlpatterns = [
    path('', diet_chart_view, name='diet_chart'),
]

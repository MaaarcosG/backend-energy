from django.urls import path
from .views import DataView

urlpatterns = [
    path('api/data/', DataView.as_view(), name='data'),
]

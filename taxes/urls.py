from django.urls import path
from .views import index, taxrate, taxCalc



urlpatterns = [

    path('', index),
    path('taxrate', taxrate),
    path('<int:num>', taxCalc)

]

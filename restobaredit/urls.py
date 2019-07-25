from django.urls import path
from restobaredit import views


urlpatterns = [
    path('restobar',views.Home,name='Home'),
]
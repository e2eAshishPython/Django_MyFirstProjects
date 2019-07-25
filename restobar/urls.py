from django.urls import path
from restobar import views
from django.contrib.auth import views as auth_View
from .views import ViewReservations ,CreateReservation



urlpatterns = [
    path('',views.Home,name='Home'),
    path('appreg',views.Reservations,name='Restobar'),
    #path('Login',auth_View.LoginView.as_view(template_name='login.html'),name='Login'),
    path('Login',views.Login,name='Login'),
    path('logout',views.logout,name='logout'),
    path('reservations',ViewReservations.as_view(),name='viewReservations'),
    path('reservations/new',CreateReservation.as_view(),name='createreservations'),
    path('createfrom/new',views.ReservationsForm,name='createfrom'),
    path('signup',views.sign,name='signup'),
    
]
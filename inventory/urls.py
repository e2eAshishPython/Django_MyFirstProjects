from django.urls import path
from inventory.views import Home
from django.conf.urls import url
from django.views.generic import ListView,UpdateView,DetailView
from .models import Restaurant,RestaurantReview,Dish
from django.utils import timezone
from .views import RestaurantDetail,RestaurantCreate,DishCreate,review
from .forms import RestaurantForm,DishForm
from django.urls import reverse

urlpatterns = [
    #path('',Home,name='Home'),
    path('restaurants/create',RestaurantCreate.as_view(),name='restaurant_create'),
    path(r'',ListView.as_view(queryset=Restaurant.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
        	context_object_name='latest_restaurant_list',
        	template_name='inventory/restaurant_list.html'),
        name='restaurant_list'),
    path('restaurants/<int:pk>',
        RestaurantDetail.as_view(),
        name='restaurant_detail'),
    path('restaurants/<int:pk>/edit',
        UpdateView.as_view(
        	model = Restaurant,
        	template_name = 'inventory/form.html',
        	form_class = RestaurantForm),
        name='restaurant_edit'),
    path('restaurants/<int:pk>/dishes/create',
    	DishCreate.as_view(),
        name='dish_create'),

    path('restaurants/<int:restaurant_id>/dishes/<int:pk>/edit',
    	UpdateView.as_view(
    		model = Dish,
    		template_name = 'inventory/form.html',
    		form_class = DishForm),
    	name='dish_edit'),
    path('restaurants/<int:restaurant_id>/dishes/<int:pk>',
        DetailView.as_view(
        	model=Dish,
        	template_name='inventory/dish_detail.html'),
        name='dish_detail'),
    path('restaurants/<int:pk>/reviews/create',
    	review,
    	name='review_create'),
]
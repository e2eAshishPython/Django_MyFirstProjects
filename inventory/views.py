from django.shortcuts import render,reverse
from django.views.generic import DetailView,CreateView,UpdateView
from .models import Restaurant,RestaurantReview,Dish
from .forms import RestaurantForm,DishForm
from django.shortcuts import get_object_or_404

# Create your views here.


def Home(request):
    return render(request,'inventory/home.html')

class RestaurantDetail(DetailView):
  model = Restaurant
  template_name = 'inventory/restaurant_detail.html'

  def get_context_data(self, **kwargs):
    context = super(RestaurantDetail, self).get_context_data(**kwargs)
    context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
    return context

class RestaurantCreate(CreateView):
  model = Restaurant
  template_name = 'inventory/form.html'
  form_class = RestaurantForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(RestaurantCreate, self).form_valid(form)


class DishCreate(CreateView):
  model = Dish
  template_name = 'inventory/form.html'
  form_class = DishForm
  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
    return super(DishCreate, self).form_valid(form)

def review(request, pk):
  restaurant = get_object_or_404(Restaurant, pk=pk)
  review = RestaurantReview(
      rating=request.POST['rating'],
      comment=request.POST['comment'],
      user=request.user,
      restaurant=restaurant)
  review.save()
  return HttpResponseRedirect(reverse('restaurant_detail', args=(restaurant.id,)))
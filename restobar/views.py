from django.shortcuts import render,redirect
from .models import Team,Menu,menu_item,Reservations as Reservations,Food_Type,Occasion
from django.contrib import messages
from datetime import date
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView, ListView, CreateView
from django.contrib.auth.models import User , auth
from .forms import Reservationsform as rs_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
 
# Create your views here.



def Home(request):

	t = Team.objects.all()
	m = Menu.objects.all()
	mi = menu_item.objects.all()
	food = Food_Type.objects.all()
	Occ = Occasion.objects.all()

	if request.method == 'POST':
		name = request.POST.get('form_name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		no_of_persons = request.POST.get('no_of_persons')
		date_picker = request.POST.get('date-picker')
		
		pickdate = date(year=int(date_picker.split('.')[2]),month=int(date_picker.split('.')[1]),day=int(date_picker.split('.')[0]))
		time_picker = request.POST.get('time-picker')
		preferred_food = get_object_or_404(Food_Type, pk=request.POST.get('preferred_food'))
		
		occasion = get_object_or_404(Occasion, pk=request.POST.get('occasion')) 
		Reserved = Reservations(name=name,email=email,ContectNo=phone,No_Of_person=no_of_persons,Date=pickdate,Time=time_picker,preferred_food=preferred_food,Occasion=occasion)
		Reserved.save()
		

		

	
	return render(request,'index.html', {'Teams':t,'Menu':m,'menu_items':mi,'food':food,'Occasion':Occ})


# def Reservations(request):
# 	form = r()
# 	print('Ashis')
# 	return render(request,'addNewname.html',{'forms':form})


def logout(request):
	auth.logout(request)
	return redirect('/')


def Login(request):
	username=''
	password =''
	if request.method == 'POST':
		username = request.POST['email']
		password = request.POST['password']
		User = auth.authenticate(username =username, password= password )
		
		if User is not None:
			auth.login(request,User)
			
			return redirect('/')
		else:
			messages.info(request,'Invalied Credinstion')
			return redirect('/Login')
	
	else:
		return render(request,'login.html')




class ViewReservations(ListView):
	
	model = Reservations
	template_name = 'reservationlist.html'
	context_object_name = 'Reservetion'
	ordering = ['-id']


	
class CreateReservation(CreateView):
	model = Reservations
	template_name = 'Createreservetions.html'
	
	form_class = rs_form
	

def ReservationsForm(request):
	form = rs_form()
	return render(request, 'CreateForm.html',{'form':form})


def sign(request):
	form = UserCreationForm()
	return render(request,'signup.html',{'form':form})




	

	
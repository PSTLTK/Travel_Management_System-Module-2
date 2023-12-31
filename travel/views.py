from django.shortcuts import render,redirect,HttpResponse
from travel.models import DestinationModel,ContinentModel,RegisterationModel,FeedbackModel,BookingModel
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required,permission_required
from travel.forms import SignUpForm,UserCreationForm,PasswordChangingForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from datetime import date
import random
import string


# Create your views here.

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,"Account was created for " + username)
            return redirect('login')
    return render(request,'signup.html',{'form':form})
 
def login_view(request):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if user.username == "admin":
                return redirect('admin_home')
            else:
                return redirect('blog')
        else:
            messages.error(request,"Invalid username or password")
            return render(request,'login.html')

@permission_required('travel.view_feedbackmodel', login_url='login')
def admin_view_feedback(request):
    detail = RegisterationModel.objects.all()
    feedback = FeedbackModel.objects.all()
    return render(request,"admin_view_feedback.html",{"detail":detail,"feedback":feedback})

def generate_random_code(length=6):
    characters= string.ascii_uppercase + string.digits
    random_code= ''.join(random.choice(characters) for _ in range(length))
    return random_code

@permission_required('travel.view_bookingmodel', login_url='login')
def admin_view_booking(request,user_id):
    user = User.objects.get(id= user_id)
    booking = BookingModel.objects.all().order_by('b_status','b_date')
    return render(request,"admin_view_booking.html",{"myuser":user,"booking":booking})

@login_required(login_url='login')
def booking(request,cus_id):
    if request.method == "GET":
        today_date= date.today().strftime("%Y-%m-%d")
        trip = DestinationModel.objects.get(id = cus_id)
        return render(request,"booking.html",{"trip":trip,"today_date":today_date})
    if request.method == "POST":
        trip = DestinationModel.objects.get(id = cus_id)
        duration_day = int(request.POST.get('duration_day'))
        duration_type = int(request.POST.get('duration_type'))
        duration_total = duration_day * duration_type
        duration = f"{duration_total} day(s) and {duration_total-1} night(s)"

        b_name = request.POST.get('b_name')
        b_email = request.POST.get('b_email')
        b_phone = request.POST.get('b_phone')
        b_date = request.POST.get('b_date')
        total_cost = request.POST.get('total_cost')

        if b_email == request.user.email:
            booking = BookingModel.objects.create(
                b_code = generate_random_code(),
                b_name = b_name,
                b_email = b_email,
                b_phone = b_phone,
                b_date = b_date,
                duration = duration,
                b_trip = trip.place,
                total_cost = total_cost,
                travel_id = cus_id,
                user_id = request.user.id,
            )
            booking.save()
            return redirect(f'/customer/booking_success/{cus_id}/{booking.id}/')
        else:
            messages.error(request,"Sorry! That is not your email. Please fill your email again correctly.")
            return redirect(f'/customer/booking/{cus_id}/')

@login_required(login_url='login')
def mybooking(request,user_id):
    booking = BookingModel.objects.filter(user_id = user_id).order_by('-booked_at')
    user = User.objects.get(id = user_id)
    return render(request,'mybooking.html',{"booking":booking,"myuser":user})

@login_required(login_url='login')
def booking_cancel(request,user_id,b_id):
    if request.method == "POST":
        booking = BookingModel.objects.filter(id = b_id)
        booking.delete()
        return redirect(f'/customer/mybooking/{user_id}/')

@login_required(login_url='login')  
def booking_success(request,cus_id,b_id):  
    booking = BookingModel.objects.get(id = b_id)
    trip = DestinationModel.objects.get(id = cus_id)
    return render(request,'booking_success.html',{'booking':booking,'trip':trip})

@permission_required('travel.view_bookingmodel', login_url='login')
def admin_booking_status_confirm(request,user_id,b_id):
    if request.method == "POST":
        booking = BookingModel.objects.get(id = b_id)
        booking.b_status = True
        booking.save()
        return redirect(f'/admin_view_booking/{user_id}/')

@permission_required('travel.view_bookingmodel', login_url='login')
def admin_home(request):
    trip = DestinationModel.objects.all()
    user = User.objects.all()
    booking = BookingModel.objects.all()
    feedback = FeedbackModel.objects.all()
    return render(request,'admin_home.html',{"trip":trip,"myuser":user,"booking":booking,"feedback":feedback})

@login_required(login_url='login')
def contact(request,user_id):
    if request.method == "GET":
        try:
            detail = RegisterationModel.objects.get(user_id = user_id)
        except Exception:
            detail = None
        return render(request,'contact.html',{"detail":detail})
    if request.method == "POST":
        feedback = FeedbackModel.objects.create(
            message = request.POST.get('message'),
            user_id = request.user.id,
            )
        feedback.save()
        return redirect("feedback")

@login_required(login_url='login')
def asia(request):
    continent = ContinentModel.objects.all()
    trip = DestinationModel.objects.filter(continent_id = 1)
    return render(request,'asia.html',{"trip":trip,"continent":continent})

@login_required(login_url='login')
def africa(request):
    continent = ContinentModel.objects.all()
    trip = DestinationModel.objects.filter(continent_id = 2)
    return render(request,'africa.html',{"trip":trip,"continent":continent})

@login_required(login_url='login')
def europe(request):
    continent = ContinentModel.objects.all()
    trip = DestinationModel.objects.filter(continent_id = 3)
    return render(request,'europe.html',{"trip":trip,"continent":continent})

@login_required(login_url='login')
def northamerica(request):
    continent = ContinentModel.objects.all()
    trip = DestinationModel.objects.filter(continent_id = 4)
    return render(request,'northamerica.html',{"trip":trip,"continent":continent})

@login_required(login_url='login')
def southamerica(request):
    continent = ContinentModel.objects.all()
    trip = DestinationModel.objects.filter(continent_id = 5)
    return render(request,'southamerica.html',{"trip":trip,"continent":continent})

@login_required(login_url='login')
def antarctica(request):
    continent = ContinentModel.objects.all()
    trip = DestinationModel.objects.filter(continent_id = 6)
    return render(request,'antarctica.html',{"trip":trip,"continent":continent})

@login_required(login_url='login')
def australia(request):
    continent = ContinentModel.objects.all()
    trip = DestinationModel.objects.filter(continent_id = 7)
    return render(request,'australia.html',{"trip":trip,"continent":continent})

@login_required(login_url='login')
def feedback(request):
    feedback = FeedbackModel.objects.all()
    return render(request,"feedback.html",{"feedback":feedback})
  
def search_by(request):
    search = request.GET.get('search')
    if search:
        try:
            trip = DestinationModel.objects.filter(
                Q(place__icontains = search) |
                Q(country__icontains = search)
            )
        except Exception:
            trip  = None
        return render(request,'view_destination.html',{"trip":trip})
    else:
        trip = DestinationModel.objects.all().order_by('-time')
        return render(request,'view_destination.html',{"trip":trip})

def home(request):
    continent = ContinentModel.objects.all()
    return render(request,'blog.html',{"continent":continent})

def custom_404_view(request):
    return render(request,'404.html')

@login_required(login_url='login')
def view_destination(request):
    continent = ContinentModel.objects.all()
    trip = DestinationModel.objects.all().order_by('-time')
    return render(request,'view_destination.html',{"trip":trip,"continent":continent})

@permission_required('travel.view_destinationmodel', login_url='login')
def admin_view_destination(request):
    trip = DestinationModel.objects.all()
    return render(request,"admin_view_destination.html",{"trip":trip})

@permission_required('travel.add_destinationmodel', login_url='login')
def admin_add_destination(request):
    if request.method == "GET":
        continent = ContinentModel.objects.all()
        return render(request,'admin_add_destination.html',{"continent":continent})
    if request.method == "POST":
        trip = DestinationModel.objects.create(
            id = request.POST.get('id'),
            place = request.POST.get('place'),
            country = request.POST.get('country'),
            flight_price = request.POST.get('flight_price'),
            continent_id = request.POST.get('continent'),
            main_image = request.FILES.get('main_image'),
            adult_per_day = request.POST.get('adult'),
            child_per_day = request.POST.get('child'),
            image_a = request.FILES.get('image_a'),
            image_b = request.FILES.get('image_b'),
            image_c = request.FILES.get('image_c'),
            description = request.POST.get('description'),
            time = datetime.now(),
        )
        trip.save()
        # messages.success(request,)
        return redirect('admin_view_destination')

@login_required(login_url='login')
def detail_destination(request,cus_id):
    continent = ContinentModel.objects.all()
    trip = DestinationModel.objects.get(id = cus_id)
    return render(request,'detail_destination.html',{"trip":trip,"continent":continent})

@permission_required('travel.change_destinationmodel', login_url='login')
def admin_edit_destination(request,cus_id):
    if request.method == "GET":
        continent = ContinentModel.objects.all()
        trip = DestinationModel.objects.get(id=cus_id)
        return render(request,'admin_edit_destination.html',{"trip":trip,"continent":continent})
    if request.method == "POST":
        continent = ContinentModel.objects.all()
        trip = DestinationModel.objects.get(id=cus_id)
        trip.place = request.POST.get('place')
        trip.country = request.POST.get('country')
        trip.adult_per_day = request.POST.get('adult')
        trip.child_per_day = request.POST.get('child')
        trip.flight_price = request.POST.get('flight_price')
        trip.continent_id = request.POST.get('continent')
        if request.FILES.get('main_image'):
            trip.main_image.delete()
            trip.main_image = request.FILES.get('main_image')
        if request.FILES.get('image_a'):
            trip.image_a.delete()
            trip.image_a = request.FILES.get('image_a')
        if request.FILES.get('image_b'):
            trip.image_b.delete()
            trip.image_b = request.FILES.get('image_b')
        if request.FILES.get('image_c'):
            trip.image_c.delete()
            trip.image_c = request.FILES.get('image_c')
        trip.description = request.POST.get('description')
        trip.save()
        # messages.success(request,)
        return redirect('admin_view_destination')
    
@permission_required('travel.delete_destinationmodel', login_url='login')
def admin_delete_destination(request,cus_id):
    trip = DestinationModel.objects.get(id=cus_id)
    trip.main_image.delete()
    trip.image_a.delete()
    trip.image_b.delete()
    trip.image_c.delete()
    trip.delete()
    # messages.error(request,)
    return redirect('admin_view_destination')

def logout_view(request):
    logout(request)
    return redirect('blog')

@permission_required('travel.view_registerationmodel', login_url='login')
def admin_view_user(request):
    try:
        detail = RegisterationModel.objects.all()
    except Exception:
        detail = None
    user = User.objects.all()
    return render(request,'admin_view_user.html',{'detail':detail,'myuser':user})

@permission_required('travel.view_destinationmodel', login_url='login')
def admin_view_profile(request,user_id):
    try:
        detail = RegisterationModel.objects.get(user_id = user_id)
    except Exception:
        detail = None
    return render(request,'view_profile.html',{'detail':detail})

@permission_required('travel.change_destinationmodel', login_url='login')
def admin_edit_profile(request,user_id):
    if request.method == "GET":
        try:
            detail = RegisterationModel.objects.get(user_id = user_id)
        except Exception:
            detail = None
        return render(request,'edit_profile.html',{'detail':detail})
    if request.method == "POST":
        try:
            detail = RegisterationModel.objects.get(user_id = user_id)
            detail.phone = request.POST.get('phone')
            if request.FILES.get('profile'):
                detail.profile.delete()
                detail.profile = request.FILES.get('profile')
            detail.address = request.POST.get('address')
            detail.save()
        except Exception:
            detail = RegisterationModel.objects.create(
                phone = request.POST.get('phone'),
                address = request.POST.get('address'),
                profile = request.FILES.get('profile'),
                user_id = request.user.id,
            )
        user = User.objects.get(id = user_id)
        user.username=request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect(f'/admin_view_profile/{user_id}/')

@login_required(login_url='login')
def view_profile(request,user_id):
    try:
        detail = RegisterationModel.objects.get(user_id = user_id)
    except Exception:
        detail = None
    return render(request,'view_profile.html',{'detail':detail})

@login_required(login_url='login')
def edit_profile(request,user_id):
    if request.method == "GET":
        try:
            detail = RegisterationModel.objects.get(user_id = user_id)
        except Exception:
            detail = None
        return render(request,'edit_profile.html',{'detail':detail})
    if request.method == "POST":
        try:
            detail = RegisterationModel.objects.get(user_id = user_id)
            detail.phone = request.POST.get('phone')
            if request.FILES.get('profile'):
                detail.profile.delete()
                detail.profile = request.FILES.get('profile')
            detail.address = request.POST.get('address')
            detail.save()
        except Exception:
            detail = RegisterationModel.objects.create(
                phone = request.POST.get('phone'),
                address = request.POST.get('address'),
                profile = request.FILES.get('profile'),
                user_id = request.user.id,
            )
        user = User.objects.get(id = user_id)
        user.username=request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect(f'/customer/view_profile/{user_id}/')

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

@login_required(login_url='login')
def password_success(request):
    return render(request,"password_success.html")
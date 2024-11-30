from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Crops,Requirements,Users,Services
from django.db import IntegrityError
from django.contrib import messages
from .models import ContactMessage
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from .weather_service import get_weather



# Create your views here.
def home(request):
    flag =1
    return render(request,'home.html',{'flag':flag})
def first(request):
    return render(request,'home.html')

# def login(request):
#     return render(request,'login.html')

def login(request):
    # Check if the user is already in the session
    if 'username' in request.session:
        return redirect('first')  # If user is in session, go directly to home page
    
    # If the user is not in the session, show the login page
    return render(request, 'login.html')


def service(request):
    return render(request,'Service.html')

def contactus(request):
    return render(request,'contactus.html')

# def checkUser(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             user = Users.objects.get(username=username,password=password)
#             return render(request,'first.html')
#         except Users.DoesNotExist:
#             user = False
#             return render(request,'login.html',{'user':user})


def checkUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Authenticate the user (you can also use your custom user model)
            user = Users.objects.get(username=username, password=password)
            
            if user is not None:
                # request.session['user_id'] = user.id 
                request.session['username'] = user.username  # Store other user info if necessary
                return render(request, 'first.html')  # Redirect after login
            else:
                user = False
                return render(request, 'login.html', {'user': user})
        except Users.DoesNotExist:
            return render(request, 'login.html', {'user': False})


def signup(request):
    return render(request,'signup.html')

# def signupUser(request):
    
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         username = request.POST.get('username')
#         mobile_no = request.POST.get('mob')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
        
#         if len(mobile_no) != 10:
#             mobError = False
#             return render(request,'signup.html',{'mob':mobError})
#         if password != confirm_password:
#             passError = False
#             return render(request,'signup.html',{'pass':passError})
#         try:
#             user = Users(
#                 name = name,
#                 username=username,
#                 mobile_no=mobile_no,
#                 password=password,
#             )
#             user.save()

#             return redirect('login')
#         except IntegrityError:
#             return HttpResponse("Integrity")
#         except Exception as e:
#             return HttpResponse('Exception')

#     return render(request,'signup.html')

def signupUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        mobile_no = request.POST.get('mob')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validate inputs
        if not all([name, username, mobile_no, password, confirm_password]):
            return render(request, 'signup.html', {'error': 'All fields are required.'})
        
        if not mobile_no.isdigit() or len(mobile_no) != 10:
            return render(request, 'signup.html', {'error': 'Enter a valid 10-digit mobile number.'})
        
        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})
        
        try:
            # Hash the password before saving
            hashed_password = make_password(password)
            
            user = Users(
                name=name,
                username=username,
                mobile_no=mobile_no,
                password=hashed_password,
            )
            user.save()
            return redirect('login')
        
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'Username or mobile number already exists.'})
        
        except Exception as e:
            return render(request, 'signup.html', {'error': f'An error occurred: {str(e)}'})
    
    return render(request, 'signup.html')


def crops_list(request):
    crops = Crops.objects.all()
    return render(request,'crops.html',{'crops':crops})

def get_crop_details(request,name):
    crop = get_object_or_404(Crops,name=name)
    
    try:
        requirements = get_object_or_404(Requirements,crop=crop)
    except Requirements.DoesNotExist:
        requirements = None
    if requirements == None:
        message = False
        return render(request,'crop_details.html',{'found':message})
    else:
        return render(request,'crop_details.html',{'crop':crop,'req':requirements})



def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Validation
        if name and email and message:
            # Save the message to the database
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been sent Successfully!')
            return redirect('contact')  # Change this to the route you'd like to redirect to
        else:
            messages.error(request, 'Please fill out all fields.')
    
    return render(request, 'contactus.html')

def profile(request):
    return render(request,'profile.html')

# def logout(request):
#     auth_logout(request)
#     return redirect('login')

def logout(request):
    
    # if 'user_id' in request.session:
    #     del request.session['user_id']
    if 'username' in request.session:
        del request.session['username']
    auth_logout(request)  
    return redirect('login')

def farm_management(request,name):
    service =get_object_or_404(Services,name=name)
    return render(request,'service_details.html',{'services':service})

# def password_reset_confirm_view(request):
#     if request.method == "POST":
#         new_password = request.POST['new_password']
#         confirm_password = request.POST['confirm_password']
#         if new_password == confirm_password:
#             user = request.user  # Assuming the user is already authenticated or retrieved
#             user.set_password(new_password)
#             user.save(update_fields=['password'])  # Only update the password field
#             login(request, user)
#             return redirect('login')
#         else:
#             error_message = "Passwords do not match."
#             return render(request, 'password_reset_confirm.html', {
#                 'error_message': error_message,
#             })


# def password_reset_confirm_view(request):
#     if request.method == "POST":
#         mobile_number = request.POST['mobile_number']
#         new_password = request.POST['new_password']
#         confirm_password = request.POST['confirm_password']
#         # user = request.user
#         user = Users.objects.get(mobile_no=mobile_number)

#         if user.mobile_no == mobile_number:
#             if new_password == confirm_password:
#                 user.password(new_password)
#                 user.save(update_fields=['password'])  
#                 login(request, user)
#                 return redirect('password_reset_complete')
#             else:
#                 error_message = "Passwords do not match."
#         else:
#             error_message = "Mobile number does not match our records."

#         return render(request, 'password_reset_confirm.html', {
#             'error_message': error_message,
#         })

#     return render(request, 'password_reset_confirm.html')


def password_reset_confirm_view(request):
    if request.method == "POST":
        mobile_number = request.POST['mobile_number']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        try:
            # Fetch the user by mobile number
            user = Users.objects.get(mobile_no=mobile_number)

            if new_password == confirm_password:
                # Hash the new password before saving it
                user.password = new_password
                user.save(update_fields=['password'])  # Only update the password field
                # You may need to log the user in manually if applicable
                return redirect('login')
            else:
                error_message = "Passwords do not match."
        except Users.DoesNotExist:
            error_message = "Mobile number does not match our records."

        return render(request, 'password_reset_confirm.html', {
            'error_message': error_message,
        })

    return render(request, 'password_reset_confirm.html')


def password_reset(request):
    return render(request,'password_reset_confirm.html')

    

def weather_view(request):
    city = request.GET.get('city', 'Surat')
    crop = request.GET.get('crop', 'rice')  # Get the selected crop from the form

    # Fetch weather data
    weather_data = get_weather(city)

    # Evaluate weather suitability based on the selected crop
    suitability_message = ""
    if 'error' not in weather_data:
        if crop == 'rice':
            suitability_message = is_weather_suitable_for_rice(weather_data)
        elif crop == 'wheat':
            suitability_message = is_weather_suitable_for_wheat(weather_data)
        elif crop == 'corn':
            suitability_message = is_weather_suitable_for_corn(weather_data)
        elif crop == 'potato':
            suitability_message = is_weather_suitable_for_potato(weather_data)
        else:
            suitability_message = "Crop not supported."

    return render(request, 'weather.html', {
        'weather': weather_data,
        'city': city,
        'suitability': suitability_message,
        'crop': crop
    })


def is_weather_suitable_for_rice(weather):
    if (20 <= weather['temperature'] <= 35) and (weather['humidity'] >= 60) and (weather['rain'] >= 0.1) and (weather['wind_speed'] < 10):
        return "The weather is suitable for growing rice."
    else:
        return "The weather conditions are not ideal for growing rice."

def is_weather_suitable_for_wheat(weather):
    if (10 <= weather['temperature'] <= 25) and (weather['humidity'] >= 50) and (weather['rain'] < 5) and (weather['wind_speed'] < 15):
        return "The weather is suitable for growing wheat."
    else:
        return "The weather conditions are not ideal for growing wheat."

def is_weather_suitable_for_corn(weather):
    # Adjust temperature range and relax rain requirements
    if (18 <= weather['temperature'] <= 35) and (weather['humidity'] >= 50) and (weather['wind_speed'] < 20):
        return "The weather is suitable for growing corn, but irrigation might be needed due to lack of rain."
    else:
        return "The weather conditions are not ideal for growing corn."

def is_weather_suitable_for_potato(weather):
    if (15 <= weather['temperature'] <= 25) and (weather['humidity'] >= 60) and (weather['rain'] >= 1) and (weather['wind_speed'] < 15):
        return "The weather is suitable for growing potatoes."
    else:
        return "The weather conditions are not ideal for growing potatoes."

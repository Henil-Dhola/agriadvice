from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from agriapp import views
urlpatterns=[
    path('',views.login,name='login'),
    path('home/',views.home,name='home'),
     path('first/', views.first, name='first'),
    path('checkUser/',views.checkUser,name='checkUser'),
    path('signup/',views.signup,name='signup'),
    path('signupUser/',views.signupUser,name='signupUser'),
    path('crops_list/',views.crops_list,name='crops_list'),
    path('crop-detail/<str:name>/',views.get_crop_details,name='get_crop_details'),
    path('service/',views.service,name='service'),
    path('contactus/',views.contactus,name='contactus'),
    path('contact/', views.contact_view, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('farm_management/<str:name>/',views.farm_management,name='farm_management'),
    path('password_reset/',views.password_reset,name='password_reset'),
    path('reset/', views.password_reset_confirm_view, name='password_reset_confirm'),
    path('weather/', views.weather_view, name='weather'),

    #path('contact/',views.contact,name='contact'),
    #path('servives/',views.services,name='services'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

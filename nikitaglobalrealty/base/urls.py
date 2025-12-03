from django.urls import path
from . import views




urlpatterns = [
    # path('', views.home, name='index'),

     path('', views.home_view, name='index'),
  
    # auth
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 

    # contact
    path('contact/submit/', views.contact_form_view, name='contact_submit'),
    path('appointment/submit/', views.appointment_form_view, name='appointment_submit'),  # NEW
     path('contact/submitting/', views.contact_inquiry_submit, name='contact_inquiry'),

    # pages
    path('about/', views.about_view, name='about' ),
    path('buywithus/', views.buywithus_view, name='buywithus' ),
    path('forsale/', views.forsale_view, name='forsale' ),
    path('homebuying/', views.home_buy_view, name='home_buy' ),
    path('homesell/', views.home_sell_view, name='homesell' ),
    path('nikita_home/', views.nikita_homes_view, name='nikita_home' ),
    path('rental/', views.rental_view, name='rental' ),
    path('terms/', views.terms_view, name='terms' ),
 
            
    path("market/", views.market_view, name="market"),

    # urls.py
    path('api/chat/', views.chat_assistant, name='chat_assistant'),


     path('properties/', views.properties_list, name='properties_list'),
    path('properties/inquiry/submit/', views.submit_property_inquiry, name='submit_property_inquiry'),

]

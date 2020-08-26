from django.urls import path,include
from Registration import views

urlpatterns=[
    path('Reciept/',views.Reciept),
    path('',views.login),
    path('login/',views.login),
    path('logout/',views.logout,name='logout'),
    path('test/',views.test),

    path('dashboard/',views.dashboard),
    path('bookings/',views.bookings),
    path('agent/',views.agent),
    path('guest/',views.guest),
    path('settings/',views.usersettings),
    path('managerooms/',views.managerooms),


    path('admindashboard/',views.admindashboard),
    path('changepassword/',views.changepassword),
    path('bookingsadmin/',views.bookingsadmin),
    path('rooms/',views.rooms),
    path('more/',views.more),
    path('agentadmin/', views.agentadmin),
    path('guestadmin/',views.guestadmin),
    path('user/', views.settings),
    path('Recieptadmin/',views.Recieptadmin),
    path('manageroomsadmin/',views.manageroomsadmin),

    path('agentview/',views.agentview),
    path('agentbooking/',views.agentbooking),
    path('Recieptagent/',views.Recieptagent),
    path('allbookings/',views.allbookings),

]

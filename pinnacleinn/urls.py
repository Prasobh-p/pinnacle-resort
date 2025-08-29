from django.urls import path
from pinnacleinn import views


urlpatterns=[

    path('homepage/',views.Homepage,name="Homepage"),
    path('aboutpage/',views.Aboutpage,name="Aboutpage"),
    path('Roompage/',views.Roompage,name="Roompage"),
    path('Filteredroom/<Adata>/',views.Filteredroom,name="Filteredroom"),
    path('Diningpage/', views.Diningpage, name="Diningpage"),
    path('Singroompage/<int:r_id>/',views.Singleroompage,name="Singleroompage"),
    path('Contactpage/',views.contactpage,name="Contactpage"),
    path('Bookingpage/',views.Bookingpage,name="Bookingpage"),
    path('Registerpage/',views.Registerpage,name="Registerpage"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('loginn/',views.loginn,name="loginn"),
    path('logout/',views.logout,name="logout"),
    path('Bookingdate/<int:id>/', views.Bookingdate, name='Bookingdate'),
    path('paymentpage/',views.paymentpage,name='paymentpage'),
    path('orderdetils/',views.orderdetils,name='orderdetils'),
    path('orderingfinal/',views.orderingfinal,name='orderingfinal'),








]
from django.urls import path
from backend import views


urlpatterns = [
    path('index/', views.indexpage, name="indexpage"),
    path('add_accommodation/', views.add_accommodationpage, name="add_accommodationpage"),
    path('save_accommodation/', views.save_accommodationpage, name="save_accommodationpage"),
    path('display/',views.displaypage, name="displaypage"),
    path('edit/<int:accid>/',views.editdata,name="editdata"),
    path('update/<int:accid>/',views.updatedata,name="updatedata"),
    path('delete/<int:accid>/',views.deletedata, name="deletedata"),
    path('add_rooms/',views.add_roomspage,name="add_roomspage"),
    path('save_roompage/',views.save_roompage,name="save_roompage"),
    path('display_room/',views.displayroompage,name="displayroompage"),
    path('edit_roompage/<int:Rid>/',views.edit_roompage,name="edit_roompage"),
    path('update_room/<int:Rid>/', views.update_roompage, name='update_roompage'),
    path('deletepage/<int:Rid>/',views.delete_roompage,name="delete_roompage"),
    path('login/',views.loginpage,name="loginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('add_food/',views.add_foodtype,name="add_foodtype"),
    path('save_food/',views.save_food,name="save_food"),
    path('dispaly_food',views.displayfoodpage,name="displayfoodpage"),
    path('editfood/<int:fooid>/',views.editfooddata,name="editfooddata"),
    path('updatefood/<int:fooid>/',views.updatefooddata,name="updatefooddata"),
    path('deletefood/<int:fooid>/',views.deletefooddata,name="deletefooddata"),
    path('add_fooditeams/',views.addfooditeams,name="addfooditeams"),
    path('savefood_iteams/',views.save_fooditeams,name="save_fooditeams"),
    path('displayfooditeams/',views.displayfooditeams,name="displayfooditeams"),
    path('Edit_fooditeampage<int:Bid>/',views.edit_foodpage,name="edit_foodpage"),
    path('fooditeam_delete<int:Bid>/',views.delete_foodpage,name="delete_foodpage"),
    path('update_foodpage<int:Bid>/',views.update_foodpage,name="update_foodpage")



]
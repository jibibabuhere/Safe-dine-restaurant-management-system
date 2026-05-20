
from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('', views.login, name="login"),
    path('logoutcode', views.logoutcode, name="logoutcode"),
    path('addreg', views.addreg, name="addreg"),
    path('addlogincode', views.addlogincode, name="addlogincode"),
    path('admin_home', views.admin_home, name="admin_home"),
    path('add_inspetor_details',views.add_inspetor_details, name="add_inspetor_details"),

    path('manage_food_inspector', views.manage_food_inspector, name="manage_food_inspector"),
    path('manage_food_menu', views.manage_food_menu, name="manage_food_menu"),
    path('manage_menu_add_item', views.manage_menu_add_item, name="manage_menu_add_item"),
    path('restaurant_home', views.restaurant_home, name="restaurant_home"),
    path('restaurant_registration', views.restaurant_registration, name="restaurant_registration"),
    path('restaurent_profile', views.restaurent_profile, name="restaurent_profile"),
    path('send_replay/<int:id>', views.send_replay, name="send_replay"),
    path('sreplay', views.sreplay, name="sreplay"),
    path('Verify_restuarent', views.Verify_restuarent, name="Verify_restuarent"),
    path('view_assigned_work', views.view_assigned_work, name="view_assigned_work"),
    path('view_booking_view_more', views.view_booking_view_more, name="view_booking_view_more"),

    path('view_booking', views.view_booking, name="view_booking"),
    path('view_complaints_and_take_action', views.view_complaints_and_take_action, name="view_complaints_and_take_action"),
    path('view_complaints', views.view_complaints, name="view_complaints"),
    path('view_fitness_certificate', views.view_fitness_certificate, name="view_fitness_certificate"),
    path('view_order', views.view_order, name="view_order"),
    path('view_order_and_status/<int:id>', views.view_order_and_status, name="view_order_and_status"),
    path('view_order', views.view_order, name="view_order"),
    path('view_payment', views.view_payment, name="view_payment"),
    path('view_review_rating', views.view_review_rating, name="view_review_rating"),
    path('view_user', views.view_user, name="view_user"),
    path('action', views.action, name="action"),

    path('view_rating_review', views.view_rating_review, name="view_rating_review"),
    path('add_food_inspector', views.add_food_inspector, name="add_food_inspector"),
    path('assign_deliveryboy/<int:id>', views.assign_deliveryboy, name="assign_deliveryboy"),
    path('add_delivery_boy', views.add_delivery_boy, name="add_delivery_boy"),

    path('accept/<int:id>', views.accept ,name="accept"),
    path('reject/<int:id>',views.reject, name="reject"),
    path('edit_food_ispector/<int:id>', views.edit_food_ispector ,name="edit_food_ispector"),
    path('delete_food_ispector/<int:id>',views.delete_food_ispector, name="delete_food_ispector"),
    path('edit_food_inspector_post', views.edit_food_inspector_post, name="edit_food_inspector_post"),
    path('View_accepted_restuarent', views.View_accepted_restuarent, name="View_accepted_restuarent"),
    path('restaurent_profile_edit_post', views.restaurent_profile_edit_post, name="restaurent_profile_edit_post"),
    path('view_restaurent_profile', views.view_restaurent_profile, name="view_restaurent_profile"),
    path('delete_food_item/<int:id>', views.delete_food_item, name="delete_food_item"),
    path('add_food_item', views.add_food_item, name="delete_food_add_food_itemitem"),







]

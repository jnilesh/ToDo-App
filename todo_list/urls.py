from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('delete/<list_id>',views.delete,name='delete'),
    path('cross_off/<list_id>',views.cross_off,name='cross_off'),
    path('uncross/<list_id>',views.uncross,name='uncross'),
    path('edit/<list_id>',views.edit,name='edit'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('list/',views.td_list, name='list'),
	path('register/',views.register_user, name='register'),
	path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('change_password/',views.change_password, name='change_password'),
    path('accounts/login/',views.r_login, name='r_login'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(), 
        name="password_reset_complete"),

# accounts/login/

]

from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('user/<int:id>/', views.profile, name='profile'),
    path('user/<int:id>/regisdriver/', views.regisdriver, name='regisdriver'),
    path('user/<int:id>/editinfo/', views.editinfo, name='editinfo'),
    path('user/<int:id>/changepassword/', views.changepassword, name='changepassword'),

    path('display/<int:id>/', views.display, name='display'),
    path('display/<int:id>/<int:rid>/delete/', views.delete, name='delete'),
    path('display/<int:id>/<int:rid>/', views.curtride, name='curtride'),
    path('display/<int:id>/<int:rid>/complete/', views.complete, name='complete'),
    path('display/<int:id>/findride/driver/', views.findridedriver, name='findridedriver'),
    path('display/<int:id>/<int:rid>/handledrive/', views.handledrive, name='handledrive'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:id>/newride/', views.newride, name='newride'),
    path('<int:id>/newshare/', views.newshare, name='newshare'),
    path('<int:id>/<int:rid>/<int:passenger>/joinshare/', views.joinshare, name='joinshare'),
    path('<int:id>/<int:rid>/deleteshare/', views.deleteshare, name='deleteshare'),
    path('<int:id>/<int:rid>/editshare/', views.editshare, name='editshare'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('review/', views.review, name='review'),
]

from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signUp,name='signUp'),
    path('login/',views.logIn,name='logIn'),
    path('logout/',views.logOut,name='logOut'),
    path('editdata/',views.editProfile,name='editdata'),
    path('postblog/',views.postBlog,name='postblog'),
    path('profile/',views.profile,name='profile'),
    path('editpost/<int:id>',views.editpost,name='editpost')
]
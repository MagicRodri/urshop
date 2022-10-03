from django.urls import path

from .views import (
    login_view,
    logout_view,
    signup_view,
    upload_pp_view,
    edit_profile_view,
    delete_profile_view
)

app_name = 'accounts'
urlpatterns = [
     path('delete_profile',delete_profile_view,name='delete'),
    path('edit_profile',edit_profile_view,name='edit'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('upload_pp/',upload_pp_view,name='upload-pp'),
    path('signup/',signup_view,name='signup')
]
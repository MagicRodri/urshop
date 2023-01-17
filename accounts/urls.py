from django.urls import path

from .views import (
    UploadPpView,
    UserLoginView,
    delete_profile_view,
    edit_profile_view,
    logout_view,
    signup_view,
)

app_name = 'accounts'
urlpatterns = [
     path('delete_profile/',delete_profile_view,name='delete'),
    path('edit_profile/',edit_profile_view,name='edit'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',logout_view,name='logout'),
    path('upload_pp/',UploadPpView.as_view(),name='upload-pp'),
    path('signup/',signup_view,name='signup')
]
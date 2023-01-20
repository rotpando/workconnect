from django.contrib import admin
from django.urls import path
from api.views import UserList, AdverList, RegisterUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users', UserList.as_view(),name="user list"),
    path('api/listadver', AdverList.as_view(),name="adver list"),
    path('api/register', RegisterUser.as_view(),name="registration")
]

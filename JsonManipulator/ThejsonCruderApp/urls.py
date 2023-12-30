from django.urls import path
from . import views

urlpatterns = [
    path('helloWorldFunction/', views.helloWorldFunction, name='helloWorldFunction'),
    path('RetrieveUserData/',views.RetrieveUserData,name='RetrieveUserData'),
    path('CreateUserData/',views.CreateUserData,name='CreateUserData'),
    path('UpdateUserData/',views.UpdateUserData,name='UpdateUserData'),
    path('ApiView/',views.ApiView,name='ApiView'),
    path('RetrieveUserDataUsingSerializers/',views.RetrieveUserDataUsingSerializers,name='RetrieveUserDataUsingSerializers'),
]


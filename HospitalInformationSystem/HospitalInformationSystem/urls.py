from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from myhis.controller.patient_api import patient_router
from rest_auth.api import auth_router

api = NinjaAPI()
api.add_router('patient/' , patient_router)
api.add_router('auth/' , auth_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' , api.urls)
]

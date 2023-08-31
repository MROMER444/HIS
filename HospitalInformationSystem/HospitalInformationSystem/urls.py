from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from myhis.controller.patient_api import patient_router
from rest_auth.api import auth_router
from myhis.controller.appointment_api import appointment_router

api = NinjaAPI(
    title = 'Hospital Information System',
    version = 0.1,
    description = 'A BackEnd to offer an APIs to a HIS application',
    csrf=True
    )


api.add_router('auth/' , auth_router)
api.add_router('patient/' , patient_router)
api.add_router('appointment/' , appointment_router)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' , api.urls),
]

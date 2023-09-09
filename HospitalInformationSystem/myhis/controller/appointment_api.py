import datetime
from ninja import Router
from myhis.models import Appointment
from myhis.schemas.Schemas import AppointmentIn , FourOFOut
from django.http import JsonResponse
from rest_auth.authorization import AuthBearer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()


appointment_router = Router(tags=['appointment'])



@appointment_router.post('/' , response = {404 : FourOFOut} , auth=AuthBearer())
def create_appointment(request , data : AppointmentIn):
    try:
        doctor = get_object_or_404(User , email = request.auth['email'])
        appointment = Appointment.objects.create(
            patient_id = data.patient_id,
            doctor = doctor,
            data = data.date
        )
        appointment_info = {
            "image" : appointment.patient.image.url,
            "name": appointment.patient.name,
            "age": appointment.patient.age,
            "address" : appointment.patient.address,
            "gender": appointment.patient.gender
        }
        return JsonResponse({'appointment_info': appointment_info})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    



@appointment_router.get('/getallapp' , response = {404 : FourOFOut} , auth=AuthBearer())
def get_appointment_details(request):
    try:
        doctor = get_object_or_404(User , email = request.auth['email'])
        appointments = Appointment.objects.filter(
            doctor = doctor,
            date = datetime.date.today()
            
            )
        appointment_details = []
        
        for appointment in appointments:
            details = {
                'image': appointment.patient.image.url,
                'name': appointment.patient.name,
                'age': appointment.patient.age,
                'address': appointment.patient.address,
                'gender': appointment.patient.gender,
            }
            appointment_details.append(details)
        
        return JsonResponse({'appointments': appointment_details})
    except Appointment.DoesNotExist:
        return JsonResponse({'detail': 'There are no appointments'})
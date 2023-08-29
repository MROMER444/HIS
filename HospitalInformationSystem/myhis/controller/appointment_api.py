from ninja import Router
from myhis.models import Appointment
from myhis.schemas.Schemas import AppointmentIn , FourOFOut
from django.http import JsonResponse



appointment_router = Router()



@appointment_router.post('/')
def create_appointment(request , payload : AppointmentIn):
    try:
        data = payload
        appointment = Appointment.objects.create(
            patient_id = data.patient_id,
            doctor_id = data.doctor_id
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
    



@appointment_router.get('/' , response = {404 : FourOFOut})
def get_appointment_details(request):
    try:
        appointments = Appointment.objects.all()
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
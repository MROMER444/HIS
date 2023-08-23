from ninja import Router
from django.http import JsonResponse
from myhis.models import Patient
from myhis.schemas.Schemas import PatientIn , FourOFOut
from typing import List
from rest_auth.authorization import AuthBearer

patient_router = Router()


@patient_router.post('/')
def addA_patient(request , payload : PatientIn):
    try:
         data = payload
         patient = Patient.objects.create(
            name=data.name,
            date_of_birth=data.date_of_birth,
            age=data.age,
            gender=data.gender,
            phone_number=data.phone_number,
            address=data.address,
            image=data.image
        )
         patient_info = {
            "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "gender": patient.gender,
        }
         return JsonResponse({'success': True , 'patient' : patient_info})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status_code=400)
    

@patient_router.get('/' , auth = AuthBearer())
def get_all_patients(request):
    try:
        patients = Patient.objects.all()
        patient_info = [
        {
            "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "gender": patient.gender,
            "phone_number" : patient.phone_number,
            "address" : patient.address,
            "date_of_birth" : patient.date_of_birth,
            "image" : patient.image.url,
        }
        for patient in patients
        ]
        return JsonResponse({'patients' : patient_info})
    except Exception as e:
        return JsonResponse({'error' : str(e)} , status_code=404)
    

@patient_router.get('/{patient_name}/' , response = {404 : FourOFOut})
def get_patient_by_name(request , patient_name : str):
    try:
        patient = Patient.objects.get(name = patient_name)
        patient_info =  {
            "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "gender": patient.gender,
            "phone_number" : patient.phone_number,
            "address" : patient.address,
            "date_of_birth" : patient.date_of_birth,
            "image" : patient.image.url,
                }
        
        return JsonResponse({'patient' : patient_info})
    except Patient.DoesNotExist:
        return 404, {'detail': f'patient with this name {patient_name} does not exist'}
    


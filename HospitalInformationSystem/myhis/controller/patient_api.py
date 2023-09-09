from ninja import Router
from django.http import JsonResponse
from myhis.models import Patient
from myhis.schemas.Schemas import PatientIn , FourOFOut , AppointmentIn
from rest_auth.authorization import AuthBearer

patient_router = Router(tags=['Patient'])


@patient_router.post('/')
def add_patient(request, payload: PatientIn):
    try:
        data = payload
        patient = Patient.objects.create(
            name=data.name,
            age=data.age,
            gender=data.gender,
            phone_number=data.phone_number,
            address=data.address,
            image=data.image
        )
        patient_info = {
            "image" : patient.image.url,
            "name": patient.name,
            "age": patient.age,
            "address" : patient.address,
            "gender": patient.gender,
        }
        return JsonResponse({'patient': patient_info})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status_code=400)


# @patient_router.get('/' , auth = AuthBearer())
@patient_router.get('/')
def get_all_patients(request): 
    try:
        patients = Patient.objects.all()
        patient_info = [
        {
            # "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "gender": patient.gender,
            "phone_number" : patient.phone_number,
            "address" : patient.address,
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
            # "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "gender": patient.gender,
            "phone_number" : patient.phone_number,
            "address" : patient.address,
            "image" : patient.image.url,
                }
        
        return JsonResponse({'patient' : patient_info})
    except Patient.DoesNotExist:
        return JsonResponse({'detail': f'patient with this name {patient_name} does not exist'})
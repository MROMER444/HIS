from ninja import Router
from myhis.models import Queue , Ticket , Patient
from myhis.schemas.Schemas import ticketIn , FourOFOut
from django.http import JsonResponse
from rest_auth.authorization import AuthBearer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


User = get_user_model()


ticket_router = Router(tags=['Ticket'])




def add_patient_to_queue(patient_id):
    patient = Patient.objects.get(id=patient_id)
    queue = Queue.objects.create(patient=patient)
    queue.queue_number = 1
    queue.save()





@ticket_router.post('/' , response = {404 : FourOFOut})
def create_ticket(request , data : ticketIn):
    try:
        ticket = Ticket.objects.create(
            patient_id = data.patient_id,
        )
        add_patient_to_queue(ticket.patient.id)
        ticket_info = {
            "image" : ticket.patient.image.url,
            "name": ticket.patient.name,
            "address" : ticket.patient.address,
            "number" : ticket.patient.phone_number,
            "age": ticket.patient.age,
            "gender": ticket.patient.gender
        }
        return JsonResponse({'ticket_info': ticket_info})
    except Exception as e:
        return JsonResponse({'detail': 'Cant create ticket!'})
    



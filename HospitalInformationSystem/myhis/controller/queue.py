from ninja import Router
from myhis.models import Queue
from myhis.schemas.Schemas import FourOFOut
from django.http import JsonResponse
from rest_auth.authorization import AuthBearer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


User = get_user_model()


queue_router = Router(tags=['Queue'])

@queue_router.get('/' , response = {404 : FourOFOut})
def get_queue_details(request):
    try:
        queue = Queue.objects.all()
        queue_details = []
        
        for queue in queue:
            details = {
                'image': queue.patient.image.url,
                'name': queue.patient.name,
                'age': queue.patient.age,
                'address': queue.patient.address,
                'gender': queue.patient.gender,
            }
            queue_details.append(details)
        
        return JsonResponse({'queue': queue_details})
    except Queue.DoesNotExist:
        return JsonResponse({'detail': 'There are no queues'})

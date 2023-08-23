from django.contrib.auth import get_user_model
from rest_auth.schemas import FourOFOut , AuthOut 
from myhis import status
from ninja import Router
from .schemas import AccountIn
User = get_user_model()
from .authorization import create_token_for_user
auth_router = Router(tags=['auth'])


@auth_router.post('signup' , response = {
201 : AuthOut,
400 : FourOFOut
})

def signup(request , account_in : AccountIn):
    if account_in.password1 != account_in.password2:
        return status.BAD_REQUEST_400 , {'detail' : 'password should look alike'}
    
    try:
        User.objects.get(email = account_in.email)
    except User.DoesNotExist:

        new_user = User.objects.create_user(
            first_name = account_in.first_name,
            last_name = account_in.last_name,
            email = account_in.email,
            password = account_in.password1,
            age = account_in.age,
            address = account_in.address,
            role = account_in.role
        )

        token = create_token_for_user(new_user)

        return status.CREATED_201 , {
            'token' : token,
            'account' : new_user
        }
    
    return status.BAD_REQUEST_400 , {'detail' : 'Email already taken!'}
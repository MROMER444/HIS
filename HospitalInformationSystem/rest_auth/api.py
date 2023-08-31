from django.contrib.auth import get_user_model
from rest_auth.schemas import FourOFOut , AuthOut , SignIn
from myhis import status
from ninja import Router
from .schemas import AccountIn
from .authorization import create_token_for_user


auth_router = Router(tags=['auth'])
User = get_user_model()


@auth_router.post('signup' , response = { 201 : AuthOut , 400 : FourOFOut})
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
            role = account_in.role,
            address = account_in.address,
            phone_number = account_in.phone_number,
            password = account_in.password1,
        )

        token = create_token_for_user(new_user)

        return status.CREATED_201 , {
            'token' : token,
            'account' : new_user
        }
    return status.BAD_REQUEST_400 , {'detail' : 'Email already taken!'}


@auth_router.post('signin' , response={200 : AuthOut,404 : FourOFOut,401 : FourOFOut})
def signin(request , sign_in : SignIn):
    try:
        user = User.objects.get(email  = sign_in.email)
    except User.DoesNotExist:
        user = None

    else:
        if not user.check_password(sign_in.password):
            return status.UNAUTHORIZED_401 , {'detail' : 'User password wrong'}
        else:
            token = create_token_for_user(user)
            
            return status.OK_200 ,  {
                'token' : token,
                'account' : user
                }  
    if not user:
        return status.NOT_FOUND_404, {'detail' : 'User is not registered'}
    
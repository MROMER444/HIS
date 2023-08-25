from django.conf import settings
from django.contrib.auth import get_user_model
from ninja.security import HttpBearer
from jose import jwt , JWTError
from HospitalInformationSystem import settings
User = get_user_model()


#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Imh1bWFtMkB5YWhvby5jb20iLCJyb2xlIjoiZG9jdG9yIn0.VA45qFJ4sW-2uUR8qUx3ezuDW9_8tzHAbnP03zMLSeg

class AuthBearer(HttpBearer):
    def authenticate(self, request, token): 
        try:
            user_email = jwt.decode(token = token , key = settings.SECRET_KEY , algorithms='HS256')
        except JWTError:
            return {'token' : 'UNauthorized'}
        if user_email:
            return {'email' : str(user_email['email'])}



# class Middleware(HttpBearer):
#     def check(self , request , token , next):
#         try:
#             user_email = jwt.decode(token = token , key = settings.SECRET_KEY , algorithms='HS256')
#         except JWTError:
#             return {'token' : 'UNauthorized'}
#         if user_email.role == 'dr':
#             next()



def create_token_for_user(user):
    token = jwt.encode({'email' : str(user.email) , 'role' : str(user.role)} , key = settings.SECRET_KEY , algorithm='HS256')
    return {
        'access' : str(token)
    }


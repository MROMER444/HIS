from ninja import Schema
from pydantic import EmailStr , Field


class AccountIn(Schema):
    first_name : str
    last_name : str
    email : EmailStr
    role : str
    address : str
    phone_number : str
    password1 : str = Field(min_length=2)
    password2 : str = Field(min_length=2)

class FourOFOut(Schema):
    detail: str


class TokenOut(Schema):
    access : str


class AccountOut(Schema):
    first_name : str
    last_name : str
    email : EmailStr
    address : str
    role : str
    phone_number : str



class AuthOut(Schema):
    token : TokenOut
    account : AccountOut


class SignIn(Schema):
    email : EmailStr
    password : str
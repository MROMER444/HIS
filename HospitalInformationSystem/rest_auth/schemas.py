from ninja import Schema
from pydantic import EmailStr , Field

class AccountIn(Schema):
    first_name : str
    last_name : str
    email : EmailStr
    password1 : str = Field(min_length=8)
    password2 : str = Field(min_length=8)
    age : int
    address : str
    role : str

class FourOFOut(Schema):
    detail: str


class TokenOut(Schema):
    access : str


class AccountOut(Schema):
    first_name : str
    last_name : str
    email : EmailStr
    age : int
    address : str
    role : str


class AuthOut(Schema):
    token : TokenOut
    account : AccountOut
from ninja import Schema

class PatientIn(Schema):
    name : str
    date_of_birth : str
    age : int
    gender : str
    phone_number : int
    address : str
    image : str


class FourOFOut(Schema):
    detail: str
from ninja import Schema

class PatientIn(Schema):
    name : str
    age : int
    gender : str
    phone_number : str
    address : str
    image : str


class FourOFOut(Schema):
    detail: str


class AppointmentIn(Schema):
    patient_id : int
    date = str

class ticketIn(Schema):
    patient_id : int
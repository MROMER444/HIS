from django.db import models 




class Patient(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='patient_images/')
    
    def __str__(self):
        return f'{self.name}'


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    specialties = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)



class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_datetime = models.DateTimeField()
    condition = models.CharField(max_length=255)
    is_emergency = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)


class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    condition = models.CharField(max_length=255)
    lab_test = models.CharField(max_length=255)
    diagnoses = models.CharField(max_length=255)
    treatments = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    dosages = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class LabTechnician(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    assigned_tests = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Administrator(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    access_levels = models.CharField(max_length=255)
    created_at = models.DateTimeField


class OtherStaff(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class LabTest(models.Model):
    lab_name = models.CharField(max_length=255)
    test_name = models.CharField(max_length=255)
    time_takes = models.IntegerField()
    technicians_id = models.ForeignKey(LabTechnician, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class LabResults(models.Model):
    test_type = models.CharField(max_length=255)
    test_result = models.CharField(max_length=255)
    order_time = models.DateTimeField()
    is_completed = models.BooleanField()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class TicketsRecords(models.Model):
    ticket_type = models.CharField(max_length=255)
    charges = models.FloatField()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class PharmacyInventory(models.Model):
    drug_details = models.CharField(max_length=255)
    quantity = models.IntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class EquipmentsInventory(models.Model):
    equipment_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class DrugDetails(models.Model):
    generic_name = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Orders(models.Model):
    datetime = models.DateTimeField()
    quantities = models.IntegerField()
    drug_id = models.ForeignKey(DrugDetails, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

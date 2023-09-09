from django.contrib import admin

from myhis.models import *
from rest_auth.models import EmailAccountManager

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(MedicalHistory)
admin.site.register(Prescription)
admin.site.register(LabTechnician)
admin.site.register(Administrator)
admin.site.register(OtherStaff)
admin.site.register(LabTest)
admin.site.register(LabResults)
admin.site.register(TicketsRecords)
admin.site.register(PharmacyInventory)
admin.site.register(EquipmentsInventory)
admin.site.register(DrugDetails)
admin.site.register(Orders)
admin.site.register(Ticket)
admin.site.register(Queue)


from django.contrib import admin
from .models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'Class', 'Standard', 'age', 'Place', 'DOB','Student_id')


# class OfferAdmin(admin.ModelAdmin):
# list_display = ('code', 'discount')


admin.site.register(Student, StudentAdmin)
# admin.site.register(offer, OfferAdmin)

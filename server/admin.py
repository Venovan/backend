from django.contrib import admin
from .models import Council, Student, MessMenu, Event, CultInventory, SportInventory, TechInventory, Complaint, HostelConstitution, OtherImages


admin.site.register([Council, Student, Event, MessMenu, CultInventory, SportInventory, TechInventory, Complaint, HostelConstitution, OtherImages])


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "rollNumber"]
    search_fields = ["rollNumber"]
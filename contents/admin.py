from django.contrib import admin

# Register your models here.
from .models import EducationLevel, ClassLevel, Grade, Subject, ResourceType, Document

admin.site.register(EducationLevel)
admin.site.register(ClassLevel)
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(ResourceType)
admin.site.register(Document)
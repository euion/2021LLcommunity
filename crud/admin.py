from django.contrib import admin

from .models import Crud, Info, Qna

# Register your models here.
admin.site.register(Crud)
admin.site.register(Info)
admin.site.register(Qna)
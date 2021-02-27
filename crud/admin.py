from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Crud)
admin.site.register(CrudComment)

admin.site.register(Info)
admin.site.register(InfoComment)

admin.site.register(Qna)
admin.site.register(QnaComment)
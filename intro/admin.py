from django.contrib import admin
from .models import Comment
from .models import Bloggs

admin.site.register(Comment)
admin.site.register(Bloggs)
# Register your models here.

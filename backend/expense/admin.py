from django.contrib import admin
from .models import Expense, UserDetail

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(Expense)

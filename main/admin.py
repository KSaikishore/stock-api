from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Stock, UserProfile, Transaction


class StockAdmin(admin.ModelAdmin):
    list_display = ('stock_symbol', 'security_name', 'quantity', 'price')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('transactions', 'user')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('Type', 'seller',  'price', 'stock', 'quantity')


admin.site.register(Stock, StockAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Transaction, TransactionAdmin)
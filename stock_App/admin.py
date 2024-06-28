from django.contrib import admin
from .models import StockPrice, MonthlyStockPrice

class MonthlyStockPriceInline(admin.TabularInline):
    model = MonthlyStockPrice
    extra = 1  # Number of empty fields to display

class StockPriceAdmin(admin.ModelAdmin):
    list_display = ('id','company',)
    search_fields = ('company',)
    inlines = [MonthlyStockPriceInline]  # Show MonthlyStockPrice inline

class MonthlyStockPriceAdmin(admin.ModelAdmin):
    list_display = ('id','stock', 'month', 'highest_price', 'lowest_price', 'open_price', 'close_price')
    list_filter = ('month', 'stock')
    search_fields = ('stock__company', 'month')

admin.site.register(StockPrice, StockPriceAdmin)
admin.site.register(MonthlyStockPrice, MonthlyStockPriceAdmin)


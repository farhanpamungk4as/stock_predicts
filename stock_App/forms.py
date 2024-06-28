from django import forms
from .models import MonthlyStockPrice, StockPrice

from datetime import date


class MonthlyStockPriceForm(forms.ModelForm):
    stock = forms.ModelChoiceField(queryset=StockPrice.objects.all(), label="Pilih Perusahaan")

    class Meta:
        model = MonthlyStockPrice
        fields = ['stock', 'month', 'highest_price', 'lowest_price', 'open_price', 'close_price']
        labels = {
            'month': 'Month and Year(masukan data saham rata-rata perbulan,  untuk kolom tanggal isi berapa saja)',  # Label untuk kolom bulan dan tahun
        }
        widgets = {
            'month': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            # Menggunakan SelectDateWidget untuk memilih bulan dan tahun
        }
    

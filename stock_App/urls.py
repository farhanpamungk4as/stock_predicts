from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_monthly_stock_price, name='add_monthly_stock_price'),
    path('company_list/<int:company_id>/', views.company_list, name='company_list'),
    path('predict/<int:company_id>/<int:days_ahead>/', views.predict_view, name='predict_view'),
    path('predict_list/', views.predict_list, name='predict_list')
    # URL untuk harga saham berdasarkan ID perusahaan
    # Tambahkan pola URL lainnya sesuai kebutuhan
]

from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import MonthlyStockPrice, StockPrice
from .forms import MonthlyStockPriceForm
from django.http import JsonResponse

def add_monthly_stock_price(request):
    if request.method == 'POST':
        form = MonthlyStockPriceForm(request.POST)
        if form.is_valid():
            selected_company = form.cleaned_data['stock']
            month = form.cleaned_data['month']
            
            # Periksa apakah data dengan bulan yang sama sudah ada
            if MonthlyStockPrice.objects.filter(stock=selected_company, month=month).exists():
                form.add_error('month', 'Data saham untuk bulan ini sudah ada.')
            else:
                monthly_stock_price = form.save(commit=False)
                monthly_stock_price.stock = selected_company
                monthly_stock_price.save()
                return redirect('company_list', company_id=selected_company.id)
        else:
            print(form.errors)
    else:
        form = MonthlyStockPriceForm()

    return render(request, 'stock_app/stock_prices.html', {'form': form})

def company_list(request, company_id):
    # Ambil perusahaan berdasarkan company_id
    company = get_object_or_404(StockPrice, pk=company_id)
    # Ambil semua harga saham bulanan terkait perusahaan
    monthly_prices = company.Monthly_Prices.all()
    return render(request, 'stock_app/company_list.html', {'company': company, 'monthly_prices': monthly_prices, 'company_id': company_id})

from .ml_utils import predict_future_prices

def predict_view(request, company_id, days_ahead):
    try:
        # Memanggil fungsi predict_future_prices untuk mendapatkan prediksi
        predictions = predict_future_prices(company_id, days_ahead)
        
        # Menyusun data prediksi menjadi format yang bisa dikirim sebagai JSON
        predictions_data = [{'date': date.strftime('%Y-%m-%d'), 'predicted_price': price} for date, price in predictions]
        
        return render(request, 'stock_App/predict.html', {'predictions': predictions_data})
    
    except StockPrice.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def predict_list(request):
    return render(request, 'stock_app/predict_list.html')

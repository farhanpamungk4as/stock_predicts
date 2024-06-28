# stock_app/ml_utils.py

import pandas as pd
from .models import MonthlyStockPrice, StockPrice
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime

def get_stock_data(company_id):
    # Mengambil perusahaan dengan ID tertentu
    companys = StockPrice.objects.get(id=company_id)
    
    # Mengambil semua data dari model MonthlyStockPrice untuk perusahaan tertentu
    data = MonthlyStockPrice.objects.filter(stock=companys)
    
    # Membuat DataFrame dari data yang diambil
    data_list = list(data.values('month', 'highest_price', 'lowest_price', 'open_price', 'close_price'))
    df = pd.DataFrame(data_list)
    
    # Mengonversi kolom 'month' menjadi tipe datetime
    df['month'] = pd.to_datetime(df['month'])
    
    # Menetapkan kolom 'month' sebagai indeks DataFrame
    df.set_index('month', inplace=True)
    
    return df

def train_model(company_id):
    # Mengambil data saham untuk perusahaan tertentu
    df = get_stock_data(company_id)
    
    # Fitur (X) dan target (y)
    X = df.index.map(lambda x: x.toordinal()).values.reshape(-1, 1)
    y = df['close_price']
    
    # Membagi data menjadi set pelatihan dan pengujian
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Membuat dan melatih model regresi linear
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model

def predict_future_prices(company_id, days_ahead):
    # Melatih model untuk perusahaan tertentu
    model = train_model(company_id)
    
    # Mengambil bulan terakhir dari data saham
    last_month = get_stock_data(company_id).index[-1]
    
    # Menghitung bulan-bulan masa depan berdasarkan bulan terakhir
    future_months = [last_month + datetime.timedelta(days=30*x) for x in range(1, days_ahead+1)]
    
    # Mengonversi bulan-bulan masa depan menjadi nilai ordinal
    future_months_ordinal = pd.DataFrame([month.toordinal() for month in future_months], columns=['month'])
    
    # Membuat prediksi harga penutupan untuk bulan-bulan masa depan
    predictions = model.predict(future_months_ordinal.values.reshape(-1, 1))
    
    # Mengembalikan daftar tuple yang berisi bulan dan harga prediksi
    return list(zip(future_months, predictions))
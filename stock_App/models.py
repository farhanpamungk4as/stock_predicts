from django.db import models



class StockPrice(models.Model):
    company = models.CharField(max_length=100, default='Unknown Company',verbose_name='Company Name')

    def __str__(self):
        return self.company

class MonthlyStockPrice(models.Model):
    stock = models.ForeignKey(StockPrice, on_delete=models.CASCADE, related_name='Monthly_Prices')
    month = models.DateField(verbose_name='Date')
    highest_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Highest Price')
    lowest_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Lowest Price')
    open_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Open Price')
    close_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Close Price')


    def __str__(self):
        return f"{self.stock.company} - {self.month.strftime('%B %Y')}"
    

    

    


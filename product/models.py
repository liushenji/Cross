from django.db import models

# Create your models here.
from db.basemodel import BaseModel
from user.models import User


class Platform(BaseModel):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120, blank=True, null=True)
    delete_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'db_product'


class Product(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    weight = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True)
    ship_day = models.CharField(max_length=10, null=True, blank=True)
    parent_sku_number = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.CharField(max_length=10, null=True, blank=True)
    img_url1 = models.CharField(max_length=1000, null=True, blank=True)
    img_url2 = models.CharField(max_length=1000, null=True, blank=True)
    img_url3 = models.CharField(max_length=1000, null=True, blank=True)
    img_url4 = models.CharField(max_length=1000, null=True, blank=True)
    img_url5 = models.CharField(max_length=1000, null=True, blank=True)
    img_url6 = models.CharField(max_length=1000, null=True, blank=True)
    img_url7 = models.CharField(max_length=1000, null=True, blank=True)
    img_url8 = models.CharField(max_length=1000, null=True, blank=True)
    img_url9 = models.CharField(max_length=1000, null=True, blank=True)
    data_source = models.CharField(max_length=1000, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    api_push_status = models.BooleanField(default=False)
    api_push_at = models.DateTimeField(null=True, blank=True)
    delete_at = models.DateTimeField(null=True, blank=True)


class Product_SKUs(BaseModel):
    products_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku_number = models.CharField(max_length=20, null=True, blank=True)
    sku_name = models.CharField(max_length=20, null=True, blank=True)
    sku_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sku_name = models.CharField(max_length=10, null=True, blank=True)
    img_url = models.CharField(max_length=1000, null=True, blank=True)


class Original_Products_data(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_title = models.CharField(max_length=120)
    product_description = models.CharField(max_length=1000)
    product_sku_data = models.CharField(max_length=1000)
    is_th = models.IntegerField(null=True, blank=True)
    is_tw = models.IntegerField(null=True, blank=True)
    is_vn = models.IntegerField(null=True, blank=True)
    is_my = models.IntegerField(null=True, blank=True)
    is_ph = models.IntegerField(null=True, blank=True)
    is_id = models.IntegerField(null=True, blank=True)
    is_sg = models.IntegerField(null=True, blank=True)
    data_source = models.CharField(max_length=1000)
    delete_at = models.DateTimeField(null=True, blank=True)

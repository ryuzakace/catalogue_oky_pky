from django.db import models

# Create your models here.

class Categories(models.Model):
    category  = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class SubCategories(models.Model):
    sub_category = models.CharField(max_length=50)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category

class Products(models.Model):
    product = models.CharField(max_length=50)
    sub_category = models.ForeignKey(SubCategories, on_delete=models.CASCADE)

    def __str__(self):
        return self.product

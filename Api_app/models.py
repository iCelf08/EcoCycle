from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_enterprise = models.BooleanField(default=False)
    
    @property
    def total_balance(self):
        return self.ramassage_set.all().aggregate(models.Sum('balance'))['balance__sum']
    
    @property
    def total_co2(self):
        return self.ramassage_set.all().aggregate(models.Sum('co2_saved'))['co2_saved__sum']

class Trash(models.Model):
    type = models.CharField(unique=True, max_length=100)
    price_per_kilo = models.DecimalField(max_digits=10, decimal_places=2)
    co2 = models.IntegerField(default=1)
    
    def __str__(self):
        return self.type

class Ramassage(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trash_type = models.ForeignKey(Trash, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    collection_date = models.DateField(auto_now_add=True)

    @property
    def balance(self):
        return self.weight * self.trash_type.price_per_kilo

    @property
    def co2_saved(self):
        return self.weight * self.trash_type.co2





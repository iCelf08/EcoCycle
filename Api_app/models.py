from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_enterprise = models.BooleanField(default=False)
    
    @property
    def total_co2_saved(self):
        return sum(ramassage.co2_saved for ramassage in self.ramassage_set.all())

    @property
    def total_balance(self):
        return sum(ramassage.balance for ramassage in self.ramassage_set.all())

class Trash(models.Model):
    CARTON = 'carton'
    PLASTIC = 'plastic'
    GLASS = 'glass'
    
    TRASH_TYPES = [
        (CARTON, 'Carton'),
        (PLASTIC, 'Plastic'),
        (GLASS, 'Glass'),
    ]
    
    FIXED_VALUES = {
        CARTON: {'price_per_kilo': 0.5, 'co2': 0.1},
        PLASTIC: {'price_per_kilo': 1.0, 'co2': 0.2},
        GLASS: {'price_per_kilo': 0.8, 'co2': 0.15},
    }
    
    type = models.CharField(max_length=100, choices=TRASH_TYPES, unique=True)
    price_per_kilo = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    co2 = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    
    def save(self, *args, **kwargs):
        if self.type in self.FIXED_VALUES:
            self.price_per_kilo = self.FIXED_VALUES[self.type]['price_per_kilo']
            self.co2 = self.FIXED_VALUES[self.type]['co2']
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.get_type_display()} - {self.price_per_kilo} per kilo, CO2: {self.co2}"

class POI(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Ramassage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trash_type = models.ForeignKey(Trash, on_delete=models.CASCADE)
    poi = models.ForeignKey(POI, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    collection_date = models.DateField(auto_now_add=True)

    @property
    def balance(self):
        return self.weight * self.trash_type.price_per_kilo

    @property
    def co2_saved(self):
        return self.weight * self.trash_type.co2
    
    def __str__(self):
        return f"Ramassage by {self.user.username} of {self.weight} kg {self.trash_type.type} at {self.poi.name} on {self.collection_date}"

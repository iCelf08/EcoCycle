from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

class Role(models.Model):
    """
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    """
    ADMIN = "admin"
    USER = "user"

    ROLE_CHOICES = [
        (ADMIN, 'admin'),
        (USER, 'user'),
    ]

    id = models.CharField(
        choices=ROLE_CHOICES,
        max_length=20,
        unique=True,
        primary_key=True
    )

    def __str__(self):
        return self.id

class User(AbstractUser):
    roles = models.ManyToManyField(Role)

    is_enterprise = models.BooleanField(default=False)
    
    @property
    def total_co2_saved(self):
        return sum(ramassage.co2_saved for ramassage in self.ramassage_set.all())

    @property
    def co2_saved(self):
        return sum(ramassage.co2_saved for ramassage in  self.ramassage_set.all())

class Trash(models.Model):
    type = models.CharField(unique=True, max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_kilo = models.DecimalField(max_digits=10, decimal_places=2)
    co2 = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.type

class Ramassage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trash_details = models.ManyToManyField(Trash)
    address = models.CharField(max_length=255)
    collection_date = models.DateField(auto_now_add=True)

    @property
    def balance(self):
        return sum(trash.weight * trash.price_per_kilo for trash in self.trash_details.all())

    @property
    def co2_saved(self):
        return sum(trash.weight * trash.co2 for trash in self.trash_details.all())
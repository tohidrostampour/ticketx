from django.contrib.auth.models import User
from django.db import models
from utils.base_model import BaseModel


class Wallet(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField(default=0)

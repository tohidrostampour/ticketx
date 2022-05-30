import uuid
from django.db import models
from ticket.models import Order
from utils.base_model import BaseModel


class Receipt(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    tracking_code = models.UUIDField(default=uuid.uuid4, editable=False)

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Created Time',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated Time',
        auto_now=True
    )

    class Meta:
        abstract = True

from django.db import models

# Create your models here.
class employee(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    emp_id = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name


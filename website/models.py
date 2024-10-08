from django.db import models


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.name


class Quote(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    service = models.CharField(max_length=100)
    budget = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Quote"

    def __str__(self):
        return self.name

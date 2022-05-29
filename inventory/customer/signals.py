from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from customer.models import Customer

@receiver(post_save,sender=Customer)
def addCredits(sender,instance,created,**kwrgs):
    if created:
        print("Added credits")


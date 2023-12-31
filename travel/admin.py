from django.contrib import admin
from travel import models

# Register your models here.

admin.site.register(models.DestinationModel)
admin.site.register(models.RegisterationModel)
admin.site.register(models.ContinentModel)
admin.site.register(models.BookingModel)
admin.site.register(models.FeedbackModel)


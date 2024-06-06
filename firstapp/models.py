from django.db import models
#import .models from ehr #for this line to work update DB details in settings under DB section

# Create your models here.

#Stage 7: Modify the created DB

class ehr(models.Model):
    HAEMATOCRIT = models.FloatField()
    HAEMOGLOBIN = models.FloatField()
    ERYTHROCYTE = models.FloatField()
    LEUCOCYTE = models.FloatField()
    THROMBOCYTE = models.IntegerField()
    MCH = models.FloatField()
    MCHC = models.FloatField()
    MCV = models.FloatField()
    AGE = models.IntegerField()
    SEX = models.IntegerField()

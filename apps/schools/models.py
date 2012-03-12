from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255)
    free_lunch = models.IntegerField()
    reduced_lunch = models.IntegerField()
    standard = models.IntegerField() 

    def __unicode__(self):
        return self.name
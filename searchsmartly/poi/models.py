from django.contrib.gis.db import models

class PoI(models.Model):
    internal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    external_id = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    coordinates = models.PointField()
    ratings = models.JSONField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Points of intrest'

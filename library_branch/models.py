from django.db import models


class LibraryBranch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name

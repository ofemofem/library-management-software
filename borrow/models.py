from django.db import models
from django.conf import settings
from books.models import Book

from datetime import datetime, timedelta


class Borrow(models.Model):
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(default=datetime.now()+timedelta(days=30))
    returned_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
    penalty_amount = models.IntegerField(default=0)
    is_penalty = models.BooleanField(default=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)




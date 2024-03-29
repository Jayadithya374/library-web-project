from django.db import models
from profiles.models import user_profile
from books.models import book
status_choices = (
    ("placed", "Placed"),
    ("using", "Using"),
    ("returned", "Returned"),
)


# Create your models here.
class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(book, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(user_profile, models.DO_NOTHING, blank=True, null=True)
    taken = models.DateTimeField(blank=True, null=True)
    exp_return = models.DateTimeField(blank=True, null=True)
    r_status = models.CharField(choices=status_choices, default="placed", max_length=20)

    class Meta:
        managed = False
        db_table = 'orders'
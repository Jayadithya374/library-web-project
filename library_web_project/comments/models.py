from django.db import models
from profiles.models import user_profile
from books.models import book
# Create your models here.
class comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(book, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(user_profile, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'comments'
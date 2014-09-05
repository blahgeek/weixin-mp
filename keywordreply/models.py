from django.db import models

# Create your models here.

class KeywordReplyModel(models.Model):
    keyword = models.CharField(max_length=255, help_text="Keyword for match", db_index=True)
    reply = models.TextField(help_text="Text to reply when matchs")
    count = models.IntegerField(default=0, editable=False,
        help_text="How many times this keyword was matched, it's automaticlly counted")


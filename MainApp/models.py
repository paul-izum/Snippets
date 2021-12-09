from django.db import models
from django.contrib.auth.models import User

LANG_CHOICES = (
    ("py", "python"),
    ("js", "javaScript"),
    ("cs", "C#"),
)

STATE_CHOICES =(
    ("pb","public"),
    ("prt","private")

)


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANG_CHOICES)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now_add=True)
    rate = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                             blank=True, null=True)
    state = models.CharField(max_length=30, choices=STATE_CHOICES )
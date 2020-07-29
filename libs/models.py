
from django.db import models
from cms.models.pluginmodel import CMSPlugin


# Create your models here.

class t_case(CMSPlugin):
    AFF = (
        ('Zanu PF', 'Zanu PF'),
        ('MDC', 'MDC'),
    )
    PRO = (
        ('Farm Mechanisation Scheme', 'Farm Mechanisation Scheme'),
    )
    fname = models.CharField(max_length=20, default='')
    lname = models.CharField(max_length=20, default='')
    affiliation = models.CharField(choices=AFF, max_length=20, default='')
    amount = models.IntegerField()
    program = models.CharField(choices=PRO, max_length=50, default='')
    user = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.lname

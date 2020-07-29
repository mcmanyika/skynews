from django.db import models
from cms.models import CMSPlugin
from libs.models import t_case


class LibsPluginModel(CMSPlugin):
    acct = models.ForeignKey(t_case, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.acct.lname

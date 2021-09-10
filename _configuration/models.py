from django.db import models
from django.contrib.auth.models import User


class Audit(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='%(app_label)s_%(class)s_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='%(app_label)s_%(class)s_updated_by')
    is_deleted = models.BooleanField(default=False)
    

    class Meta:
        abstract = True

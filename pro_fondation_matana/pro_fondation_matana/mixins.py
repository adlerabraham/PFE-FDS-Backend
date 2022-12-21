from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth import get_user_model


class AuditMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.CharField(max_length=255, blank=False, null=True)
    updated_by = models.CharField(max_length=255, blank=False, null=True)
    

    class Meta:
        abstract = True



class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SoftDeleteModel(models.Model):

    is_deleted = models.BooleanField(default=False)
    is_deleted_at = models.DateTimeField(blank=False, null=True)
    is_deleted_by = models.CharField(max_length=255, blank=False, null=True)
    objects = models.Manager()
    undeleted_objects = SoftDeleteManager()

    def soft_delete(self):
        self.is_deleted = True
        self.is_deleted_at = timezone.now()
        self.save()

    # def restore(self):
    #     self.is_deleted = False
    #     self.save()

    class Meta:
        abstract = True




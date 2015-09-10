__author__ = 'administrator'
from django.db import models


class DonorManager(models.Manager):
    def multi_donation_donors(self):
        return self.get_queryset().annotate(donations=models.Count('donations')).filter(
            donations__gt=1)


class MultiDonationDonorManger(DonorManager):
    def get_queryset(self):
        return super(DonorManager, self).get_queryset().annotate(donations=Count('donations')).filter(
            donations__gt=1)


class ContactDonors(DonorManager):
    def get_queryset(self):
        return super(ContactDonors, self).get_queryset().filter(can_be_contacted=True)

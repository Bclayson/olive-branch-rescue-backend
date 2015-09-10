from django.db import models


# Create your models here.
from django.utils.text import slugify
from olive_branch_rescue.base_models import TrackedModel
from donors import managers


class Donation(TrackedModel):
    amount = models.IntegerField()
    donor = models.ForeignKey('Donor', related_name='donations')


class Donor(TrackedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(primary_key=True, blank=True, null=True)
    email = models.EmailField(max_length=100)
    can_be_contacted = models.BooleanField(default=True)

    @property
    def total_given(self):
        return sum(self.donations.values_list('amount', flat=True))

    multi_donations = managers.MultiDonationDonorManger()
    contacts = managers.ContactDonors()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Donor, self).save(*args, **kwargs)

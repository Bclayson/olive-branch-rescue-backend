from donors import models

__author__ = 'administrator'

from rest_framework import serializers


class DonationSerializer(serializers.ModelSerializer):
    donor = serializers.SlugRelatedField(slug_field='slug')

    class Meta:
        model = models.Donation
        fields = ('amount', 'donor')


class DonorSerializer(serializers.ModelSerializer):
    donations = serializers.SlugRelatedField(slug_field='amount', many=True)
    total_given = serializers.SerializerMethodField(method_name='get_total_given')

    class Meta:
        model = models.Donor
        fields = ('slug', 'name', 'donations', 'email', 'can_be_contacted',)

    def get_total_given(self, obj):
        return obj.total_given

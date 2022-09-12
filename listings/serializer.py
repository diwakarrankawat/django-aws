from django.forms import CharField
from rest_framework.serializers import ModelSerializer, SerializerMethodField, RelatedField
from . import models
from datetime import date

class DateSerializer(ModelSerializer):
    total_scrapped = SerializerMethodField()
    class Meta:
        model = models.Day
        fields = ["date", "total_scrapped"]
    
    def get_total_scrapped(self, obj: models.Day):
        return models.Listing.objects.filter(date=obj).count()

class DateRel(RelatedField):
    class Meta:
        model=models.Day
    def to_internal_value(self, data):
        g, _ = models.Day.objects.get_or_create(date.today())
        return g
    
    def to_representation(self, value: models.Day):
        return value.date.isoformat()

class ListingSerializer(ModelSerializer):
    date = DateRel(queryset = models.Day.objects.all())
    class Meta:
        model = models.Listing
        fields = '__all__'
        extra_kwargs = {"phone": {'required': False, 'allow_null': True}, "reviews": {'required': False, 'allow_null': True}, "website": {'required': False, 'allow_null': True, 'allow_blank':True}, "categories": {'required': False, 'allow_null': True,}, 'review_link': {'required': False, 'allow_null': True,}, 'rating': {'required': False, 'allow_null': True,}, 'address': {'required': False, 'allow_null': True,}}
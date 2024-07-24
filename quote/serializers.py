from rest_framework import serializers
from .models import Quote, Item

class QuoteSerializer(serializers.ModelSerializer):

    item = serializers.SlugRelatedField(
        slug_field="item",
        queryset=Item.objects.all(),
        allow_null=True,
        required=False,
    )
    class Meta:
        model = Quote
        fields = '__all__'
    
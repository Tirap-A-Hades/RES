from rest_framework.serializers import ModelSerializer

from real_estate_card.models import RealEstate


class EstateSerializer(ModelSerializer):
    class Meta:
        model = RealEstate
        fields = '__all__'

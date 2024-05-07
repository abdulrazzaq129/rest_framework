from rest_framework import serializers
from .models import CarList,ShowRoomList
from decimal import Decimal

def alphanumeric(value):
    if not str(value).isalnum():
        raise serializers.ValidationError("Only Alphanumeric Characters are allowed.")


        
class CarListSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()

    class Meta:
        model = CarList
        fields = '__all__'

    def get_discounted_price(self, obj):
        price = obj.price
        if price is not None:
            discount_amount = Decimal('0.05') * price  # Calculate 5% of the price
            discounted_price = price - discount_amount
            return round(discounted_price, 2)  # Round the discounted price to 2 decimal places
        else:
            return None

# class CarListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField(read_only=True)
#     chassisnumber = serializers.CharField(max_length=100, validators=[alphanumeric])
#     price = serializers.DecimalField(max_digits=9, decimal_places=2)

#     def create(self, validated_data):
#         return CarList.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.chassisnumber = validated_data.get('chassisnumber', instance.chassisnumber)
#         instance.price = validated_data.get('price', instance.price)
#         instance.save()
#         return instance
    
    def validate_price(self, value):
        if value <= 10000:
            raise serializers.ValidationError("Price must be greater than or equal to 10000.")
        return value
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Description Value Must be different.")
        return data

class ShowRoomSerializer(serializers.ModelSerializer):
    # Showrooms = CarListSerializer(many=True, read_only=True)
    # Showrooms = serializers.StringRelatedField(many=True)
    # Showrooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Showrooms = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='car-detail-view'
    # )

    class Meta:
        model = ShowRoomList
        fields = "__all__"
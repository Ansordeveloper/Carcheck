from rest_framework import serializers

from apps.cars.models import Car, SpecialMarks, PeriodsOwnership


class SpecialMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialMarks
        fields = "__all__"

class PeriodsOwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodsOwnership
        fields = "__all__"

class CarSerializer(serializers.ModelSerializer):
    cars_special_marks = SpecialMarksSerializer(read_only=True, many=True)
    cars_periods_ownership = PeriodsOwnershipSerializer(read_only=True, many=True)
    class Meta:
        model = Car
        fields = ('id', 'license_plate', 'brand', 'model', 'color', 
                'year', 'rudder_location', 'engine_volume',
                'cars_special_marks', 'cars_periods_ownership')
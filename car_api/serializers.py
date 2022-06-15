from rest_framework import serializers
from car_api.models import Car, Reservation


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'vehicle_number', 'vehicle_name', 'model', 'rent_type']


class AvailableCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'vehicle_number',
                  'vehicle_name', 'model', 'availability']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'customer', 'car', 'issue_date',
                  'return_date', 'payment_type']


class CarDetailsReservationSerializer(serializers.Serializer):
    car = CarSerializer()
    current_active_bookings = ReservationSerializer(many=True)

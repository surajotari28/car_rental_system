import json
from datetime import date
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from car_api.models import Reservation
from car_api.serializers import ReservationSerializer


@api_view(['GET'])
def view_all_reservations(request):
    """
    API endpoint for showing all reservations in the system.
    """
    if request.method == 'GET':
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def view_reservation_details(request, rent_pk):
    """
    API endpoint for showing a particular reservation details.
    """
    try:
        reservation = Reservation.objects.get(pk=rent_pk)
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)


permission_classes = [IsAuthenticated]


@api_view(['POST'])
def book_car(request):
    """
    API endpoint for booking an available car.
    """
    if request.method == 'POST':
        serializer = ReservationSerializer(data=request.data)

        if serializer.is_valid():
            current_date = date.today()
            issue_date = serializer.validated_data['issue_date']
            return_date = serializer.validated_data['return_date']

            car = serializer.validated_data['car']
            reservations = Reservation.objects.all().filter(car=car.id)

            for r in reservations:
                if r.issue_date <= issue_date <= r.return_date:
                    content = {
                        "message": "The selected car is not available on this date"}
                    return Response(data=json.dumps(content), status=status.HTTP_400_BAD_REQUEST)

            if current_date <= issue_date and issue_date <= return_date:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

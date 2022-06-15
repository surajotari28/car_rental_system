from django.urls import path
from car_api.views import car, reservation

urlpatterns = [
    path('car/', car.view_all_cars),
    path('car/add/', car.add_car),
    path('car/<int:car_pk>/', car.view_car_details),
    path('car/<int:car_pk>/active_booking/',
         car.view_car_details_active_booking),
    path('car/<int:car_pk>/update/', car.edit_car_details),
    path('car/<int:car_pk>/delete/', car.delete_car),

    path('rent/', reservation.view_all_reservations),
    path('rent/book/', reservation.book_car),
    path('rent/<int:rent_pk>/', reservation.view_reservation_details),

    path('car/status/', car.view_all_cars_on_given_date)

]

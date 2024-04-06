from django.urls import path
from . import stuview  # Import your views.py
from . import adminviews 

urlpatterns = [
    path('student_login/', stuview.student_login, name='student_login'),
    path('student_dashboard/', stuview.student_dashboard, name='student_dashboard'),
    path('book_room/<int:room_id>/', stuview.book_room, name='book_room'),
    # Add similar URL patterns for other functionalities (admin login, book room, etc.)
    path('admin_login/', adminviews.admin_login, name='admin_login'),
    path('admin_dashboard/', adminviews.admin_dashboard, name='admin_dashboard'),
    # Add additional URL patterns for admin functionalities (e.g., manage rooms, manage bookings)
    path('manage_rooms/', adminviews.manage_rooms, name='manage_rooms'),  # Example for managing rooms
    path('manage_bookings/<int:booking_id>/', adminviews.manage_booking, name='manage_booking'),  # Example for managing bookings (specific booking)
]
 

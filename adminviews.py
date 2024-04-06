from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Room, Booking

def admin_login(request):
  if request.method == 'POST':
    email = request.POST['email']
    admin_id = request.POST['AdminID']
    #password = request.POST['password']
    #user = authenticate(username=email, password=password)
    user = authenticate(username=email, admin_id=admin_id)
    if user is not None:
      if user.is_staff:
        login(request, user)
        return redirect('admin_dashboard')
      else:
        # Handle non-staff user trying to login as admin
        return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
  return render(request, 'admin_login.html')

def admin_dashboard(request):
  if not request.user.is_authenticated or not request.user.is_staff:
    return redirect('admin_login')
  bookings = Booking.objects.all()
  return render(request, 'admin_dashboard.html', {'bookings': bookings})

def manage_rooms(request):
  if not request.user.is_authenticated or not request.user.is_staff:
    return redirect('admin_login')
  if request.method == 'POST':
    # Implement logic to add a new room based on form data
    room_name = request.POST['room_name']
    capacity = request.POST['capacity']
    # Add data validation and error handling
    room = Room.objects.create(name=room_name, capacity=capacity)
    room.save()
    return redirect('manage_rooms')  # Redirect back to manage rooms after adding
  rooms = Room.objects.all()
  return render(request, 'manage_rooms.html', {'rooms': rooms})

def manage_booking(request, booking_id):
  if not request.user.is_authenticated or not request.user.is_staff:
    return redirect('admin_login')
  try:
    booking = Booking.objects.get(pk=booking_id)
  except Booking.DoesNotExist:
    # Handle case where booking ID is not found
    return render(request, 'manage_booking.html', {'error': 'Booking not found'})
  if request.method == 'POST':
    action = request.POST['action']  # Get the selected action (approve/reject)
    if action == 'approve':
      booking.status = 'approved'
    elif action == 'reject':
      booking.status = 'rejected'
    # Add data validation and error handling
    booking.save()
    return redirect('admin_dashboard')  # Redirect back to admin dashboard after updating booking
  return render(request, 'manage_booking.html', {'booking': booking})

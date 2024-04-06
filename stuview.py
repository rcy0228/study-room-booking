from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Room, Booking

def student_login(request):
  if request.method == 'POST':
    email = request.POST['Email']
    student_id = request.POST['StudentID']
    #password = request.POST['password']
    #user = authenticate(username=email, password=password)
    user = authenticate(username=email, student_id=student_id)
    if user is not None:
      if user.is_staff:  # Check if user is not a staff (admin)
        return redirect('admin_login')  # Redirect to admin login
      login(request, user)
      return redirect('student_dashboard')
    else:
      # Handle invalid credentials
      return render(request, 'student_login.html', {'error': 'Invalid credentials'})
  return render(request, 'student_login.html')

def student_dashboard(request):
  if not request.user.is_authenticated:
    return redirect('student_login')
  rooms = Room.objects.all()
  bookings = Booking.objects.filter(student=request.user)
  return render(request, 'student_dashboard.html', {'rooms': rooms, 'bookings': bookings})

def book_room(request, room_id):
  if not request.user.is_authenticated:
    return redirect('student_login')
  room = Room.objects.get(pk=room_id)
  # Check for existing bookings and date conflicts
  if request.method == 'POST':
    date = request.POST['date']
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    # Add validation for booking conflicts and time format
    booking = Booking.objects.create(student=request.user, room=room, date=date, start_time=start_time, end_time=end_time, status='pending')
    booking.save()
    return redirect('student_dashboard')
  return render(request, 'book_room.html', {'room': room})

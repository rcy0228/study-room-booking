from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
  name = models.CharField(max_length=100)
  capacity = models.IntegerField()

  def __str__(self):
    return self.name

class Booking(models.Model):
  student = models.ForeignKey(User, on_delete=models.CASCADE)
  room = models.ForeignKey(Room, on_delete=models.CASCADE)
  date = models.DateField()
  start_time = models.TimeField()
  end_time = models.TimeField()
  status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('Available', 'available')])

  def __str__(self):
    return f"{self.student.username} - {self.room.name} on {self.date}"

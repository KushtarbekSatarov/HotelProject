from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    star_rating = models.DecimalField(max_digits=2, decimal_places=1)
    amenities = models.TextField()
    image = models.ImageField(upload_to='hotels/img/')

    def __str__(self):
        return self.name


class RoomType(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, default='Single')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='room_types')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    max_occupancy = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests = models.IntegerField()

    def __str__(self):
        return f"Booking for {self.user.username} at {self.room_type.hotel.name}"


class Reviews(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hotel/img/')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.hotel.name}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='favorites')
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return self.user.username


# alumni/models.py

from django.db import models
from django.contrib.auth.models import User

class AlumniProfile(models.Model):
    DEPARTMENT_CHOICES = [
        ("CE", "Civil Engineering"),
        ("EEE", "Electrical & Electronic Engineering"),
        ("ME", "Mechanical Engineering"),
        ("CSE", "Computer Science & Engineering"),
        ("ETE", "Electronics & Telecommunication Engineering"),
        ("IPE", "Industrial & Production Engineering"),
        ("GCE", "Glass & Ceramic Engineering"),
        ("URP", "Urban & Regional Planning"),
        ("MTE", "Mechatronics Engineering"),
        ("ARCH", "Architecture"),
        ("ECE", "Electrical & Computer Engineering"),
        ("ChE/CFPE", "Chemical/CFPE"),
        ("BECM", "Building Engineering & Construction Management"),
        ("MSE", "Materials Science & Engineering"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, blank=True)
    batch = models.CharField(max_length=50)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    phone_number = models.CharField(max_length=20)
    alternative_phone = models.CharField(max_length=20, blank=True)
    present_address = models.TextField()
    permanent_address = models.TextField()
    current_job = models.TextField()
    previous_job = models.CharField(max_length=255, blank=True)
    college_days_tableegh = models.TextField()
    DISTRICT_CHOICES = [
    ("Bagerhat", "Bagerhat"),
    ("Bandarban", "Bandarban"),
    ("Barguna", "Barguna"),
    ("Barisal", "Barisal"),
    ("Bhola", "Bhola"),
    ("Bogra", "Bogra"),
    ("Brahmanbaria", "Brahmanbaria"),
    ("Chandpur", "Chandpur"),
    ("Chapai Nawabganj", "Chapai Nawabganj"),
    ("Chittagong", "Chittagong"),
    ("Chuadanga", "Chuadanga"),
    ("Comilla", "Comilla"),
    ("Cox's Bazar", "Cox's Bazar"),
    ("Dhaka", "Dhaka"),
    ("Dinajpur", "Dinajpur"),
    ("Faridpur", "Faridpur"),
    ("Feni", "Feni"),
    ("Gaibandha", "Gaibandha"),
    ("Gazipur", "Gazipur"),
    ("Gopalganj", "Gopalganj"),
    ("Habiganj", "Habiganj"),
    ("Jamalpur", "Jamalpur"),
    ("Jessore", "Jessore"),
    ("Jhalokati", "Jhalokati"),
    ("Jhenaidah", "Jhenaidah"),
    ("Joypurhat", "Joypurhat"),
    ("Khagrachhari", "Khagrachhari"),
    ("Khulna", "Khulna"),
    ("Kishoreganj", "Kishoreganj"),
    ("Kurigram", "Kurigram"),
    ("Kushtia", "Kushtia"),
    ("Lakshmipur", "Lakshmipur"),
    ("Lalmonirhat", "Lalmonirhat"),
    ("Madaripur", "Madaripur"),
    ("Magura", "Magura"),
    ("Manikganj", "Manikganj"),
    ("Meherpur", "Meherpur"),
    ("Moulvibazar", "Moulvibazar"),
    ("Munshiganj", "Munshiganj"),
    ("Mymensingh", "Mymensingh"),
    ("Naogaon", "Naogaon"),
    ("Narail", "Narail"),
    ("Narayanganj", "Narayanganj"),
    ("Narsingdi", "Narsingdi"),
    ("Natore", "Natore"),
    ("Netrokona", "Netrokona"),
    ("Nilphamari", "Nilphamari"),
    ("Noakhali", "Noakhali"),
    ("Pabna", "Pabna"),
    ("Panchagarh", "Panchagarh"),
    ("Patuakhali", "Patuakhali"),
    ("Pirojpur", "Pirojpur"),
    ("Rajbari", "Rajbari"),
    ("Rajshahi", "Rajshahi"),
    ("Rangamati", "Rangamati"),
    ("Rangpur", "Rangpur"),
    ("Satkhira", "Satkhira"),
    ("Shariatpur", "Shariatpur"),
    ("Sherpur", "Sherpur"),
    ("Sirajganj", "Sirajganj"),
    ("Sunamganj", "Sunamganj"),
    ("Sylhet", "Sylhet"),
    ("Tangail", "Tangail"),
    ("Thakurgaon", "Thakurgaon"),
]

class AlumniProfile(models.Model):
    # ... other fields ...
    home_district = models.CharField(max_length=50, choices=DISTRICT_CHOICES)
    # ...
    blood_group = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username

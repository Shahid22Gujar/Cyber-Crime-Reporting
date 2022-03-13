from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
CYBER_CRIME_CATEGORY=(
    ('CP','Child Pornography'),
    ('CB','Cyber Bullying'),
    ('P','Phishing'),
    ('OJF','Online Job Fraud'),
    ('V','Vishing'),
    ('Sm','Smishing'),
    ('S','Sexting'),
    ('P','Phishing'),
    ('SimSS','SIM Swap Scam'),
    ('Sp','Spamming'),
    ('R','Ransomware'),
    ('DB','Data Breach'),
    ('DoS','Denial Services of Attack'),
    ('VWM','Viruses,Worms,and Trojans'),
)

class VictimUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    user_adhar=models.CharField(max_length=50)
    category_crime=models.CharField(choices=CYBER_CRIME_CATEGORY,max_length=10)
    screenshot=models.ImageField(upload_to="screenshot/")
    suspected_person=models.CharField(max_length=50)
    date_crime=models.DateTimeField()
    suspected_email=models.EmailField()
    mobile=models.CharField(max_length=12)
    suspected_mobile=models.CharField(max_length=12)
    crime_source=models.CharField(max_length=100)
    id_usedby_criminal=models.CharField(max_length=50)
    def __str__(self):
        return str(self.user)

class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='profile_img')
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    email=models.EmailField()
    dob=models.DateField()



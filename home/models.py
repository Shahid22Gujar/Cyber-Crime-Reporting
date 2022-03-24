
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

class Report(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    ip=models.GenericIPAddressField(blank=True,null=True)
    # user_adhar=models.CharField(max_length=50)
    category_crime=models.CharField(choices=CYBER_CRIME_CATEGORY,max_length=10)
    # suspected_person=models.CharField(max_length=50)
    # screenshots_obj=models.ForeignKey("Screenshots",on_delete=models.CASCADE,null=True)
    date_crime=models.DateTimeField()
    suspected_email=models.EmailField(blank=True)
    mobile=models.CharField(max_length=12,blank=True)
    suspected_mobile=models.CharField(max_length=12,blank=True)
    incident_place=models.CharField(max_length=100)
    # id_usedby_criminal=models.CharField(max_length=50)
    reason_for_delay_reporting=models.CharField(max_length=200,blank=True)
    additional_information=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return f'{self.user if self.user else self.ip}'

class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='profile_img')
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    email=models.EmailField()
    dob=models.DateField()

class Screenshots(models.Model):
    victimuser=models.ForeignKey(Report,on_delete=models.CASCADE,null=True)
    screenshots=models.ImageField(upload_to="screenshot/")
    def __str__(self) -> str:
        return str(self.victimuser)



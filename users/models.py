from django.db import models
# from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	is_counsellor = models.BooleanField(default=False, null=True)
	is_counsellee = models.BooleanField(default=False, null=True)

	def __str__(self):
		return self.username


class Profile(models.Model):
	GENDER = (
        ('female', 'Female'),
        ('male', 'Male'),
    )
	dob = models.DateField('date of birth', null=True, blank = True)
	gender = models.CharField(max_length=10, choices=GENDER, null=True, blank = True)
	address = models.CharField(max_length=200, null=True, blank = True)
	phone_number = models.BigIntegerField('mobile number', null=True, blank = True)
	bio = models.TextField('short bio', null=True, blank = True)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)


	class Meta:
		abstract = True 

	def __str__(self):
		return f"{self.user.username}'s Profile"


class Counsellee(Profile):
	interests = models.TextField(null=True, blank = True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'counsellee', null=True)
	active = models.BooleanField(default=True, null=True)

class Counsellor(Profile):
	quote = models.CharField(max_length=300, null=True, blank=True)
	website = models.CharField(max_length=300, null=True, blank = True)
	qualification = models.CharField('education and qualifications', max_length=300, null=True, blank=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'counsellor', null=True)
	available = models.BooleanField(default=True, null=True)
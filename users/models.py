from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

from PIL import Image


class Category(models.Model):
	name = models.CharField(max_length=200, null=True)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'


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
	dob = models.DateField('date of birth', null=True, blank=True)
	gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
	address = models.CharField(max_length=200, null=True, blank = True)
	phone_number = models.BigIntegerField('mobile number', null=True, blank=True)
	bio = models.TextField('short bio', null=True, blank=True)
	image = models.ImageField(default='default.png', upload_to='profile_photos', null=True)

	class Meta:
		abstract = True 

	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}'s Profile"

	def save(self):
		super().save() # run save method of super class
		img = Image.open(self.image.path) # open image that has been saved
		if img.height > 300 or img.width > 400:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)


class Counsellee(Profile):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'counsellee', null=True)
	categories = models.ManyToManyField(Category)
	interests = models.TextField(null=True, blank = True)
	twitter_handle = models.CharField(max_length=120, null=True) 
	active = models.BooleanField(default=True, null=True)


class Counsellor(Profile):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'counsellor', null=True)
	counsellees = models.ManyToManyField(Counsellee, through='Counselling')
	specialty = models.ManyToManyField(Category)
	quote = models.CharField(max_length=300, null=True, blank=True)
	website = models.CharField(max_length=300, null=True, blank = True)
	qualification = models.CharField('education and qualifications', max_length=300, null=True, blank=True)
	available = models.BooleanField(default=True, null=True)


class Counselling(models.Model):
	counsellor = models.ForeignKey(Counsellor, on_delete=models.CASCADE, null=True)
	counsellee = models.ForeignKey(Counsellee, on_delete=models.CASCADE, null=True)
	date_contacted = models.DateField(default=timezone.now)
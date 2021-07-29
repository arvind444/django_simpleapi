from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length = 200)
	language = models.CharField(max_length = 100)
	instructor = models.CharField(max_length = 50)
	price = models.CharField(max_length = 15)

	def __str__(self):
		return f"The course name is {self.name} The language you are going to learn is {self.language}. Your course instructor will be {self.instructor}. The course price is {self.price}."
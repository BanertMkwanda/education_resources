from django.db import models

# Create your models here.

class EducationLevel(models.Model):
	# Primary or secondary level.
	text = models.CharField(max_length=30)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		# Return a string presentation of the EducationLevel model.
		return self.text

class ClassLevel(models.Model):
	# Junior or Senior
	educationlevel = models.ForeignKey(EducationLevel, on_delete=models.CASCADE)
	text = models.CharField(max_length=30)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		# return a string presentation of ClassLevel  model.
		return self.text

class Grade(models.Model):
	# Class like form 1, standard 4 to which resource that  user is looking for belong like form 4.
	classlevel = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
	text = models.CharField(max_length=30)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'classies'

	def __str__(self):
		# Return string representation of the Class model.
		return self.text

class Subject(models.Model):
	# subject of the resuorce that user is looking for like Agriculture.
	grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
	text = models.CharField(max_length=30)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'subjects'

	def __str__(self):
		# Return a string reppresentation of the Subject model.
		return self.text

class ResourceType(models.Model):
	# Type of material user is lookig for like book, pamphlet
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	text = models.CharField(max_length=30)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		# Return a strimg representation of ResourceType model.
		return self.text

class Document(models.Model):
	# Admin uploading pdf
	resource_type = models.ForeignKey(ResourceType, on_delete=models.CASCADE)
	caption = models.CharField(max_length=40)
	price = models.FloatField()
	back_cover = models.ImageField(upload_to="back_covers/")
	front_cover = models.ImageField(upload_to="front_covers/")
	uploaded_document = models.FileField(upload_to="documents/")
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'documents'

	def __str__(self):
		# return a string representstion of the Document model.
		return self.caption



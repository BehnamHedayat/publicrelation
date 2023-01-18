from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    idNumber = models.PositiveIntegerField()
    organ = models.CharField(max_length=100)
    job = models.CharField(max_length=60)
    employDate = models.DateField()
    birthDate = models.DateField()
    pesonalPhone = models.PositiveIntegerField()
    jobPhone = models.PositiveIntegerField()

    def __str__(self):
        return "{} {} {}".format(self.firstName, self.lastName, self.jobPhone)


#skill models

class Skills(models.Model):
    skillName = models.CharField(max_length=200)
    description = models.TextField()
    experince = models.PositiveIntegerField()

    def __str__(self):
        return "{} {}".format(self.skillName, self.experince)

from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=10)

class Company(models.Model):
    companyname=models.CharField(max_length=100)
    liscenceno=models.CharField(max_length=50)
    place=models.CharField(max_length=100)
    pin=models.CharField(max_length=10)
    post=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    photo=models.CharField(max_length=500)
    phoneno=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    status=models.CharField(max_length=10)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Guide(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=20)
    phoneno=models.CharField(max_length=20)
    photo=models.CharField(max_length=500)
    place=models.CharField(max_length=100)
    pin=models.CharField(max_length=10)
    post=models.CharField(max_length=100)
    district=models.CharField(max_length=500)
    workplace=models.CharField(max_length=500)
    qualification=models.CharField(max_length=500)
    certificate=models.CharField(max_length=500)
    status = models.CharField(max_length=10)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=500)
    phone=models.CharField(max_length=20)
    photo=models.CharField(max_length=500)
    place=models.CharField(max_length=100)
    pin=models.CharField(max_length=20)
    post=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)


class Job(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    qualification=models.CharField(max_length=50)
    description=models.CharField(max_length=1000)
    date=models.DateField()


class Vacancy(models.Model):
    JB = models.CharField(max_length=100)
    COMPANY = models.ForeignKey(Company, on_delete=models.CASCADE)
    companydetails = models.CharField(max_length=1000)
    eligibility = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)


class Application(models.Model):
    VACANCY = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    CV=models.CharField(max_length=1000)
    status = models.CharField(max_length=10)


class Chat(models.Model):
    FROM =models.ForeignKey(Login, on_delete=models.CASCADE,related_name="fromid")
    TO =models.ForeignKey(Login, on_delete=models.CASCADE,related_name="toid")
    message=models.CharField(max_length=1000)
    date = models.DateField()


class Request(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    GUIDE = models.ForeignKey(Guide, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)

class Videos(models.Model):
    video = models.CharField(max_length=1000)
    date = models.DateField()
    title =models.CharField(max_length=100)
    description =models.CharField(max_length=100)












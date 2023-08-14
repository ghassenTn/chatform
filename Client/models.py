from django.db import models
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=200)
    age = models.IntegerField()
    nblogged = models.IntegerField(default=1)
    def __str__(self):
        return self.name
    def setnblogged(self):
        self.nblogged = self.nblogged+1
    def getnblogged(self):
        return self.nblogged

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Post by {self.user.name}"

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

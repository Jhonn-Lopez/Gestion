from django.db import models

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class ActiveCurse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curse = models.ForeignKey('Curse', on_delete=models.CASCADE)
    is_active = models.CharField(max_length=1)

class Alternative(models.Model):
    alt_id = models.IntegerField(primary_key=True)
    alt_desc = models.CharField(max_length=250)  # Asegúrate de ajustar la longitud según tus necesidades
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

class CorrectAnswer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    alternative = models.ForeignKey(Alternative, on_delete=models.CASCADE)

class Curse(models.Model):
    curse_id = models.IntegerField(primary_key=True)
    cur_name = models.CharField(max_length=250)
    cur_desc = models.CharField(max_length=1000)
    module = models.ForeignKey('Module', on_delete=models.CASCADE)

class Module(models.Model):
    module_id = models.IntegerField(primary_key=True)
    mod_name = models.CharField(max_length=250)
    mod_desc = models.CharField(max_length=1000)
    video = models.BinaryField(null=True)  # Puedes utilizar BinaryField para el campo "video"
    text = models.TextField()  # Utilizamos TextField para el campo "text"

class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=500)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

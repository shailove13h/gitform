from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Taluka(models.Model):
    
    name = models.CharField(max_length=30)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='taluka')
    def __str__(self):
        return self.name

class Block(models.Model):
    
    name = models.CharField(max_length=30)
    taluka = models.ForeignKey(Taluka, on_delete=models.CASCADE, related_name='blockes')
    def __str__(self):
        return self.name

class Sector(models.Model):
    
    name = models.CharField(max_length=30)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='sector')
    def __str__(self):
        return self.name
    
class Village(models.Model):
    
    name = models.CharField(max_length=30)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='village')
    def __str__(self):
        return self.name
    
class AWC(models.Model):
    
    name = models.CharField(max_length=100)
    awccode = models.CharField(max_length=30)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='awc')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='awc')
    def __str__(self):
        return self.name
    


class User(AbstractUser, models.Model):
    email = models.EmailField(unique = True)

class Choices(models.Model):
    choice = models.CharField(max_length=5000)
    is_answer = models.BooleanField(default=False)

class Questions(models.Model):
    question = models.CharField(max_length= 10000)
    question_type = models.CharField(max_length=20)
    required = models.BooleanField(default= False)
    answer_key = models.CharField(max_length = 5000, blank = True)
    score = models.IntegerField(blank = True, default=0)
    feedback = models.CharField(max_length = 5000, null = True)
    choices = models.ManyToManyField(Choices, related_name = "choices")
    districts = models.ManyToManyField(District, related_name = "districts")
    blocks = models.ManyToManyField(Block, related_name = "blocks")
    sectors = models.ManyToManyField(Sector, related_name = "sectors")
    villages = models.ManyToManyField(Village, related_name = "villages")
    awcs = models.ManyToManyField(AWC, related_name = "awcs")

class Answer(models.Model):
    answer = models.CharField(max_length=5000)
    answer_to = models.ForeignKey(Questions, on_delete = models.CASCADE ,related_name = "answer_to")

class Form(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000, blank = True)
    creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "creator")
    background_color = models.CharField(max_length=20, default = "#d9efed")
    text_color = models.CharField(max_length=20, default="#272124")
    collect_email = models.BooleanField(default=False)
    authenticated_responder = models.BooleanField(default = False)
    edit_after_submit = models.BooleanField(default=False)
    confirmation_message = models.CharField(max_length = 10000, default = "Your response has been recorded.")
    is_quiz = models.BooleanField(default=False)
    is_district = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)
    is_sector = models.BooleanField(default=False)
    is_village = models.BooleanField(default=False)
    allow_view_score = models.BooleanField(default= True)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    questions = models.ManyToManyField(Questions, related_name = "questions")

class Responses(models.Model):
    response_code = models.CharField(max_length=20)
    response_to = models.ForeignKey(Form, on_delete = models.CASCADE, related_name = "response_to")
    responder_ip = models.CharField(max_length=30)
    responder = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "responder", blank = True, null = True)
    responder_email = models.EmailField(blank = True)
    response = models.ManyToManyField(Answer, related_name = "response")




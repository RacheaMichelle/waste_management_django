from django.db import models
from django.contrib.auth.models import User

class QuizQuestion(models.Model):
    WASTE_TYPES = [
        ('plastic', 'Plastic'),
        ('paper', 'Paper'),
        ('glass', 'Glass'),
        ('organic', 'Organic'),
        ('metal', 'Metal'),
        ('e-waste', 'E-Waste'),
        ('clothing', 'Clothing'),
        ('hazardous', 'Hazardous'),
        ('construction', 'Construction'),
        ('medical', 'Medical'),
    ]

    question = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=20, choices=WASTE_TYPES)
    wrong_answer_1 = models.CharField(max_length=20, choices=WASTE_TYPES)
    wrong_answer_2 = models.CharField(max_length=20, choices=WASTE_TYPES)
    explanation = models.TextField()

class QuizScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

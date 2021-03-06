from django.db import models
from django.conf import settings


class Quiz(models.Model):
    name = models.CharField(max_length=150)
    time = models.IntegerField(help_text="duration of the quiz in second", default=1)
    number_of_question = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Question(models.Model):
    content = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', blank=True)

    def __str__(self):
        return self.content


class Answer(models.Model):
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True)
    number = models.IntegerField(default=1, blank=True)

    def __str__(self):
        return f"question: {self.question}, answer: {self.content}, correct: {self.is_correct}"


class MarksOfUser(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, null=True)
    question = models.ManyToManyField(Question, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.user} answer to {self.question.first()} and {self.quiz}"

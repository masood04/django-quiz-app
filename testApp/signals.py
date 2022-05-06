from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Question
from django.db import DatabaseError


@receiver(pre_save, sender=Question)
def check_maximum_question_of_quiz(sender, instance, **kwargs):
    quiz = instance.quiz
    print('Debug')
    if quiz.questions.count() >= quiz.number_of_question:
        raise DatabaseError('You have reached maximum number of question')

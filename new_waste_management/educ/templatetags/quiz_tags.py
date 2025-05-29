from django import template
import random

register = template.Library()

@register.filter
def get_answers_randomized(question):
    answers = [question.correct_answer, question.wrong_answer_1, question.wrong_answer_2]
    random.shuffle(answers)
    return answers

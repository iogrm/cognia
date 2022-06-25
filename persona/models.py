from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Mbti(models.Model):
    mbti = models.CharField(max_length=128, null=False, blank=False)
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/mbti_avatar/', null=False, blank=False)
    description = RichTextField()

    def __str__(self):
        return self.mbti


class UserProfile(models.Model):
    email = models.EmailField(max_length=512, null=False, blank=False)
    first_name = models.CharField(max_length=128, null=True, blank=False)
    sir_name = models.CharField(max_length=128, null=True, blank=False)
    mbti = models.ForeignKey('Mbti', on_delete=models.CASCADE)
    birth = models.DateField(null=True, blank=False)
    isFemale = models.BooleanField(null=True, blank=False)

    def __str__(self):
        return self.first_name


class Character(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    title = models.CharField(max_length=128, null=True, blank=True)
    mbti = models.ForeignKey('Mbti', on_delete=models.CASCADE)
    isFemale = models.BooleanField(null=False, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    cover = models.FileField(upload_to='files/character_cover/', null=False, blank=False,
                             validators=[validate_file_extension])
    description = RichTextField()

    def __str__(self):
        if self.title is None:
            return self.name
        else:
            return self.name + "  -  " + self.title


class Place(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    loc = models.CharField(max_length=128, null=False, blank=False)
    mbti = models.ForeignKey('Mbti', on_delete=models.CASCADE)
    description = RichTextField()
    picture = models.FileField(upload_to='files/place_cover/', null=False, blank=False,
                               validators=[validate_file_extension])


class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/category_cover/', null=False, blank=False,
                             validators=[validate_file_extension])

    def __str__(self):
        return self.title


class Trait(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    symbol = models.CharField(max_length=128, null=False, blank=False)
    description = RichTextField()

    def __str__(self):
        return str(self.title)


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    trait_agree = models.ForeignKey('Trait', on_delete=models.CASCADE, related_name='trait_agree')
    trait_disagree = models.ForeignKey('Trait', on_delete=models.CASCADE, related_name='trait_disagree')
    question = RichTextField()

    def __str__(self):
        return "Question " + str(self.question_id)


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    answer = models.IntegerField(null=False, blank=False, default=0)

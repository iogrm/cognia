from django.contrib import admin

from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'mbti']


admin.site.register(UserProfile, UserProfileAdmin)


class CharacterAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['name', 'title', 'category']


admin.site.register(Character, CharacterAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Category, CategoryAdmin)


class MbtiAdmin(admin.ModelAdmin):
    list_display = ['mbti', 'title']


admin.site.register(Mbti, MbtiAdmin)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'loc', 'mbti']


admin.site.register(Place, PlaceAdmin)


class TraitAdmin(admin.ModelAdmin):
    list_display = ['title', 'symbol']


admin.site.register(Trait, TraitAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'trait_agree', 'trait_disagree', 'question']


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_id', 'user', 'question', 'time', 'answer']


admin.site.register(Answer, AnswerAdmin)

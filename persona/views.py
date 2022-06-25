from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from .analyse import get_mbti
from .models import *
from django.shortcuts import render
from .forms import SignupForm, LoginForm


class SignupPage(TemplateView):
    def get(self, request, **kwargs):
        form = SignupForm(request.GET or None)
        error_css = {
            'input_email_class': "",
            'span_email_style': "display: none;",
        }
        if form.is_valid():
            print("is valid")
            first_name = form.cleaned_data.get("first_name")
            sir_name = form.cleaned_data.get("sir_name")
            email = form.cleaned_data.get("email")
            mbti = Mbti.objects.filter(mbti__contains="xxxx")[0]
            print(mbti)
            users = UserProfile.objects.filter(email__contains=email)
            if not users:
                print('if not users:')
                user = UserProfile()
                user.first_name = first_name
                user.sir_name = sir_name
                user.email = email
                user.mbti = mbti
                user.save()
                request.session['email'] = email
                return redirect('test')

        else:
            print(form.errors)
            print('else not users:')
            error_css = {
                'input_email_class': "error",
                'span_email_style': "",
            }

        context = {
            'form': form,
            'error_css': error_css,
        }

        return render(request, 'signup.html', context)


class LoginPage(TemplateView):
    def get(self, request, **kwargs):
        form = LoginForm(request.GET or None)
        error_css = {
            'input_email_class': "",
            'span_email_style': "display: none;",
        }
        if form.is_valid():
            print("is valid")
            email = form.cleaned_data.get("email")
            users = UserProfile.objects.filter(email__contains=email)
            if users:
                user = LoginForm()
                user.email = email
                request.session['email'] = email
                return redirect('home')
            else:
                print('else users:')
                print(form.errors)
                error_css = {
                    'input_email_class': "error",
                    'span_email_style': "",
                }

        context = {
            'form': form,
            'error_css': error_css,
        }
        return render(request, 'login.html', context)


class PassportPage(TemplateView):
    def get(self, request, **kwargs):
        print()
        print('passport:')
        user_data = []
        character_data = []
        email = request.session.get('email')
        users = UserProfile.objects.filter(email__contains=email)
        user = users[0]
        mbti = user.mbti
        print(mbti)
        mbti = Mbti.objects.filter(mbti=mbti)[0]
        user_data.append({
            'email': user.email,
            'mbti_title': mbti.title,
            'cover': mbti.cover.url,
            'sir_name': user.sir_name,
            'first_name': user.first_name,
            'mbti': mbti.mbti,
            'birth': user.birth,
            'isFemale': user.isFemale,
        })

        place = Place.objects.filter(mbti=mbti)[0]
        user_data.append({
            'name': place.title,
            'pic': place.picture.url,
        })

        all_characters = Character.objects.filter(mbti=mbti)
        for character in all_characters:
            character_data.append({
                'name': character.name,
                'title': self.getTitle(character),
                'cover': character.cover.url,
                'category': character.category.title,
            })

        # print(character_data)
        context = {
            'character_data': character_data,
            'user_data': user_data,
        }

        return render(request, 'passport.html', context)

    def getTitle(self, character):
        if not character.title:
            title = character.name
        else:
            title = character.title
        return title


# Create your views here.
def test_page(request):
    email = request.session.get('email')
    user = UserProfile.objects.filter(email__contains=email)[0]
    if request.method == 'POST':
        print()
        print(request.POST)
        questions = Question.objects.all()
        traits = {}
        for q in questions:
            print(q.question_id)
            print(request.POST.get(str(q.question_id)))
            answer = request.POST.get(str(q.question_id))
            if answer == 'agree_max':
                traits[q.trait_agree.title] = traits.get(q.trait_agree.title, 0) + 3
                print("agree max", q.trait_agree.title, traits[q.trait_agree.title])
            elif answer == 'agree_med':
                traits[q.trait_agree.title] = traits.get(q.trait_agree.title, 0) + 2
                print("agree med", q.trait_agree.title, traits[q.trait_agree.title])
            elif answer == 'agree_min':
                traits[q.trait_agree.title] = traits.get(q.trait_agree.title, 0) + 1
                print("agree min", q.trait_agree.title, traits[q.trait_agree.title])
            elif answer == 'neutral':
                print("neutral")
            elif answer == 'disagree_min':
                traits[q.trait_disagree.title] = traits.get(q.trait_disagree.title, 0) + 1
                print("disagree min", q.trait_disagree.title, traits[q.trait_disagree.title])
            elif answer == 'disagree_med':
                traits[q.trait_disagree.title] = traits.get(q.trait_disagree.title, 0) + 2
                print("disagree med", q.trait_disagree.title, traits[q.trait_disagree.title])
            elif answer == 'disagree_max':
                traits[q.trait_disagree.title] = traits.get(q.trait_disagree.title, 0) + 3
                print("disagree max", q.trait_disagree.title, traits[q.trait_disagree.title])
            else:
                print('else')

        analyzed_mbti = get_mbti(traits).lower()

        request.session['email'] = email
        user.mbti = Mbti.objects.filter(mbti__contains=analyzed_mbti)[0]
        user.save()
        return redirect('home')
    else:
        questions = Question.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'mbti_test3.html', context)


class AccountSettings(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'account-settings.html')


class AllCharacterAPIView(APIView):
    def get(self, request, format=None):
        try:
            all_characters = Character.objects.all().order_by('name')[:10]
            data = []
            for character in all_characters:
                data.append({
                    'name': character.name,
                    'title': character.title,
                    'mbti': character.mbti.mbti,
                    'category': character.category.title,
                    'cover': character.cover.url if character.cover else None,
                    'description': character.description,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SingleCharacterAPIView(APIView):
    def get(self, request, format=None):
        try:
            character_name = request.GET['character_name']
            characters = Character.objects.filter(name__contains=character_name)
            serialized_data = serializers.SingleCharacterSerializer(characters, many=True)
            data = serialized_data.data
            return Response({'data': data}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SearchCharacterAPIView(APIView):
    def get(self, request, format=None):
        try:
            from django.db.models import Q
            query = request.GET['query']
            characters = Character.objects.filter(Q(description__icontains=query))
            data = []
            for character in characters:
                data.append({
                    'name': character.name,
                    'title': character.title,
                    'mbti': character.mbti.mbti,
                    'category': character.category.title,
                    'cover': character.cover.url if character.cover else None,
                    'description': character.description,
                    'isFemale': character.isFemale,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubmitCharacterAPIView(APIView):
    def post(self, request, format=None):
        try:
            serializer = serializers.SubmitCharacterSerializer(data=request.data)
            if serializer.is_valid():
                name = serializer.data.get('name')
                title = serializer.data.get('title')
                cover = request.FILES.get('cover')
                description = serializer.data.get('description')
                category_id = serializer.data.get('category_id')
                isFemale = serializer.data.get('isFemale')
                mbti = serializer.data.get('mbti')
            else:
                return Response({'status': 'Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)

            category = Category.objects.get(id=category_id)

            character = Character()
            character.name = name
            character.title = title
            character.cover = cover
            character.description = description
            character.category = category
            character.isFemale = isFemale
            character.mbti = Mbti.objects.filter(mbti__contains=mbti)[0]
            character.save()
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateCharacterAPIView(APIView):
    def post(self, request, format=None):
        try:
            serializer = serializers.UpdateCharacterCoverSerializer(data=request.data)
            if serializer.is_valid():
                character_id = serializer.data.get('character_id')
                cover = request.FILES['cover']
            else:
                return Response({'status': 'Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)
            # Character.objects.filter(id=character_id).update(cover=cover)
            character = Character.objects.filter(id=character_id)[0]
            character.cover = cover
            character.save()
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteCharacterAPIView(APIView):
    def post(self, request, format=None):
        try:
            serializer = serializers.DeleteCharacterSerializer(data=request.data)
            if serializer.is_valid():
                character_id = serializer.data.get('character_id')
            else:
                return Response({'status': 'Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)
            Character.objects.filter(id=character_id).delete()
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

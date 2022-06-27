from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Phrases
from .models import Word
from .forms import PhraseForm
from .forms import WordForm
from django.http import HttpResponseRedirect


# Create your views here.


def home(request):
    return render(request, 'Flashcards/home.html')


def all_phrases(request):
    phrase_dict = Phrases.objects.all()
    """
    #li = []
    #(li.append(phrase_dict))
    """
    return phrase_dict


def all_words(request):
    word_dict = Word.objects.all()
    """
    #li = []
    #(li.append(phrase_dict))
    """
    return word_dict


def free_for_all(request):
    """
    Combines the words and phrases in the database to provide a mix of phrases
    and words in the test

    :param request:
    :return:
    """
    free_all = all_words(request) + all_phrases(request)
    """
    #li = []
    #(li.append(phrase_dict))
    """
    return free_all


def add_phrase(request):
    """
    This is currently running when a user accesses the add phrase screen and submits a new phrase.
    Should be called add_phrase
    :param request:
    :return:
    """
    submitted = False

    if request.method == "POST":
        form = PhraseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = PhraseForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'Flashcards/add_phrase.html', {'form': form, 'submitted': submitted})


def add_word(request):
    """
    This is runs when a user accesses the add words page and submits a new word

    :param request:
    :return:
    """
    submitted = False

    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = WordForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'Flashcards/add_word.html', {'form': form, 'submitted': submitted})


def phrases(request):
    all_items = all_phrases(request)
    eng_lis = []
    french_lis = []
    tense_lis = []

    for item in all_items:
        eng_lis.append(item.English)
        french_lis.append(item.French)
        tense_lis.append(item.Tenses)

    num = random.randint(0, len(eng_lis) - 1)

    if request.method == "POST":
        answer = str(request.POST['answer']).upper()
        correct_answer = str(request.POST['correct']).upper()
        correct_answer_low = str(request.POST['correct'])
        old_answer = str(request.POST['correct'])
        old_question = str(request.POST['question'])
        tense_old = 'Tense(s): ' + str(request.POST['Tenses'])

        if correct_answer in answer:
            my_answer = "Correct!"
            result = old_question + " = " + old_answer
            color = "success"

        else:
            my_answer = "Incorrect! " + old_question + " != " + request.POST['answer']
            result = old_question + " = " + correct_answer_low
            color = "danger"

        return render(request, 'Flashcards/phrases.html', {'answer': answer, 'color': color,
                                                           'tense_old': tense_old,
                                                           'my_answer': my_answer,
                                                           'result': result,
                                                           'French': french_lis[num],
                                                           'English': eng_lis[num],
                                                           'Tenses': tense_lis[num]})

    return render(request, 'Flashcards/phrases.html', {'French': french_lis[num], 'English': eng_lis[num],
                                                       'Tenses': tense_lis[num]
                                                       })


def words(request):
    all_items = all_words(request)
    eng_lis = []
    french_lis = []
    tense_lis = []

    for item in all_items:
        eng_lis.append(item.English)
        french_lis.append(item.French)
        tense_lis.append(item.Tenses)

    num = random.randint(0, len(eng_lis) - 1)

    if request.method == "POST":
        answer = str(request.POST['answer']).upper()
        correct_answer = str(request.POST['correct']).upper()
        correct_answer_low = str(request.POST['correct'])
        old_answer = str(request.POST['correct'])
        old_question = str(request.POST['question'])
        tense_old = 'Tense(s): ' + str(request.POST['Tenses'])

        if answer in correct_answer:
            my_answer = "Correct!"
            result = old_question + " = " + old_answer
            color = "success"

        else:
            my_answer = "Incorrect! " + old_question + " != " + request.POST['answer']
            result = old_question + " = " + correct_answer_low
            color = "danger"

        return render(request, 'Flashcards/words.html', {'answer': answer, 'color': color,
                                                           'tense_old': tense_old,
                                                           'my_answer': my_answer,
                                                           'result': result,
                                                           'French': french_lis[num],
                                                           'English': eng_lis[num],
                                                           'Tenses': tense_lis[num]})

    return render(request, 'Flashcards/words.html', {'French': french_lis[num], 'English': eng_lis[num],
                                                       'Tenses': tense_lis[num]
                                                       })


def free(request):
    all_items_phrases = all_phrases(request)
    all_items_word = all_words(request)
    eng_lis = []
    french_lis = []
    tense_lis = []

    for item in all_items_phrases:
        eng_lis.append(item.English)
        french_lis.append(item.French)
        tense_lis.append(item.Tenses)
    for item in all_items_word:
        eng_lis.append(item.English)
        french_lis.append(item.French)
        tense_lis.append(item.Tenses)

    num = random.randint(0, len(eng_lis) - 1)

    if request.method == "POST":
        answer = str(request.POST['answer']).upper()
        correct_answer = str(request.POST['correct']).upper()
        correct_answer_low = str(request.POST['correct']).upper()
        old_answer = str(request.POST['correct'])
        old_question = str(request.POST['question'])

        if correct_answer in answer:
            my_answer = "Correct!"
            result = old_question + " = " + old_answer
            color = "success"
        else:
            my_answer = "Incorrect! " + old_question + " != " + request.POST['answer']
            result = old_question + " = " + correct_answer_low
            color = "danger"

        return render(request, 'Flashcards/free.html', {'answer': answer, 'color': color,
                                                         'my_answer': my_answer,
                                                         'result': result,
                                                         'French': french_lis[num],
                                                         'English': eng_lis[num]})

    return render(request, 'Flashcards/free.html', {'French': french_lis[num], 'English': eng_lis[num]
                                                     })


def glossary(request):
    return render(request, 'Flashcards/glossary.html')


def about(request):
    return render(request, 'Flashcards/about.html')

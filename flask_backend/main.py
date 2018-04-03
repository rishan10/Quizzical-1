import logging
from flask import Flask, jsonify
from google.cloud import vision
from google.cloud.vision import types as typesImg
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types as typesLang
from operator import itemgetter
from aylienapiclient import textapi
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import pyrebase
import requests
import os
import json
import random


def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    client = vision.ImageAnnotatorClient()
    image = typesImg.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    s = texts[0].description.replace('\n', ' ')
    return s


def detect_document_uri(uri):
    """Detects document features in the file located in Google Cloud
    Storage."""
    client = vision.ImageAnnotatorClient()
    image = typesImg.Image()
    image.source.image_uri = uri

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    s = ""

    for page in document.pages:
        for block in page.blocks:
            block_words = []

            blockText = ""
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols:
                        blockText += symbol.text
                    blockText += " "
                block_words.extend(paragraph.words)

            if (len(blockText) >= 50):
                s += blockText
    return s


def getText():
    config = {
        "apiKey": "AIzaSyB3WoePm0O8LlMH5iRozX-TbgPjIo-XJJ8",
        "authDomain": "quizzical-1.firebaseapp.com",
        "databaseURL": "https://quizzical-1.firebaseio.com",
        "projectId": "quizzical-1",
        "storageBucket": "quizzical-1.appspot.com",
        "messagingSenderId": "549005474865"
    }
    firebase = pyrebase.initialize_app(config)

    storage = firebase.storage()
    url = storage.child("images/image.png").get_url(None)
    fullText = detect_document_uri(url)

    return fullText


def simple_get(url):
    """
    Attempts to get the content at url by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def getAnswerChoices(queryString):
    query = queryString
    raw_html = simple_get("https://www.google.com/search?q=" + query + "&cad=h")

    raw_html = raw_html[raw_html.find("People also search for".encode()):]

    html = BeautifulSoup(raw_html, 'html.parser')
    # print("\n\n\n\n")
    # print(html)
    mydivs = html.find_all("a", class_="fl")
    # otherD = html.find_all("div", class_="czonVc")

    choices = []

    for i in range(len(mydivs)):
        if i >= 3:
            break
        if "..." not in mydivs[i].text:
            choices.append(str(mydivs[i].text))
            # print(str(mydivs[i].text))

    return choices


getAnswerChoices('Special Relativity')

# # Instantiates a client
# client = language.LanguageServiceClient()

# # The text to analyze
# text = u'Hello, world!'
# document = types.Document(
#     content=text,
#     type=enums.Document.Type.PLAIN_TEXT)

# # Detects the sentiment of the text
# sentiment = client.analyze_sentiment(document=document).document_sentiment

# print('Text: {}'.format(text))
# print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

"""Detects entities in the text."""


def getQuestionData(text):
    client = language.LanguageServiceClient()

    sumClient = textapi.Client("f6d9958d", "0814f897ec695d115d91055bb53d7cfa")

    # textString = 'At a time when European kingdoms were beginning to establish new trade routes and colonies, motivated by imperialism and economic competition, Columbus proposed to reach the East Indies (South and Southeast Asia) by sailing westward. This eventually received the support of the Spanish Crown, which saw a chance to enter the spice trade with Asia through this new route. During his first voyage in 1492, he reached the New World instead of arriving in Japan as he had intended, landing on an island in the Bahamas archipelago that he named San Salvador. Over the course of three more voyages, he visited the Greater and Lesser Antilles, as well as the Caribbean coast of Venezuela and Central America, claiming all of it for the Crown of Castile. Though preceded by short-lived Norse colonization of North America led by Leif Erikson in the 11th century,[5][6] Columbus is the European explorer credited with establishing and documenting routes to the Americas, securing lasting European ties to the Americas, and inaugurating a period of exploration, conquest, and colonization that lasted for centuries. His exertions thereby strongly contributed to the development of the modern Western world. He also founded the transatlantic slave trade and has been accused by several historians of initiating the genocide of the Hispaniola natives. Columbus himself saw his accomplishments primarily in the light of spreading the Catholic religion.[7] Columbus had set course in hopes of finding a western route to the Indies (Asia). He called the inhabitants of the lands that he visited indios Spanish for Indians. His strained relationship with the Spanish crown and its appointed colonial administrators in America led to his arrest and dismissal as governor of the settlements on the island of Hispaniola in 1500, and later to protracted litigation over the benefits that he and his heirs claimed were owed to them by the crown.'

    textString = text

    document = typesLang.Document(
        content=textString,
        type=enums.Document.Type.PLAIN_TEXT)
    allEntities = client.analyze_entities(document).entities

    # textString = "DEVELOPMENT OF THE ECONOMIC THEORY OF VALUE Because economic activity has been a central feature of all societies, it is surprising that these activities were not studied in any detail until recently. For the most part, economic phenomena were treated as a basic aspect of human behavior that was not sufficiently interesting to deserve specific attention. It is, of course, true that individuals have always studied economic activities with a view toward making some kind of personal gain. Roman traders were not above making profits on their transactions. But investigations into the basic nature of these activities did not begin in any depth until the eighteenth century.3 Because this book is about economic theory as it stands today, rather than the history of economic thought, our discussion of the evolution of economic theory will be brief. Only one area of economic study will be examined in its historical setting: the theory of value. Early economic thoughts on value The theory of value, not surprisingly, concerns the determinants of the “value” of a commodity. This subject is at the center of modern microeconomic theory and is closely intertwined with the fundamental economic problem of allocating scarce resources to alternative uses. The logical place to start is with a definition of the word “value.” Unfortunately, the meaning of this term has not been consistent throughout the development of the subject. Today we regard value as being synonymous with the price of a commodity.4 Earlier philosopher-economists, however, made a distinction between the market price of a commodity and its value. The term “value” was then thought of as being, in some sense, synonymous with “importance,” “essentiality,” or (at times) “godliness.” Because “price” and “value” were separate concepts, they could differ, and most early economic discussions centered on these divergences. For example, St. Thomas Aquinas believed value to be divinely determined. Since prices were set by humans, it was possible for the price of a commodity to differ from its value. A person accused of charging a price in excess of a good’s value was guilty of charging an “unjust” price. For example, St. Thomas believed the “just” rate of interest to be zero. Any lender who demanded a payment for the use of money was charging an unjust price and could be—and sometimes was—prosecuted by church officials. The founding of modern economics During the latter part of the eighteenth century, philosophers began to take a more scientific approach to economic questions. The 1776 publication of The Wealth of Nations by Adam Smith (1723–1790) is generally considered the beginning of modern economics. In his vast, all-encompassing work, Smith laid the foundation for thinking about market forces in an ordered and systematic way. Still, Smith and his immediate successors, such as David Ricardo (1772–1823), continued to distinguish between value and price. To Smith, for example, the value of a commodity meant its “value in use,” whereas the price represented its “value in exchange.” The distinction between these two concepts was illustrated by the famous waterdiamond paradox. Water, which obviously has great value in use, has little value in exchange (it has a low price); diamonds are of little practical use but have a great value in exchange. The paradox with which early economists struggled derives from the observation that some very useful items have low prices whereas certain nonessential items have high prices."
    # summary = client.Summarize({"text": "At a time when European kingdoms were beginning to establish new trade routes and colonies, motivated by imperialism and economic competition, Columbus proposed to reach the East Indies (South and Southeast Asia) by sailing westward. This eventually received the support of the Spanish Crown, which saw a chance to enter the spice trade with Asia through this new route. During his first voyage in 1492, he reached the New World instead of arriving in Japan as he had intended, landing on an island in the Bahamas archipelago that he named San Salvador. Over the course of three more voyages, he visited the Greater and Lesser Antilles, as well as the Caribbean coast of Venezuela and Central America, claiming all of it for the Crown of Castile. Though preceded by short-lived Norse colonization of North America led by Leif Erikson in the 11th century,[5][6] Columbus is the European explorer credited with establishing and documenting routes to the Americas, securing lasting European ties to the Americas, and inaugurating a period of exploration, conquest, and colonization that lasted for centuries. His exertions thereby strongly contributed to the development of the modern Western world. He also founded the transatlantic slave trade and has been accused by several historians of initiating the genocide of the Hispaniola natives. Columbus himself saw his accomplishments primarily in the light of spreading the Catholic religion.[7] Columbus had set course in hopes of finding a western route to the Indies (Asia). He called the inhabitants of the lands that he visited indios Spanish for Indians. His strained relationship with the Spanish crown and its appointed colonial administrators in America led to his arrest and dismissal as governor of the settlements on the island of Hispaniola in 1500, and later to protracted litigation over the benefits that he and his heirs claimed were owed to them by the crown."})

    # sentiment = sumClient.Summarize({'text': textString, 'title': 'Title', 'sentences_percentage': 25}) #sentences_number': 10})
    sentiment = sumClient.Summarize(
        {'text': textString, 'title': 'Title', 'sentences_number': 10})

    summary = "";

    for element in sentiment['sentences']:
        # print (element + "\n")
        summary = summary + " " + element

    text = summary

    # Instantiates a plain text document.
    document = typesLang.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    list1 = []

    sentSentences = client.analyze_sentiment(document).sentences

    for i in sentSentences:
        list1.append(i.text.content)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities

    # entity types from enums.Entity.Type
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')
    noun_type = ('TYPE_UNKNOWN', 'PROPER', 'COMMON')

    entries = entities  # sorted(entities, key=lambda entities: entities.salience, reverse=True)

    sentenceEntities = []
    scores = []
    questions = []
    answers = []
    choices = {}
    fullObject = {}
    optimalWord = ""

    # for entity in entries:
    #     print('=' * 20)
    #     print(u'{:<16}: {}'.format('name', entity.name))
    #     print(u'{:<16}: {}'.format('type', entity_type[entity.type]))
    #     print(u'{:<16}: {}'.format('salience', entity.salience))

    # print(summary)
    # print("\n\n")

    count = 0

    for sentence in list1:
        count += 1
        sentenceEntities = []
        scores = []
        for word in entries:
            if word.name in sentence:
                sentenceEntities.append(word)
                scores.append(-1)
        if len(scores) == 0:
            continue
        for i in range(len(sentenceEntities)):
            score = 0
            e = sentenceEntities[i]
            if noun_type[e.mentions[0].type] == 'PROPER':
                score += 2
            else:
                score += 1
            score += e.salience
            if entity_type[e.type] != 'UNKNOWN':
                score += 1
            scores[i] = score

        maxEntity = sentenceEntities[scores.index(max(scores))]
        maxWord = sentenceEntities[scores.index(max(scores))].name
        answers.append(maxWord)
        # index = sentence.find(maxWord)
        # print("\n" + maxWord + "\n" + sentence[:index] + " ____ " + sentence[index + len(maxWord) + 1:])
        options = []
        # for allE in allEntities:
        #     if entity_type[allE.type] == entity_type[maxEntity.type] and noun_type[allE.mentions[0].type] == noun_type[maxEntity.mentions[0].type]:
        #         options.append(allE)

        options.sort(key=lambda x: x.salience, reverse=True)
        count = 0
        inChoices = False
        choices = {}
        choices[maxWord] = []

        choices[maxWord] = getAnswerChoices(maxWord)

        if not choices[maxWord]:
            for o in allEntities:
                if count >= 3:
                    break
                if entity_type[o.type] == entity_type[maxEntity.type] and \
                                noun_type[o.mentions[0].type] == noun_type[
                            maxEntity.mentions[0].type]:
                    for c in choices[maxWord]:
                        if (o.name.lower() == c.lower()):
                            inChoices = True
                            break
                    if o.name.lower() != maxWord.lower() and not inChoices:
                        choices[maxWord].append(o.name)
                        count += 1

        count = len(choices[maxWord])
        if count < 3:
            for o in allEntities:
                if count >= 3:
                    break
                if entity_type[o.type] == entity_type[maxEntity.type]:
                    for c in choices[maxWord]:
                        if (o.name.lower() == c.lower()):
                            inChoices = True
                            break
                if o.name.lower() != maxWord.lower() and not inChoices:
                    choices[maxWord].append(o.name)
                    count += 1

        count = len(choices[maxWord])
        if count < 3:
            for o in allEntities:
                if count >= 3:
                    break
                if noun_type[o.mentions[0].type] == noun_type[
                    maxEntity.mentions[0].type]:
                    for c in choices[maxWord]:
                        if (o.name.lower() == c.lower()):
                            inChoices = True
                            break
                if o.name.lower() != maxWord.lower() and not inChoices:
                    choices[maxWord].append(o.name)
                    count += 1

        index = sentence.find(maxWord)
        question = sentence[:index] + " ____ " + sentence[
                                                 index + len(maxWord) + 1:]
        questions.append(question)

        fullObject[question] = choices

    sentenceEntities = []
    scores = []
    score = 0

    # for k, v in fullObject.items():
    #     print(k + " ")
    #     print(v)
    #     print("\n")

    for word in entries:
        if noun_type[word.mentions[0].type] == 'PROPER':
            score += word.salience

            if entity_type[word.type] != 'UNKNOWN' and entity_type[
                word.type] != 'OTHER':
                score += 1

            sentenceEntities.append(word)
            scores.append(score)

    numMCQ = len(questions)

    if len(scores) > 0 and len(sentenceEntities) > 0:
        sortedEntities = [list(x) for x in zip(
            *sorted(zip(scores, sentenceEntities), key=itemgetter(0)))][1]
        lim = int(0.15 * len(sortedEntities))
        for i in range(lim):
            maxEntity = sortedEntities[i]
            if entity_type[maxEntity.type] == 'LOCATION':
                questions.append("What happened in the " + maxEntity.name + "?")
                answers.append("Free Response - Location")
            if entity_type[maxEntity.type] == 'EVENT':
                questions.append(
                    "What happened during the " + maxEntity.name + "?")
                answers.append("Free Response - Event")
            if entity_type[maxEntity.type] == 'PERSON':
                questions.append(
                    "What is the importance of " + maxEntity.name + "?")
                answers.append("Free Response - Person")

    # for entity in entries:
    #     for s in list1:
    #         index = s.find(entity.name)
    #         if index != -1:
    #             questions.append(s[:index] + " ____ " + s[index + len(entity.name) + 1:])
    #             answers.append(entity.name)
    #             list1.remove(s)
    #             break

    # PRINTING QUESTIONS W ANSWERS
    # for i in range(len(questions)):
    #     print(str(i+1) + ". " + questions[i] + "\n Answer: " + answers[i] + "\n")

    data = []
    for i in range(len(questions)):
        if i < numMCQ:
            data.append({"Question": questions[i], "Correct": answers[i],
                         "Answers": fullObject[questions[i]][
                             answers[i]]})  # answer_choices[i]})
        else:
            data.append({"Question": questions[i], "Correct": answers[i],
                         "Answers": ["", "", ""]})

    return data


"""Detects entities in the text."""
client = language.LanguageServiceClient()

questions = []
correct_answers = []
answer_choices = []


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def getBiggestNumber(arr):
    # ASSUMES ARR IS NOT EMPTY
    maxAnswer = arr[0]

    for answer in arr:
        if (len(answer) > len(maxAnswer)):
            maxAnswer = answer

    return maxAnswer


def generateQuestion(sentence, answer):
    # document2 = types.Document(
    # content=sentence,
    # type=enums.Document.Type.PLAIN_TEXT)

    # raw_words = client.analyze_syntax(document2).tokens


    # words = []

    # for word in raw_words:
    #     try:
    #         word_token = word.text.content
    #         words.append(word_token)

    #     except Exception:
    #         continue

    # realQuestion = ""

    # for word in words:
    #     if word == answer:
    #         realQuestion += " ____ "
    #     if word == '\'':
    #         realQuestion += word
    #     else:
    #         realQuestion += word + " "

    index = sentence.find(answer)
    realQuestion = sentence[:index] + " ____ " + sentence[
                                                 index + len(answer) + 1:]

    return realQuestion


def generateNumericalAnswerChoices(correct_answer):
    mcanswers = []

    num = int(correct_answer)
    lowerbound = num + 1
    upperbound = num + 11

    for i in range(0, 3):
        randomNum = random.randint(lowerbound, upperbound)
        while (str(randomNum) in mcanswers):
            randomNum = random.randint(lowerbound, upperbound)
        mcanswers.append(str(randomNum))

    return mcanswers


def fillAnswerChoices(correct_answers):
    answer_choices = []
    for answer in correct_answers:
        answer_choices.append(generateNumericalAnswerChoices(answer))
    return answer_choices


def QandA(text):
    questions = []
    correct_answers = []
    answer_choices = []
    document = typesLang.Document(content=text,
                                  type=enums.Document.Type.PLAIN_TEXT)

    raw_sentences = client.analyze_syntax(document).sentences
    sentences = []

    for sentence in raw_sentences:
        try:
            sentence_token = sentence.text.content
            sentences.append(sentence_token)

        except Exception:
            continue

    for sentence in sentences:
        document2 = typesLang.Document(
            content=sentence,
            type=enums.Document.Type.PLAIN_TEXT)

        words = client.analyze_syntax(document2).tokens

        tempWords = []
        for word in words:
            token = word.text.content
            if RepresentsInt(token):
                tempWords.append(token)
        if (len(tempWords) is not 0):
            correctAnswer = getBiggestNumber(tempWords)
            question = generateQuestion(sentence, correctAnswer)
            correct_answers.append(correctAnswer)
            questions.append(question)

        answer_choices = fillAnswerChoices(correct_answers)

    data = []
    for i in range(len(questions)):
        data.append({"Question": questions[i], "Correct": correct_answers[i],
                     "Answers": answer_choices[i]})

    return data


def generateQuestions(testString):
    numData = QandA(testString)
    mcData = getQuestionData(testString)
    data = numData + mcData
    return data


app = Flask(__name__)


@app.route('/')
def main():
    text = getText()
    print(text)
    questions = generateQuestions(text)
    return jsonify(questions)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
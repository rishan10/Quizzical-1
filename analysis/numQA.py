from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json
import random

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
	#ASSUMES ARR IS NOT EMPTY
	maxAnswer = arr[0]

	for answer in arr:
		if(len(answer) > len(maxAnswer)):
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
    realQuestion = sentence[:index] + " ____ " + sentence[index + len(answer) + 1:]

    return realQuestion



def generateNumericalAnswerChoices(correct_answer):
	mcanswers = []

	num = int(correct_answer)
	lowerbound = num + 1
	upperbound = num + 11

	for i in range(0,3):
		randomNum = random.randint(lowerbound, upperbound)
		while (str(randomNum) in mcanswers):
			randomNum = random.randint(lowerbound, upperbound)
		mcanswers.append(str(randomNum))

	return mcanswers

def fillAnswerChoices(correct_answers):
	for answer in correct_answers:
		answer_choices.append(generateNumericalAnswerChoices(answer))


def QandA(text):
    document = types.Document(
        content=text,
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
        document2 = types.Document(
            content=sentence,
            type=enums.Document.Type.PLAIN_TEXT) 

        words = client.analyze_syntax(document2).tokens

        tempWords = []
        for word in words:
            token = word.text.content
            if RepresentsInt(token):
                tempWords.append(token)
        if(len(tempWords) is not 0):
            correctAnswer = getBiggestNumber(tempWords)
            question = generateQuestion(sentence, correctAnswer)
            correct_answers.append(correctAnswer)
            questions.append(question)

    fillAnswerChoices(correct_answers)

    data = []
    for i in range(len(questions)):
        data.append({"Question": questions[i], "Correct": correct_answers[i], "Answers": answer_choices[i]})
    
    return data
	
			


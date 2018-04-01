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

# def isFront(sentence, answer):
# 	document = types.Document(
#     content=sentence,
#     type=enums.Document.Type.PLAIN_TEXT) 

# 	words = client.analyze_syntax(document).tokens

# 	return (words[0] == answer)

# def isBack(sentence, answer):
# 	document = types.Document(
#     content=sentence,
#     type=enums.Document.Type.PLAIN_TEXT) 

# 	words = client.analyze_syntax(document).tokens

# 	return (words[len(words)-1] == answer)

def generateQuestion(sentence, answer):
	document2 = types.Document(
    content=sentence,
    type=enums.Document.Type.PLAIN_TEXT) 

	raw_words = client.analyze_syntax(document2).tokens


	words = []

	for word in raw_words:
		try:
			word_token = word.text.content
			words.append(word_token)

		except Exception:
			continue

	realQuestion = ""

	for word in words:
		if word == answer:
			realQuestion+="--- "
		else:
			realQuestion += word + " "

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
	#text = "World War II (1939-1945) was the largest armed conflict in human history. Ranging over six continents and all the world's oceans, the war caused an estimated 50 million military and civilian deaths, including those of 6 million Jews. Global in scale and in its repercussions, World War II created a new world at home and abroad. Among its major results were the beginning of the nuclear era, increased pressure to decolonize the Third World, and the advent of the Cold War. The war also ended America's relative isolation from the rest of the world and resulted in the creation of the United Nations. Domestically, the war ended the Great Depression as hundreds of thousands of people, many of them women, went into the defense industries. At the same time, African Americans made significant strides toward achieving their political, economic and social rights. The roots of World War II, which eventually pitted Germany, Japan, and Italy (the Axis) against the United States, Great Britain and the Soviet Union (the Allies), lay in the militaristic ideologies and expansionist policies of Nazi Germany, Italy, and Japan. The weak response of the European democracies to fascist aggression and American isolationism allowed the Axis powers to gain the upper hand initially. Although the war began with Nazi Germany's attack on Poland in September 1939, the United States did not enter the war until after the Japanese bombed the American fleet in Pearl Harbor, Hawaii, on December 7, 1941. Between those two events, President Franklin Roosevelt worked hard to prepare Americans for a conflict that he regarded as inevitable. In November 1939, he persuaded Congress to repeal the arms embargo provisions of the neutrality law so that arms could be sold to France and Britain. After the fall of France in the spring of June 1940, he pushed for a major military buildup and began providing aid in the form of Lend-Lease to Britain, which now stood alone against the Axis powers. America, he declared, must become the great arsenal of democracy. From then on, America's capacity to produce hundreds of thousands of tanks, airplanes, and ships for itself and its allies proved a crucial factor in Allied success, as did the fierce resistance of the Soviet Union, which had joined the war in June 1941 after being attacked by Germany. The brilliance of America's military leaders, including General Dwight D. Eisenhower, who planned and led the attack against the Nazis in Western Europe, and General Douglas MacArthur and Fleet Admiral Chester Nimitz, who led the Allied effort in the Pacific, also contributed to the Allied victory. Among the war's major turning points for the United States were the Battle of Midway (1942), the invasion of Italy (1943), the Allied invasion of France (1944), the battle of Leyte Gulf (1944) and the dropping of the atomic bombs on Japan (1945). The war ended with the Axis powers' unconditional surrender in 1945. ER had played an unprecedented role in the planning and implementation of New Deal programs. Although she was not in a position to take an active role in the day-to-day planning and prosecution of the war, she found other ways to exercise her influence. She served briefly as assistant director of the Office of Civilian Defense, but found that by serving in an official position she created so much controversy that it harmed the agency, and she resigned. At FDR's behest she undertook two major tours, one to Europe (1942) and one to the South Pacific (1943), where she met with Allied servicemen and wartime leaders, providing comfort and boosting morale. Her major concerns, however, were with refugees, the advancement of civil rights and social programs, and the home front. She worked tirelessly to get refugees, especially Jews, out of Europe, encouraging and aiding the work of relief organizations such as the Emergency Rescue Committee and the Children's Crusade for Children, and pushing FDR and other members of his government to do more. Her efforts were often frustrated, but she did not give up and continued to pursue this work after the war when it was easier for refugees to leave Europe. On the home front, she visited defense plants around the country and used her My Day column and speeches to encourage the war effort. She continued to champion civil rights and civil liberties arguing that America could not simultaneously fight racism abroad and tolerate it at home. The painful sacrifices of war would be pointless if America did not achieve equality and justice for all its citizens. Thanks to her efforts, opportunities for African Americans in the military, including opportunities to engage in combat, were expanded significantly. ER was also directly responsible for ending segregation in military recreational areas and transportation services. Together with NAACP Executive Secretary Walter White and African American union leader A. Philip Randolph, she persuaded Franklin D. Roosevelt to issue an executive order in 1941 prohibiting racial discrimination in defense industries and establishing the Fair Employment Practices Commission. Always an advocate for women, ER championed their right to work in war-related industries and strongly encouraged women to do so. She was instrumental in starting social programs such as day-care centers and community laundries to lighten the domestic burdens of the women workers. After the war, ER supported the right of women to remain in their jobs if they depended on their wages. ER also continued to support labor and its right to organize despite opposition from Congress, business, and the public, and her insistence on the importance of postwar planning was reflected in FDR's call for a G.I. Bill of Rights."


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

	for i in range(0, len(questions)):
		print(str(i+1) + ". " + questions[i])
		print("Answer: " + correct_answers[i])
		for j in range(0,3):
			print("Choice: " + answer_choices[i][j])



	
			



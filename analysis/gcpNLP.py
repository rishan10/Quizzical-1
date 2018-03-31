# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from aylienapiclient import textapi
import json


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
client = language.LanguageServiceClient()

sumClient = textapi.Client("f6d9958d", "0814f897ec695d115d91055bb53d7cfa")

#textString = 'At a time when European kingdoms were beginning to establish new trade routes and colonies, motivated by imperialism and economic competition, Columbus proposed to reach the East Indies (South and Southeast Asia) by sailing westward. This eventually received the support of the Spanish Crown, which saw a chance to enter the spice trade with Asia through this new route. During his first voyage in 1492, he reached the New World instead of arriving in Japan as he had intended, landing on an island in the Bahamas archipelago that he named San Salvador. Over the course of three more voyages, he visited the Greater and Lesser Antilles, as well as the Caribbean coast of Venezuela and Central America, claiming all of it for the Crown of Castile. Though preceded by short-lived Norse colonization of North America led by Leif Erikson in the 11th century,[5][6] Columbus is the European explorer credited with establishing and documenting routes to the Americas, securing lasting European ties to the Americas, and inaugurating a period of exploration, conquest, and colonization that lasted for centuries. His exertions thereby strongly contributed to the development of the modern Western world. He also founded the transatlantic slave trade and has been accused by several historians of initiating the genocide of the Hispaniola natives. Columbus himself saw his accomplishments primarily in the light of spreading the Catholic religion.[7] Columbus had set course in hopes of finding a western route to the Indies (Asia). He called the inhabitants of the lands that he visited indios Spanish for Indians. His strained relationship with the Spanish crown and its appointed colonial administrators in America led to his arrest and dismissal as governor of the settlements on the island of Hispaniola in 1500, and later to protracted litigation over the benefits that he and his heirs claimed were owed to them by the crown.'
physicsString = 'Special relativity is the theory developed by Albert Einstein in 1905 to explain the observed fact that the speed of light is a constant regardless of the direction or velocity of one’s motion. Einstein laid down two simple postulates to explain this strange fact, and, in the process, derived a number of results that are even stranger. According to his theory, time slows down for objects moving at near light speeds, and the objects themselves become shorter and heavier. The wild feat of imagination that is special relativity has since been confirmed by experiment and now plays an important role in astronomical observation. The Michelson-Morley Experiment As we discussed in the chapter on waves, all waves travel through a medium: sound travels through air, ripples travel across water, etc. Near the end of the nineteenth century, physicists were still perplexed as to what sort of medium light travels through. The most popular answer at the time was that there is some sort of invisible ether through which light travels. In 1879, Albert Michelson and Edward Morley made a very precise measurement to determine at what speed the Earth is moving relative to the ether. If the Earth is moving through the ether, they reasoned, the speed of light should be slightly different when hitting the Earth head-on than when hitting the Earth perpendicularly. To their surprise, the speed of light was the same in both directions. For people who believed that light must travel through an ether, the result of the Michelson-Morley experiment was like taking a ride in a boat and discovering that the boat crossed the wave crests at the same rate when it was driving against the waves as when it was driving in the same direction as the waves. No one was sure what to make of the Michelson-Morley experiment until 1905, when Albert Einstein offered the two basic postulates of special relativity and changed forever the way we think about space and time. He asked all sorts of unconventional questions, such as, “What would I see if I were traveling at the speed of light?” and came up with all sorts of unconventional answers that experiment has since more or less confirmed. The Basic Postulates of Special Relativity Special relativity is founded upon two basic postulates, one a holdover from Newtonian mechanics and the other a seeming consequence of the Michelson-Morley experiment. As we shall see, these two postulates combined lead to some pretty counterintuitive results. First Postulate The laws of physics are the same in all inertial reference frames. An inertial reference frame is one where Newton’s First Law, the law of inertia, holds. That means that if two reference frames are moving relative to one another at a constant velocity, the laws of physics in one are the same as in the other. You may have experienced this at a train station when the train is moving. Because the train is moving at a slow, steady velocity, it looks from a passenger’s point of view that the station is moving backward, whereas for someone standing on the platform, it looks as if the train is moving forward. Einstein’s first postulate tells us that neither the passenger on the train nor the person on the platform is wrong. It’s just as correct to say that the train is still and the Earth is moving as it is to say that the Earth is still and the train is moving. Any inertial reference frame is as good as any other. Second Postulate The speed of light in a vacuum is a constant— m/s—in every reference frame, regardless of the motion of the observer or the source of the light. This postulate goes against everything we’ve learned about vector addition. According to the principles of vector addition, if I am in a car moving at 20 m/s and collide with a wall, the wall will be moving at 20 m/s relative to me. If I am in a car moving at 20 m/s and collide with a car coming at me at 30 m/s, the other car will be moving at 50 m/s relative to me. By contrast, the second postulate says that, if I’m standing still, I will measure light to be moving at m/s, or c, relative to me, and if I’m moving toward the source of light at one half of the speed of light, I will still observe the light to be moving at c relative to me. By following out the consequences of this postulate—a postulate supported by the Michelson-Morley experiment—we can derive all the peculiar results of special relativity. Time Dilation One of the most famous consequences of relativity is time dilation: time slows down at high speeds. However, it’s important to understand exactly what this means. One of the consequences of the first postulate of special relativity is that there is no such thing as absolute speed: a person on a train is just as correct in saying that the platform is moving backward as a person on the platform is in saying that the train is moving forward. Further, both the person on the train and the person on the platform are in inertial reference frames, meaning that all the laws of physics are totally normal. Two people on a moving train can play table tennis without having to account for the motion of the train. The point of time dilation is that, if you are moving relative to me in a very highspeed train at one-half the speed of light, it will appear to me that time is moving slower on board the train. On board the train, you will feel like time is moving at its normal speed. Further, because you will observe me moving at one-half the speed of light relative to you, you will think time is going more slowly for me. What does this all mean? Time is relative. There is no absolute clock to say whether I am right or you are right. All the observations I make in my reference frame will be totally consistent, and so will yours. We can express time dilation mathematically. If I were carrying a stopwatch and measured a time interval, , you would get a different measure, t, for the amount of time I had the stopwatch running. The relation between these measures is: So suppose I am moving at one-half the speed of light relative to you. If I measure 10 seconds on my stopwatch, you will measure the same time interval to be: This equation has noticeable effects only at near light speeds. The difference between t and is only a factor of . This factor—which comes up so frequently in special relativity that it has been given its own symbol, —is very close to 1 unless v is a significant fraction of c. You don’t observe things on a train moving at a slower rate, since even on the fastest trains in the world, time slows down by only about 0.00005%. Time Dilation and Simultaneity Normally, we would think that if two events occur at the same time, they occur at the same time for all observers, regardless of where they are. However, because time can speed up or slow down depending on your reference frame, two events that may appear simultaneous to one observer may not appear simultaneous to another. In other words, special relativity challenges the idea of absolute simultaneity of events. EXAMPLE A spaceship of alien sports enthusiasts passes by the Earth at a speed of 0.8c, watching the final minute of a basketball game as they zoom by. Though the clock on Earth measures a minute left of play, how long do the aliens think the game lasts? Because the Earth is moving at such a high speed relative to the alien spaceship, time appears to move slower on Earth from the aliens’ vantage point. To be precise, a minute of Earth time seems to last: Length Contraction Not only would you observe time moving more slowly on a train moving relative to you at half the speed of light, you would also observe the train itself becoming shorter. The length of an object, , contracts in the direction of motion to a length when observed from a reference frame moving relative to that object at a speed v. EXAMPLE You measure a train at rest to have a length of 100 m and width of 5 m. When you observe this train traveling at 0.6c (it’s a very fast train), what is its length? What is its width? WHAT IS ITS LENGTH? We can determine the length of the train using the equation above: WHAT IS ITS WIDTH? The width of the train remains at 5 m, since length contraction only works in the direction of motion. Addition of Velocities If you observe a person traveling in a car at 20 m/s, and throwing a baseball out the window in the direction of the car’s motion at a speed of 10 m/s, you will observe the baseball to be moving at 30 m/s. However, things don’t quite work this way at relativistic speeds.'
textString = "'World War II (1939-1945) was the largest armed conflict in human history. Ranging over six continents and all the world's oceans, the war caused an estimated 50 million military and civilian deaths, including those of 6 million Jews. Global in scale and in its repercussions, World War II created a new world at home and abroad. Among its major results were the beginning of the nuclear era, increased pressure to decolonize the Third World, and the advent of the Cold War. The war also ended America's relative isolation from the rest of the world and resulted in the creation of the United Nations. Domestically, the war ended the Great Depression as hundreds of thousands of people, many of them women, went into the defense industries. At the same time, African Americans made significant strides toward achieving their political, economic and social rights. The roots of World War II, which eventually pitted Germany, Japan, and Italy (the Axis) against the United States, Great Britain and the Soviet Union (the Allies), lay in the militaristic ideologies and expansionist policies of Nazi Germany, Italy, and Japan. The weak response of the European democracies to fascist aggression and American isolationism allowed the Axis powers to gain the upper hand initially. Although the war began with Nazi Germany's attack on Poland in September 1939, the United States did not enter the war until after the Japanese bombed the American fleet in Pearl Harbor, Hawaii, on December 7, 1941. Between those two events, President Franklin Roosevelt worked hard to prepare Americans for a conflict that he regarded as inevitable. In November 1939, he persuaded Congress to repeal the arms embargo provisions of the neutrality law so that arms could be sold to France and Britain. After the fall of France in the spring of June 1940, he pushed for a major military buildup and began providing aid in the form of Lend-Lease to Britain, which now stood alone against the Axis powers. America, he declared, must become the great arsenal of democracy. From then on, America's capacity to produce hundreds of thousands of tanks, airplanes, and ships for itself and its allies proved a crucial factor in Allied success, as did the fierce resistance of the Soviet Union, which had joined the war in June 1941 after being attacked by Germany. The brilliance of America's military leaders, including General Dwight D. Eisenhower, who planned and led the attack against the Nazis in Western Europe, and General Douglas MacArthur and Fleet Admiral Chester Nimitz, who led the Allied effort in the Pacific, also contributed to the Allied victory. Among the war's major turning points for the United States were the Battle of Midway (1942), the invasion of Italy (1943), the Allied invasion of France (1944), the battle of Leyte Gulf (1944) and the dropping of the atomic bombs on Japan (1945). The war ended with the Axis powers' unconditional surrender in 1945. ER had played an unprecedented role in the planning and implementation of New Deal programs. Although she was not in a position to take an active role in the day-to-day planning and prosecution of the war, she found other ways to exercise her influence. She served briefly as assistant director of the Office of Civilian Defense, but found that by serving in an official position she created so much controversy that it harmed the agency, and she resigned. At FDR's behest she undertook two major tours, one to Europe (1942) and one to the South Pacific (1943), where she met with Allied servicemen and wartime leaders, providing comfort and boosting morale. Her major concerns, however, were with refugees, the advancement of civil rights and social programs, and the home front. She worked tirelessly to get refugees, especially Jews, out of Europe, encouraging and aiding the work of relief organizations such as the Emergency Rescue Committee and the Children's Crusade for Children, and pushing FDR and other members of his government to do more. Her efforts were often frustrated, but she did not give up and continued to pursue this work after the war when it was easier for refugees to leave Europe. On the home front, she visited defense plants around the country and used her My Day column and speeches to encourage the war effort. She continued to champion civil rights and civil liberties arguing that America could not simultaneously fight racism abroad and tolerate it at home. The painful sacrifices of war would be pointless if America did not achieve equality and justice for all its citizens. Thanks to her efforts, opportunities for African Americans in the military, including opportunities to engage in combat, were expanded significantly. ER was also directly responsible for ending segregation in military recreational areas and transportation services. Together with NAACP Executive Secretary Walter White and African American union leader A. Philip Randolph, she persuaded Franklin D. Roosevelt to issue an executive order in 1941 prohibiting racial discrimination in defense industries and establishing the Fair Employment Practices Commission. Always an advocate for women, ER championed their right to work in war-related industries and strongly encouraged women to do so. She was instrumental in starting social programs such as day-care centers and community laundries to lighten the domestic burdens of the women workers. After the war, ER supported the right of women to remain in their jobs if they depended on their wages. ER also continued to support labor and its right to organize despite opposition from Congress, business, and the public, and her insistence on the importance of postwar planning was reflected in FDR's call for a G.I. Bill of Rights.'"
#summary = client.Summarize({"text": "At a time when European kingdoms were beginning to establish new trade routes and colonies, motivated by imperialism and economic competition, Columbus proposed to reach the East Indies (South and Southeast Asia) by sailing westward. This eventually received the support of the Spanish Crown, which saw a chance to enter the spice trade with Asia through this new route. During his first voyage in 1492, he reached the New World instead of arriving in Japan as he had intended, landing on an island in the Bahamas archipelago that he named San Salvador. Over the course of three more voyages, he visited the Greater and Lesser Antilles, as well as the Caribbean coast of Venezuela and Central America, claiming all of it for the Crown of Castile. Though preceded by short-lived Norse colonization of North America led by Leif Erikson in the 11th century,[5][6] Columbus is the European explorer credited with establishing and documenting routes to the Americas, securing lasting European ties to the Americas, and inaugurating a period of exploration, conquest, and colonization that lasted for centuries. His exertions thereby strongly contributed to the development of the modern Western world. He also founded the transatlantic slave trade and has been accused by several historians of initiating the genocide of the Hispaniola natives. Columbus himself saw his accomplishments primarily in the light of spreading the Catholic religion.[7] Columbus had set course in hopes of finding a western route to the Indies (Asia). He called the inhabitants of the lands that he visited indios Spanish for Indians. His strained relationship with the Spanish crown and its appointed colonial administrators in America led to his arrest and dismissal as governor of the settlements on the island of Hispaniola in 1500, and later to protracted litigation over the benefits that he and his heirs claimed were owed to them by the crown."})
sentiment = sumClient.Summarize({'text': textString, 'title': 'Title', 'sentences_number': 10})

summary = "";

for element in sentiment['sentences']:
    # print (element + "\n")
    summary = summary + " " + element

text = summary

list1 = text.split('.')

# Instantiates a plain text document.
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects entities in the document. You can also analyze HTML with:
#   document.type == enums.Document.Type.HTML
entities = client.analyze_entities(document).entities

# entity types from enums.Entity.Type
entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')
noun_type = ('TYPE_UNKNOWN', 'PROPER', 'COMMON')

entries = entities #sorted(entities, key=lambda entities: entities.salience, reverse=True)

sentenceEntities = []
scores = []
questions = []
answers = []
optimalWord = ""

for entity in entries:
    print('=' * 20)
    print(u'{:<16}: {}'.format('name', entity.name))
    print(u'{:<16}: {}'.format('type', entity_type[entity.type]))
    print(u'{:<16}: {}'.format('salience', entity.salience))

print(summary)
print("\n\n")


for sentence in list1:
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
        if entity_type[e.type] != 'UNKNOWN' or entity_type[e.type] != 'OTHER':
            score += 1
        scores[i] = score
    
    maxWord = sentenceEntities[scores.index(max(scores))].name
    answers.append(maxWord)
    index = sentence.find(maxWord)
    questions.append(sentence[:index] + " ____ " + sentence[index + len(maxWord) + 1:])

# for entity in entries:
#     for s in list1:
#         index = s.find(entity.name)
#         if index != -1:
#             questions.append(s[:index] + " ____ " + s[index + len(entity.name) + 1:])
#             answers.append(entity.name)
#             list1.remove(s)
#             break

# PRINTING QUESTIONS W ANSWERS            
for i in range(len(questions)):
    print(str(i+1) + ". " + questions[i] + "\n Answer: " + answers[i] + "\n")

# for entity in entries:
#     print('=' * 20)
#     print(u'{:<16}: {}'.format('name', entity.name))
#     print(u'{:<16}: {}'.format('type', entity_type[entity.type]))
#     print(u'{:<16}: {}'.format('metadata', entity.metadata))
#     print(u'{:<16}: {}'.format('salience', entity.salience))
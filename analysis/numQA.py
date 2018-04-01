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

    


physicsString = 'Special relativity is the theory developed by Albert Einstein in 1905 to explain the observed fact that the speed of light is a constant regardless of the direction or velocity of one’s motion. Einstein laid down two simple postulates to explain this strange fact, and, in the process, derived a number of results that are even stranger. According to his theory, time slows down for objects moving at near light speeds, and the objects themselves become shorter and heavier. The wild feat of imagination that is special relativity has since been confirmed by experiment and now plays an important role in astronomical observation. The Michelson-Morley Experiment As we discussed in the chapter on waves, all waves travel through a medium: sound travels through air, ripples travel across water, etc. Near the end of the nineteenth century, physicists were still perplexed as to what sort of medium light travels through. The most popular answer at the time was that there is some sort of invisible ether through which light travels. In 1879, Albert Michelson and Edward Morley made a very precise measurement to determine at what speed the Earth is moving relative to the ether. If the Earth is moving through the ether, they reasoned, the speed of light should be slightly different when hitting the Earth head-on than when hitting the Earth perpendicularly. To their surprise, the speed of light was the same in both directions. For people who believed that light must travel through an ether, the result of the Michelson-Morley experiment was like taking a ride in a boat and discovering that the boat crossed the wave crests at the same rate when it was driving against the waves as when it was driving in the same direction as the waves. No one was sure what to make of the Michelson-Morley experiment until 1905, when Albert Einstein offered the two basic postulates of special relativity and changed forever the way we think about space and time. He asked all sorts of unconventional questions, such as, “What would I see if I were traveling at the speed of light?” and came up with all sorts of unconventional answers that experiment has since more or less confirmed. The Basic Postulates of Special Relativity Special relativity is founded upon two basic postulates, one a holdover from Newtonian mechanics and the other a seeming consequence of the Michelson-Morley experiment. As we shall see, these two postulates combined lead to some pretty counterintuitive results. First Postulate The laws of physics are the same in all inertial reference frames. An inertial reference frame is one where Newton’s First Law, the law of inertia, holds. That means that if two reference frames are moving relative to one another at a constant velocity, the laws of physics in one are the same as in the other. You may have experienced this at a train station when the train is moving. Because the train is moving at a slow, steady velocity, it looks from a passenger’s point of view that the station is moving backward, whereas for someone standing on the platform, it looks as if the train is moving forward. Einstein’s first postulate tells us that neither the passenger on the train nor the person on the platform is wrong. It’s just as correct to say that the train is still and the Earth is moving as it is to say that the Earth is still and the train is moving. Any inertial reference frame is as good as any other. Second Postulate The speed of light in a vacuum is a constant— m/s—in every reference frame, regardless of the motion of the observer or the source of the light. This postulate goes against everything we’ve learned about vector addition. According to the principles of vector addition, if I am in a car moving at 20 m/s and collide with a wall, the wall will be moving at 20 m/s relative to me. If I am in a car moving at 20 m/s and collide with a car coming at me at 30 m/s, the other car will be moving at 50 m/s relative to me. By contrast, the second postulate says that, if I’m standing still, I will measure light to be moving at m/s, or c, relative to me, and if I’m moving toward the source of light at one half of the speed of light, I will still observe the light to be moving at c relative to me. By following out the consequences of this postulate—a postulate supported by the Michelson-Morley experiment—we can derive all the peculiar results of special relativity. Time Dilation One of the most famous consequences of relativity is time dilation: time slows down at high speeds. However, it’s important to understand exactly what this means. One of the consequences of the first postulate of special relativity is that there is no such thing as absolute speed: a person on a train is just as correct in saying that the platform is moving backward as a person on the platform is in saying that the train is moving forward. Further, both the person on the train and the person on the platform are in inertial reference frames, meaning that all the laws of physics are totally normal. Two people on a moving train can play table tennis without having to account for the motion of the train. The point of time dilation is that, if you are moving relative to me in a very highspeed train at one-half the speed of light, it will appear to me that time is moving slower on board the train. On board the train, you will feel like time is moving at its normal speed. Further, because you will observe me moving at one-half the speed of light relative to you, you will think time is going more slowly for me. What does this all mean? Time is relative. There is no absolute clock to say whether I am right or you are right. All the observations I make in my reference frame will be totally consistent, and so will yours. We can express time dilation mathematically. If I were carrying a stopwatch and measured a time interval, , you would get a different measure, t, for the amount of time I had the stopwatch running. The relation between these measures is: So suppose I am moving at one-half the speed of light relative to you. If I measure 10 seconds on my stopwatch, you will measure the same time interval to be: This equation has noticeable effects only at near light speeds. The difference between t and is only a factor of . This factor—which comes up so frequently in special relativity that it has been given its own symbol, —is very close to 1 unless v is a significant fraction of c. You don’t observe things on a train moving at a slower rate, since even on the fastest trains in the world, time slows down by only about 0.00005%. Time Dilation and Simultaneity Normally, we would think that if two events occur at the same time, they occur at the same time for all observers, regardless of where they are. However, because time can speed up or slow down depending on your reference frame, two events that may appear simultaneous to one observer may not appear simultaneous to another. In other words, special relativity challenges the idea of absolute simultaneity of events. EXAMPLE A spaceship of alien sports enthusiasts passes by the Earth at a speed of 0.8c, watching the final minute of a basketball game as they zoom by. Though the clock on Earth measures a minute left of play, how long do the aliens think the game lasts? Because the Earth is moving at such a high speed relative to the alien spaceship, time appears to move slower on Earth from the aliens’ vantage point. To be precise, a minute of Earth time seems to last: Length Contraction Not only would you observe time moving more slowly on a train moving relative to you at half the speed of light, you would also observe the train itself becoming shorter. The length of an object, , contracts in the direction of motion to a length when observed from a reference frame moving relative to that object at a speed v. EXAMPLE You measure a train at rest to have a length of 100 m and width of 5 m. When you observe this train traveling at 0.6c (it’s a very fast train), what is its length? What is its width? WHAT IS ITS LENGTH? We can determine the length of the train using the equation above: WHAT IS ITS WIDTH? The width of the train remains at 5 m, since length contraction only works in the direction of motion. Addition of Velocities If you observe a person traveling in a car at 20 m/s, and throwing a baseball out the window in the direction of the car’s motion at a speed of 10 m/s, you will observe the baseball to be moving at 30 m/s. However, things don’t quite work this way at relativistic speeds.'
wwString = "'World War II (1939-1945) was the largest armed conflict in human history. Ranging over six continents and all the world's oceans, the war caused an estimated 50 million military and civilian deaths, including those of 6 million Jews. Global in scale and in its repercussions, World War II created a new world at home and abroad. Among its major results were the beginning of the nuclear era, increased pressure to decolonize the Third World, and the advent of the Cold War. The war also ended America's relative isolation from the rest of the world and resulted in the creation of the United Nations. Domestically, the war ended the Great Depression as hundreds of thousands of people, many of them women, went into the defense industries. At the same time, African Americans made significant strides toward achieving their political, economic and social rights. The roots of World War II, which eventually pitted Germany, Japan, and Italy (the Axis) against the United States, Great Britain and the Soviet Union (the Allies), lay in the militaristic ideologies and expansionist policies of Nazi Germany, Italy, and Japan. The weak response of the European democracies to fascist aggression and American isolationism allowed the Axis powers to gain the upper hand initially. Although the war began with Nazi Germany's attack on Poland in September 1939, the United States did not enter the war until after the Japanese bombed the American fleet in Pearl Harbor, Hawaii, on December 7, 1941. Between those two events, President Franklin Roosevelt worked hard to prepare Americans for a conflict that he regarded as inevitable. In November 1939, he persuaded Congress to repeal the arms embargo provisions of the neutrality law so that arms could be sold to France and Britain. After the fall of France in the spring of June 1940, he pushed for a major military buildup and began providing aid in the form of Lend-Lease to Britain, which now stood alone against the Axis powers. America, he declared, must become the great arsenal of democracy. From then on, America's capacity to produce hundreds of thousands of tanks, airplanes, and ships for itself and its allies proved a crucial factor in Allied success, as did the fierce resistance of the Soviet Union, which had joined the war in June 1941 after being attacked by Germany. The brilliance of America's military leaders, including General Dwight D. Eisenhower, who planned and led the attack against the Nazis in Western Europe, and General Douglas MacArthur and Fleet Admiral Chester Nimitz, who led the Allied effort in the Pacific, also contributed to the Allied victory. Among the war's major turning points for the United States were the Battle of Midway (1942), the invasion of Italy (1943), the Allied invasion of France (1944), the battle of Leyte Gulf (1944) and the dropping of the atomic bombs on Japan (1945). The war ended with the Axis powers' unconditional surrender in 1945. ER had played an unprecedented role in the planning and implementation of New Deal programs. Although she was not in a position to take an active role in the day-to-day planning and prosecution of the war, she found other ways to exercise her influence. She served briefly as assistant director of the Office of Civilian Defense, but found that by serving in an official position she created so much controversy that it harmed the agency, and she resigned. At FDR's behest she undertook two major tours, one to Europe (1942) and one to the South Pacific (1943), where she met with Allied servicemen and wartime leaders, providing comfort and boosting morale. Her major concerns, however, were with refugees, the advancement of civil rights and social programs, and the home front. She worked tirelessly to get refugees, especially Jews, out of Europe, encouraging and aiding the work of relief organizations such as the Emergency Rescue Committee and the Children's Crusade for Children, and pushing FDR and other members of his government to do more. Her efforts were often frustrated, but she did not give up and continued to pursue this work after the war when it was easier for refugees to leave Europe. On the home front, she visited defense plants around the country and used her My Day column and speeches to encourage the war effort. She continued to champion civil rights and civil liberties arguing that America could not simultaneously fight racism abroad and tolerate it at home. The painful sacrifices of war would be pointless if America did not achieve equality and justice for all its citizens. Thanks to her efforts, opportunities for African Americans in the military, including opportunities to engage in combat, were expanded significantly. ER was also directly responsible for ending segregation in military recreational areas and transportation services. Together with NAACP Executive Secretary Walter White and African American union leader A. Philip Randolph, she persuaded Franklin D. Roosevelt to issue an executive order in 1941 prohibiting racial discrimination in defense industries and establishing the Fair Employment Practices Commission. Always an advocate for women, ER championed their right to work in war-related industries and strongly encouraged women to do so. She was instrumental in starting social programs such as day-care centers and community laundries to lighten the domestic burdens of the women workers. After the war, ER supported the right of women to remain in their jobs if they depended on their wages. ER also continued to support labor and its right to organize despite opposition from Congress, business, and the public, and her insistence on the importance of postwar planning was reflected in FDR's call for a G.I. Bill of Rights.'"
sales = "Salesforce is a leading provider of enterprise software, delivered through the cloud, with a focus on customer relationship management, or CRM. We introduced our first CRM solution in 2000, and we have since expanded our service offerings into new areas and industries with new editions, features and platform capabilities. Our core mission is to empower our customers to connect with their customers in entirely new ways through cloud, mobile, social, Internet of Things (“IoT”) and artificial intelligence technologies. Our service offerings are intuitive and easy to use. They can be deployed rapidly, configured easily and integrated with other platforms and enterprise applications, or apps. We deliver our service offerings via major internet browsers and on leading mobile devices. We sell to businesses of all sizes and in almost every industry worldwide on a subscription basis, primarily through our direct sales efforts and also indirectly through partners. Through our platform and other developer tools, we also encourage third parties to develop additional functionality and new apps that run on our platform, which are sold separately from, or in conjunction with, our service offerings. 3 Our Customer Success Platform is a comprehensive portfolio of service offerings providing sales force automation, customer service and support, marketing automation, digital commerce, community management, analytics, application development, IoT integration, collaborative productivity tools and our professional cloud services. Salesforce also believes in giving back. We pioneered, and have inspired other companies to adopt, an integrated philanthropy model called the 1-1-1 model, which leverages 1% of a company’s equity, employee time and product to help improve communities around the world. We also believe in equality for all, and have spearheaded initiatives to create a world where equal pay, equal advancement, equal opportunity and equal rights become a reality for our employees and the broader world. We were incorporated in Delaware in February 1999. Our principal executive offices are located in San Francisco, California, and our principal website address is www.salesforce.com. Our office address is The Landmark @ One Market, Suite 300, San Francisco, California 94105. The Age of the Customer At Salesforce, we believe we are living in the single most innovative era in history, as everyone and every thing becomes connected. There are now billions of mobile phones and intelligent connected devices. And behind each and every device, interaction, product and connected community is a customer. Companies have the opportunity to harness all of this information about customers in new and extraordinary ways, enabling them to intelligently connect and engage with customers across every part of the customer experience. Our Customer Success Platform provides a single view of the customer across all touchpoints. We bring together the power of cloud, mobile, social, IoT and artificial intelligence technologies, enabling our customers to harness data and deliver the connected experiences their customers are increasingly coming to expect."
kareemString = "Hall of Fame basketball center Kareem Abdul-Jabbar is the NBA's all-time leading scorer. He won six NBA titles, five with the Los Angeles Lakers, over 20 years. Kareem Abdul-Jabbar Biography Kareem Abdul-Jabbar was born in New York City in 1947. A dominant high school basketball player, Abdul-Jabbar was recruited to play at UCLA and led the Bruins to three national titles. His dominance continued in the NBA, first for the Milwaukee Bucks, and later the Los Angeles Lakers. Abdul-Jabbar won six titles and six MVP awards, and finished as the league's all-time scorer. He retired in 1989 and is widely considered one of the greatest players in NBA history, and his talent was celebrated as early as high school. Lew Alcindor Kareem Abdul-Jabbar was born Ferdinand Lewis Alcindor Jr. on April 16, 1947, in New York City. The only son of Ferdinand Lewis Alcindor Sr., a New York City policeman, and his wife, Cora, Alcindor was always the tallest kid in his class. Known as Lew Alcindor, by the age of nine he stood an impressive 5'8\", and by the time he hit eighth grade, he'd grown another full foot and could already dunk a basketball. He started playing the sport at an early age. At Power Memorial Academy, Alcindor put together a high school career few could rival. He set New York City school records in scoring and rebounds, while simultaneously leading his team to an astonishing 71 consecutive wins and three straight city titles. In 2000 the National Sports Writers dubbed Alcindor's team \"The #1 High School Team of the Century.\" Kareem Abdul-Jabbar Height Kareem Abdul-Jabbar is 7'2\" tall. John Wooden After graduating in 1965, Alcindor enrolled at the University of California-Los Angeles. There, he continued his unprecedented dominance, becoming the college game's best player. Under legendary coach John Wooden, Alcindor led the Bruins to three national championships from 1967 to 1969 and was named the National Collegiate Athletic Association (NCAA) Tournament's Most Outstanding Player for those years. Milwaukee Bucks In the spring of 1969 the Milwaukee Bucks, in only their second year of existence, selected Alcindor with the first overall pick in the NBA draft. Alcindor quickly adjusted to the pro game. He finished second in the league in scoring and third in rebounding, and was named Rookie of the Year. He also helped dramatically change the fortunes of his franchise. Coming off a dismal 27-win season the year before, the retooled Bucks, with Alcindor manning the basket, improved to 56-26. The following season the Bucks, having added future Hall of Fame guard Oscar Robertson to their roster, made another huge leap. The team finished the regular season 66-16 and then steamrolled through the playoffs, sweeping the Baltimore Bullets in the 1971 NBA finals. That same year Alcindor won his first Most Valuable Player award, the first of six MVP honors he received during his long career. Conversion to Islam Shortly after the 1971 season ended, Alcindor converted to Islam and adopted the name Kareem Abdul-Jabbar, which translates into noble, powerful servant. In 1974, Abdul-Jabbar again led the Bucks to the NBA finals, where the team lost to the Boston Celtics. Los Angeles Lakers Even with all his on-the-court success as a Buck, Abdul-Jabbar struggled to find happiness off the court in his life in Milwaukee. \"Live in Milwaukee?\" he said in an early magazine interview. \"No, I guess you could say I exist in Milwaukee. I am a soldier hired for service and I will perform that service well. Basketball has given me a good life, but this town has nothing to do with my roots. There's no common ground.\" Following the end of the 1975 season, Abdul-Jabbar demanded a trade, requesting Bucks management send him to either New York or Los Angeles. He was eventually shipped west for a package of players, none of whom came close to delivering for Milwaukee what Abdul-Jabbar would give the Lakers. Over the next 15 seasons Abdul-Jabbar turned Los Angeles into a perennial winner. Beginning with the 1979-80 season, when he was paired with rookie point guard Earvin \"Magic\" Johnson, the dominant center propelled the Lakers to five league titles. His signature jump shot, the skyhook, came to be an unstoppable offensive weapon for Abdul-Jabbar, and the Lakers enjoyed championship dominance over Julius \"Dr. J\" Erving's Philadelphia 76ers, Larry Bird's Boston Celtics and Isiah Thomas' Detroit Pistons. Hollywood Calls His success on the court led to some acting opportunities. Abdul-Jabbar appeared in several films, including the 1979 martial-arts film Game of Death and the 1980 comedy Airplane! Even as he aged, the health-conscious Abdul-Jabbar remained in remarkable shape. Well into his 30s, he still managed to average more than 20 points a game. By his late 30s, he was still playing around 35 minutes a game. In the 1985 finals against the Boston Celtics, which the Lakers won in six games, the 38-year-old Abdul-Jabbar was named the series MVP. Kareem Abdul-Jabbar Stats When Abdul-Jabbar retired in 1989, he was the NBA's all-time leading scorer, with 38,387 points, and became the first NBA player to play for 20 seasons. His career totals included 17,440 rebounds, 3, 189 blocks and 1,560 games. He also broke records for having scored the most points, blocked the most shots and won the most MVP titles in 1989. Years after his retirement, Abdul-Jabbar seemed especially proud about his longevity. The '80s made up for all the abuse I took during the '70s, he told the Orange County Register. I outlived all my critics. By the time I retired, everybody saw me as a venerable institution. Things do change. Post-Playing Life Since his retirement, Abdul-Jabbar hasn't strayed too far from the game he loves, working for the New York Knicks and the Los Angeles Lakers. He even spent a year as a coach on the White Mountain Apache reservation in Arizona—an experience that he recorded in the 2000 book A Season on the Reservation. He has written several other books, including 2007's On the Shoulders of Giants, about the Harlem Renaissance. Abdul-Jabbar has also worked as a public speaker and a spokesperson for several products. In 1995 Abdul-Jabbar was elected to the Naismith Memorial Basketball Hall of Fame. In November 2009 Abdul-Jabbar was diagnosed with a rare form of leukemia, but his long-term prognosis looked favorable. In February 2011, doctors declared the retired NBA star cancer free. Abdul-Jabbar was named a 2016 recipient of the Presidential Medal of Freedom, presented by Barack Obama. A father of five, Abdul-Jabbar has four children from his first marriage to Habiba Abdul-Jabbar and a son from another relationship."


QandA(wwString)
	
			


import nltk as nltk

__author__ = 'Abduljaleel'

from twitter import *
import time
from pymongo import *


#Access the twitter app
CON_key = 'c2zHl8hyYPcnRcqtjchJZwMb5'
CON_secret = 'u0i3NYcO6nZNn8JjT5cc7PDwEZMMfnRU9jewZ68eqA9qlqHLhw'
ACCESS_key = '61739184-EBxmw8OxMtOKWGXyE2Tvx9mioTOzy5FF22xld0QV6'
ACCESS_secret = '8tuGKkfaJBGsONt8UQrhx37f2RsbwD28UJrCKdRvgaSzw'

# connecting to MongoDB

# connection = Connection()
# database = connection.heartdia
# t_mongo = database.hd

# states = ' Alabama Alaska Arizona Arkansas California Colorado Connecticut Delaware Florida Georgia Hawaii' \
#          ' Idaho Illinois Indiana Iowa Kansas Kentucky Louisiana Maine Maryland Massachusetts Michigan' \
#          ' Minnesota Mississippi Missouri Montana Nebraska Nevada Hampshire Jersey York Carolina Dakota Ohio' \
#          ' Oklahoma Oregon Pennsylvania Rhode Tennessee Texas Utah Vermont Virginia Washington Wisconsin,Wyoming' \
#          ' District Puerto Guam American AL AK AZ AR CA CO CT FL GA HI ID IL IA KS KY ME MD MA DE' \
#          ' MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK PA RI SC SD TN TX UT VT VA DC' \
#          ' WA WV WI WY USA U.S.A. states america chicago nyc philadelphia miami angeles houston phoenix dallas austin' \
#          ' jacksonville indianapolis fransisco columbus charlotte detroit memphis seattle denver boston nashville davidson' \
#          ' baltimore oklahoma louisville portland milwaukee albuquerque tucson fresno sacramento atlanta omaha raleigh' \
#          ' oakland minneapolis tulsa cleveland wichita arlington'

# api = Twitter(auth=OAuth(ACCESS_key, ACCESS_secret, CON_key, CON_secret))
pp = TwitterStream(auth=OAuth(ACCESS_key, ACCESS_secret, CON_key, CON_secret))
# tt = '"diseases of heart", "heart diseases", heart disease, "coronary artery disease", heart failure, "heart attack",' \
#      '"acute coronary", angina, "atrial fibrillation", "atrial fib", arrhythmias, "atherosclerotic cardiovascular",' \
#      '"congenital heart", "peripheral arterial disease","pericardial", "myocardial infarction", endocarditis, pericardium,' \
#      'myocarditis, diabetes, diabetic'
# tt = '"diseases of heart", "heart diseases", heart disease, "coronary artery disease", heart failure, "heart attack",' \
#      '"acute coronary", angina, "atrial fibrillation", "atrial fib", arrhythmias, "atherosclerotic cardiovascular",' \
#      '"congenital heart", "peripheral arterial disease","pericardial", "myocardial infarction", endocarditis, pericardium,' \
#      ' myocarditis, malignant, cancer, copd, asthma, bronchitis, emphysema, "chronic obstructive pulmonary", "lower respiratory",' \
#      ' stroke, "brain attack", cerebrovascular, alzheimer, diabetes, diabetic, influenza, pneumonia, flu, nephritis, nephrotic,' \
#      ' nephrosis, renal failure, kidney disorder, kidney failure, kidney disease, septicemia, blood poisoning, bacteraemia,' \
#      ' bacteremia, sepsis, chronic liver disease, cirrhosis, liver cirrhosis, hypertension, hypertensive, high blood pressure,' \
#      ' parkinson, "paralysis agitans", "shaking palsy", pneumonitis, "aspiration pneumonia", "pulmonary aspiration",' \
#      ' "inhalation pneumonia", "endotracheal aspiration", "cardiac arrest", "congestive heart", "heart block", CHD, IHD,' \
#      ' CAD, tumor, malignancy, D.M, H1N1, H5N1, bronchopneumonia, ESRD, "end stage renal", "dialysis"'
tt = "t-mobile"
# twit = t_mongo.find()
# n=0
# print twit.count()

while True:
    try:
        for tweets in pp.statuses.filter(track=tt):
            text = tweets['text']
            print text
            # if text!='' and text!=None:
            #     t_mongo.insert(tweets)
            #     print text
            # n+=1
            # if n % 100 == 0:
            #     print n
            # print ['user']['location']
            # if 'lang' in tweets:
            #     text = tweets['lang']
            #     if text!=None:
            #         loc = tweets['user']['location']
            #         if (loc != None) and (loc != ''):
            #             print text +'.......'+ loc + '...'+ tweets['text']
            #             t_mongo.insert(tweets)
            #             n+=1
            #             if n % 100 == 0:
            #                 print n
            #         else:
            #             if 'coordinates' in tweets:
            #                 cor = tweets['coordinates']
            #                 if cor != None:
            #                     print text +'.......'+ str(cor)
            #                     t_mongo.insert(tweets)
            #                     n+=1
            #                     if n % 100 == 0:
            #                         print n
    except Exception as e:
        print 'PLEASE WAIT'
        time.sleep(14)

'''''
twit = t_mongo.find()
print twit.count() # or t_mongo.coun()

number = 1
for row in twit:
    print str(number) + "......" + row['text'] + "....." + row['created_at']
    number += 1





# geolocator = Nominatim()
# while True:
#     try:
#         for tweet in pp.statuses.filter(track=tt):
#             # print 'TEXT = ' + tweet['text']
#             if 'user' in tweet:
#                 #print tweet['user']
#                 location = tweet['user']['location']
#                 # print 'location = '+location
#                 loc = location.split(' ')
#
#
#                 found = False
#                 for tt in loc:
#                     if tt != '':
#                         tt = tt+' '
#                         if tt.lower() in states.lower():
#                             print "United States"
#                             found = True
#                             break
#
#                 if (location != '') and (found==False):
#                     try:
#                         nn = nn+1
#                         print nn
#                         print 'location = '+location
#
#                         location = geolocator.geocode(location)
#                         print(location.address)
#                     except Exception as e:
#                         #print location
#                         print 'address in invalid'
#
#                         #
#                         #
#                         # tt = tweet['coordinates']
#                         # if (tt):
#                         #     print 'coordinates = ' + str(tweet['coordinates'])
#
#                 print '-------------------------'
#             else:
#                 print "no user"
#
#     except Exception as e:
#         print 'SOMTHING HAPPENED'

'''''


import nltk

#We have to create a function resulting the following:
pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive')]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative')]


tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))



def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words
#func1
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

#func2
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


#call func1 and func2
word_features = get_word_features()
#we will get the results from functions #1 & #2 as word_features


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
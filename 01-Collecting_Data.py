__author__ = 'Abduljaleel'

from twitter import *
import time
from geopy.geocoders import Nominatim


'''
geolocator = Nominatim()
location = geolocator.geocode("miami")
print(location.address)


'''

#Access the twitter app
CON_key = 'c2zHl8hyYPcnRcqtjchJZwMb5'
CON_secret = 'u0i3NYcO6nZNn8JjT5cc7PDwEZMMfnRU9jewZ68eqA9qlqHLhw'
ACCESS_key = '61739184-EBxmw8OxMtOKWGXyE2Tvx9mioTOzy5FF22xld0QV6'
ACCESS_secret = '8tuGKkfaJBGsONt8UQrhx37f2RsbwD28UJrCKdRvgaSzw'

# states = ' Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii,' \
#          ' Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan,' \
#          ' Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, Hampshire, Jersey, York,' \
#          ' Carolina, Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode,' \
#          ' Tennessee, Texas, Utah, Vermont, Virginia, Washington, Wisconsin, Wyoming, District,' \
#          ' Puerto, Guam, American, AL AK AZ AR CA CO CT DE FL GA' \
#          ' HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA ' \
#          ' WA WV WI WY USA U.S.A. united states america chicago nyc philadelphia miami angeles houston phoenix dallas austin' \
#          ' jacksonville indianapolis fransisco columbus charlotte detroit memphis seattle denver boston nashville davidson' \
#          ' baltimore oklahoma louisville portland milwaukee albuquerque tucson fresno sacramento atlanta omaha raleigh' \
#          ' oakland minneapolis tulsa cleveland wichita arlington'

api = Twitter(auth=OAuth(ACCESS_key, ACCESS_secret, CON_key, CON_secret))
# m=0
# maxid=0
# n=0
# try:
#     search_result = api.search.tweets(q="google", count=100, max_id=0)
#     for tweet in search_result['statuses']:
#         print str(tweet['id']) + '....' + str(tweet['created_at'])
#         if (n==99):
#             maxid=tweet['id']
#         n = n+1
# except Exception as e:
#     print 'rate limit!!!!!!'
#     time.sleep(1)
#
# m=m+100
# print m
# print maxid

while(True):
    try:
        search2 = api.search.tweets(track=['Verizon'])
        n=0
        for tweet in search2['statuses']:
            print str(tweet['user']['screen_name']) + '....' + str(tweet['created_at']) + tweet['text']
            # if (n==99):
            maxid=tweet['id']
            # n = n+1
        m=m+100
        print m
    except Exception as e:
        print 'rate limit!!!!!!'
        time.sleep(1)



    # location =  tweet['user']['location']
    # loc = location.split(' ')
    # print loc
    #
    # for tt in loc:
    #     if tt != '':
    #         if tt.lower() in states.lower():
    #             print "United States"
    #             break

    # tt = tweet['coordinates']
    # if (tt):
    #     print tweet['coordinates']


# pp = TwitterStream(auth=OAuth(ACCESS_key, ACCESS_secret, CON_key, CON_secret))
# tt = "isis, iraq"
#
# for tweet in pp.statuses.filter(track=tt):
#     #print tweet['text']
#     #print tweet['lang']
#     print tweet['user']['location']
#     print tweet['coordinates']


result = '123 Main Street, Los Angeles, CA, 90034, USA'




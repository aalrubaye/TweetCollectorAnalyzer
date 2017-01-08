pp = TwitterStream(auth=OAuth(ACCESS_key, ACCESS_secret, CON_key, CON_secret))
tt = '"keyword 1", "keyword 2", "keyword n"'

#connecting to MongoDB
connection = Connection()
database = connection.the_name_of_your_db
t_mongo = database.the_name_of_your_collection(same_as_table_in_sql)

twit = t_mongo.find()

while True:
    try:
        for tweets in pp.statuses.filter(track=pp):
            #this line prints the entire jason
            print tweets
            #if you want to print a specific parameter of that
            print tweets['user']
            print tweets['text']
            #and so on
            #you have to learn how to navigate a tweet and retrieve a specific parameter of it
            #dev.twitter.com is the source

            #if you want to insert the data into mongo db
            t_mongo.insert(tweets)

    except Exception as e:
        print 'PLEASE WAIT, Some error happened'
        time.sleep(14)

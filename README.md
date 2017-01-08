# TweetCollectorAnalyzer

This code was mainly written to collect, filter, and analyze Health-related tweets in a short period of time to examine the existing networks of people who are suffering from diseases that lead to death in the United States.
In this code we aimed to build and analyze networks of social groups on Twitter related to the topic of certain diseases. We considered 13 health conditions that are categorized as the top leading causes of death in the United States and tracked any message that mentioned at least one of these health conditions. To define a relation between Twitter users and create a network, we used the concept of time window where the focus is on a particular period of time. In the process of reconstructing social structures related to each one of the health conditions, we assigned different lengths to a time window.

##Data filteration
after 60 days of collecting tweets, was implementing the filtration process over the dataset we stored. In order to extract those tweets 
were posted from the United States, we needed to filter them out based on the places they originated from. Initially, geocoding parameters were used to retrieve locations for the collected tweets. Geocoding is a process of describing locations based on their postal address or spatial positions as a global address. Geographic coordinates specify a set of values to indicate a particular location on the earth.

##Networks creation
In our work, the users that tweeted from the United States are considered to be the nodes and two users are connected to each other if both have mentioned the same health condition in their tweets. According to the this definition, all tweets that mentioned the same health conditions would be related to each other. Therefore, to construct a network of a specific health conditions by considering all tweets in the period of 60 days, the network would be too densely connected. In other words, for each one of the health conditions we would end up with a clique of n nodes, where n is the total number of tweets that mentioned the same disease. In this case, the generated networks would not show any interesting characteristic.

![degree_distribution](https://cloud.githubusercontent.com/assets/17988691/21747658/151e6cc0-d53c-11e6-92e8-656a0900b6e8.png)

##Time Window
In the generated networks, we can lose information if we do not define the best way of moving the time window over the data. If we consider a tweet as an event, the simplest way to shift the time window is to move it forward event by event. The second issue to overcome is selecting a length for the time-window. If the length is too large or too small, the network generated might not have useful information. A very large time window’s size results in having fully connected clusters connected to each other. In the worst case, if we assign the highest possible size to the time window, we have one big clique. Choosing a very small length may lead us to generate networks that most probably have many disconnected nodes. In order to avoid direct bias, we worked with multiple sizes in this thesis . To have
more accurate results we assigned 12 different lengths starting from 1 hour, 2 hours, 3 hours, and up to 12 hours. This means that we have twelve different networks for each one of the health conditions. The idea is to find which of these time windows yield structural information.
The idea of using a time window naturally leads to weighted networks. If two users who mentioned the same health condition are within the time window for more than one iteration of the time window, their connection gets reinforced; when two tweets are close to each other on the timeline, their users tend to have a stronger connection compared to those users who tweeted in farther periods.
![timewindow](https://cloud.githubusercontent.com/assets/17988691/21747644/cdcc8ee2-d53b-11e6-982b-335324f861a5.png)

![example](https://cloud.githubusercontent.com/assets/17988691/21747647/e3d20dfc-d53b-11e6-95c2-d559f2acaaeb.png)

##An example of extracted netwroks:
![florida_diabetes](https://cloud.githubusercontent.com/assets/17988691/21747648/e7e28a8e-d53b-11e6-876e-1da968567314.png)



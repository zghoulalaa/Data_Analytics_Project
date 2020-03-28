import numpy as np #to handle all the numbers and matrices
import pandas as pd #for reading and manipulating the data
import matplotlib.pyplot as plt #for data visualization

data = pd.read_csv('/home/alaa/Desktop/Data_Analytics/Tweets.csv')

"""
Analysis and visualization on the data will be done and presented. Pandas and matplotlib are libraries for data visualization and statistics.the code will start by showing the number of negative, positive and neutral reviews.
"""

counter = data.airline_sentiment.value_counts()
index = [1,2,3]
plt.figure(1,figsize=(12,6))
plt.bar(index,counter,color=['red','yellow','green'])
plt.xticks(index,['negative','neutral','positive'],rotation=0)
plt.xlabel('Type')
plt.ylabel('Count')
plt.title('Summery of Sentiment')
plt.show()

"""
the next part will show the numbers of each type of review for each airline.
"""

figure_2 = data.groupby(['airline', 'airline_sentiment']).size()
figure_2.unstack().plot(kind='bar', stacked=True,color=['r', 'y', 'g'])
plt.show()
print(figure_2)

"""
 It is important to know which airline pleases their costumers the most. the code will show the percentage of the negative reviews for each airline.
"""

negative_tweets = data.groupby(['airline','airline_sentiment']).count().iloc[:,0]
total_tweets = data.groupby(['airline'])['airline_sentiment'].count()

Airline_negative_percentage = {'American':negative_tweets[0] / total_tweets[0],'Delta':negative_tweets[3] / total_tweets[1],'Southwest': negative_tweets[6] / total_tweets[2],
'US Airways': negative_tweets[9] / total_tweets[3],'United': negative_tweets[12] / total_tweets[4],'Virgin': negative_tweets[15] / total_tweets[5]}
percentage = pd.DataFrame.from_dict(Airline_negative_percentage, orient = 'index')
percentage.columns = ['Negative Percentage']
print(percentage)
ax = percentage.plot(kind = 'bar', rot=0, colormap = 'Reds_r')
ax.set_xlabel('Airlines')
ax.set_ylabel('Percentage of negative tweets')
plt.show()

"""
people complain for many reasons. 10 reasons to be specific. In the next figure, the code will illustrate these reason for each airline.
"""

negative_reasons = data.groupby('airline')['negativereason'].value_counts(ascending=True)
negative_reasons.groupby(['airline','negativereason']).sum().unstack().plot(kind='bar')
plt.xlabel('Airline')
plt.ylabel('Number of Negative reasons')
plt.title("The causes of negative results for airlines")
plt.show()




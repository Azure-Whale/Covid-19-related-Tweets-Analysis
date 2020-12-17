# Covid-19-related-Tweets-Analysis
## Project Goal:
Our study aims to learn if there is any potential undiscovered symptoms that people would like to share on their social media. 
## Precedures:
Firstly, the data is gained from Twitter API which enables us to gain daily tweet. We keep crawling the data for serveral days and it reached about 200+GB data and we saved those on the internal server, I implement some common NLP techniques to clean the tweet like tokenization, removing stopping words and etc for further analysis.

Next, what we did is geting a symptoms data, I got the data from a medical dictionary of public organization. I implemented some match technique like regex to script the data from the dictionary. So now we got a full list of symptoms. After that, I use pandas to transfer collected data into dataframe and filter out our target category of symptoms.

The final step is to do a match & count in our collected tweet, and try to find most common side-effects of Covid-19 talked by people on Twitter
## Results:
By extracting and visualizing these data, we try to learn things behind these daily tweets. Here is the frequency distribution of where people mentioned Covid-19 side-effects in their tweets. The distribution vary from one side-effect to another one.

### Distribution of US
![alt text](https://github.com/Azure-Whale/Covid-19-related-Tweets-Analysis/blob/master/Images/City.png)


### Distribution of worldwide
![alt text](https://github.com/Azure-Whale/Covid-19-related-Tweets-Analysis/blob/master/Images/Country.png)

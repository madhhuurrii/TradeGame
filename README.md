# $TradeGame

## Inspiration
After the problem Statements were released in Opening ceremony, I got intrigued to Finance Domain track. Also coincdently Past week I took a Stock market Foundation course, inorder to make myself aware of Trading and Stock Market as a non-finance background student. I learned about how trading is done, and understood why new-comers leave trading abruptly after making loss. 
Which is why I thought to use this hackathon as a platform to mix up my technical and little bit finance knowledge to built a Trading Simulator called "Tradegame" YAY!! 
## What it does
TradeGame is an application  which provides a platform to user to explore how trading works and understand the basic of Stock market in general.
TradeGame offer a gamified approach to buy stock using virtual coins and oversee how stock market change in real-time.
During the course I learned on what stocks to invest and what to avoid thru Top Gainers and losers using 3rd party application called Nuvama. In TradeGame, we dont need any application as we can check ourselves what all stocks are performing well in BSE(Bombay Stock Exchange).
I also tried implementing gamified approch for eg. to buy stock using a concept of virtual coins which is provided to the user while new Registeration($ 1000 virtual coins). 
## How we built it
So first after brainstroming the possible ideas related to domain, I design wireframes on what all features to  be included in TradeGame. 
After that I started designing mockups intially so that devlopment process can also speed, and to be honest it did worked! I was worried intially I may not be able complete as design took a ample amount of time, but after designing It was  very smooth to work  with User interface using Jinja2 in flask for templating, also used html,css, bootstrap, since design was done. After implementing and setting up the database using sqlite for Login and registration. i was able to setup the database schema for the user.  
Then I tweaked around StockAPIs to collect data for Top 5 gainers and losers. I used BSEdata API for that. I used AlphaVantage for plot the intratrading stock using stock name. 
## Challenges we ran into
Since I was using Stock APIs, many APIs were paid version. 
Also AlphaVantage had 25 limit per day, so it was quite difficult to build and test application due to these limitations.(PS. I made 4-5 accounts and switched btw 2 internet connection for IP address Change lol) 
Also working alone in 24hr hackathon was also a challenge but I felt I tackled it quite well since I was able to pull of major feature which i had planned.
## Accomplishments that we're proud of
1. I was able to automate the top5 gainers and losers using the BSEdata API. So the Market statistics page give real-time data to users.
2. I was able to gamify little bit by buying stocks using virtual coins. 
3. Working alone helped me unleash my full potential.
4. Pulling of major features which i had ideated during the start of hackathon.

## What's next for TradeGame
1. To implement Sell stock option
2. To showcase Trade transactions in dashboard
3. To deploy $TradeGame as web application 

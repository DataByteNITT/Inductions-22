Topic 5 
Anonymous dataset visualization and insights
Sangames S 
107121088


Tool Used :
  As mentioned in the task I must have used RStudio or Tableau, but I started with Power BI as I have prior experience in using Power BI and because of the reason it is much similar to Tableau . I have also used python with Seaborn and Pandas libraries to visualize some graphs which are not available  in Power BI.
As I had used  Power BI and I don’t have a business account in it , I have combined the report as a pdf file and attached it. If possible I can show the dashboards in more dynamic manner during interviews or further rounds. The python file is attached is attached in .ipynb format.
Approach Used :
  Looking at the dataset , it contains various data that is required by a club to sign a player. So I have decided to go with the title “ PLAYER SCOUTING GUIDE” .

DashBoard 1 :
By looking through the dataset , the viewer must get basic spread of the data . So I have added cards in Power BI which displays the number of countries represented by the players, clubs represented by the players and the total number of players in the dataset. 
Conclusion 1: From these data , we can infer that this dataset has information of potentially all the global players and from various renowned clubs. Also the football culture is most dominant in Europe.
To represent it in a more graphical way, a world map with dots representing the number of players in that region is provided. Also to get the exact data , a matrix table ( in Power BI) is used to give the count of players from each country. 
Dashboard 2:
Going into more financial part, this dashboard contains visualizations about wage, value and age of the players. 


Conclusion from the graphs :
* From the first line graph we can infer that the wage and the value of the players have a good amount of correlation and these two features do not vary a lot for a particular overall of a player.
* From the scatter plot we can infer that the wage of a player increases exponentially with his overall rating. Also there is a wage gap between 0.2 million and 0.4 million which differentiates the elite players( high overall players) from the pack.
* From the barplot we get information about the clubs which pay more to their players. Here median wage is used as it might give an appropriate insight.
* From the 2nd line graph we infer that, stamina of the players have a tricky trend with their age and it breaks down the myth that young players have the best stamina.

DashBoard 3 :
 This dashboard gives the best players to scout for their club and some specialist in particular areas.
Conclusion and approach :
* A slicer is included to filter the players based on their position and the card beside it displays the maximum rating of the player available. 
* Also the table gives more detailed information about the top players in that particular position.
* A tree map is used to display the distribution of players with respect to various positions, which further insights us that players prefer common positions like CB , GK, ST, CM ,LB, CDM .
* A matrix table is used here to find free kick specialist, a new measure is added in Power BI FK specialist , which is the sum of the free kick accuracy, crossing  and curve. As these are the most required skills required for a free kick taker.

Heatmap ( python file )
* Heatmap is displayed here to find the common trend among various features ( columns) present in the dataset.
* From the heatmap, the features which are multicollinear with others can be dropped down.
* To plot the heatmap, first ,correlation between various features is calculated . variables which are of string type are dropped before calculating correlation.
* Features like GK diving, GK handling, GK kicking, GK positioning are correlated more and except one feature others can be dropped.
     Scatter Plot with Hue
* To get more information about nationality and the age of the players they have, a scatter plot with hue as nationality is shown.


 P.S : I have not spent enough time to design the dashboard .So please consider it. 

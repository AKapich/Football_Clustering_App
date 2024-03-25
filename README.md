# [Top 5 European Leagues Clustering App](https://clustering-top5leagues-alekskapich.streamlit.app/)

![](https://raw.githubusercontent.com/AKapich/Football_Clustering_App/main/screenshot.png)

Web app giving an ability to discover more profoundly varying play styles for various football positions.
It's based on clustering algorithm, moreover integrates OpenAI API enabling users to generate cluster analysis performed by AI.

## How to use the app?
The sidebar enables users to select analyzed position, age range for the players and threshold for minutes played in order for the players to be included in the analysis.
Then, after the clusterization takes place, every cluster can be scrutinized and players within the cluster can be compared to all the other players meeting the filtering criteria (the ones who fell into other clusters). The metrics to be displayed on the beeswarm plots can be chosen within the menu as well.

### Bonus - AI analysis
For those who own their OpenAI API key, there is an option to connect directly to ChatGPT, that is pre-set to prepare descriptive analysis of the considered cluster.

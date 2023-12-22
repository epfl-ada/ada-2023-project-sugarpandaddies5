# From Damsels to Dialogue: A Critical Examination of the Bechdel Test and Female Representation in Cinema
Find our data story [here](https://zoehud.github.io/)

## Abstract
Cinema is an art reflecting society and therefore, lays bare its inequalities, particularly concerning the portrayal of women on screen. The Bechdel Test provides a simple criterion to assess this representation in films and works of fiction. It highlights the underrepresentation of women, often relegated to secondary roles or romantic interests when they do appear in movies. The test has three criteria that a film must meet to pass: it must have at least two named female characters, these characters must have a conversation with each other, and the conversation must be about something other than a man.
Although this test appears like a bare minimum, [less than half](https://psycnet.apa.org/fulltext/2022-95091-001.html) of noteworthy films from the past 40 years have passed. Using the CMU Movie Corpus we will proceed with a critical analysis of the Bechdel test and what it truly says about female representation in cinema. 

## Research Questions
- Does the country of production and/or the genre of the film impact the likelihood of passing the Bechdel test ?
- Does the result of the test impact box office success ?
- How has the proportion of films that pass the Bechdel test changed over time ?
- What is the impact of the quantity of female characters on the result of the test ?
- Can films that uphold misogynistic character tropes still pass the test ?
- What is the impact of woman director ?
- Can we accurately predict the result of the test based only on information contained in the MCU Movie Corpus ?

## Additional Datasets
All datasets can be found in our data folder
- Bechdel Test results : dataset containing a pass/fail marker for about 10000 films.
- CPI per country : dataset giving inflation information for a range of countries. It is important to adjust box office revenue for inflation, especially considering that certain movies studied were produced over 100 years ago when money had a very different value.
- [Directors Gender](https://github.com/taubergm/HollywoodGenderData/blob/master/all_directors_gender.csv) : dataset of 5056 directors with their gender (male or female)

## Methods
### Part 1 : Data clean up and pre-processing
**Step 1.1 Merging the datasets** : The two main datasets that are used are the CMU Movie Metadata (81,741 movies), and the downloaded Bechdel results (10136 movies) (from the page https://bechdeltest.com). Merging these two tables on a relevant and unique identifier is a challenge, since they don't have the same identifiers: on one hand CMU Movies has the Wikipedia page ID, on the other hand, Bechdel table has the Imdb page IDs. To adress this, we will request Wikipedia Page IDs of movies in the Bechdel Table, by giving the title and year of the movie. The merge will then be performed on Wikipedia Page IDs.

**Step 1.2 Assumptions** : Check necessary assumptions for subsequent statistical tests : As we intend to use statistical tests and perform logistic regressions, several hypotheses need to be established. This will be done in Milestone 3.


### Part 2 : General analysis 
**Step 2.1 Time** The first vizualitions are time series: amount of movies across the years, Bechdel rate evolution, Proportion of Bechdel passing movies evolution

**Step 2.2 Revenue and budget**
We visualized the percentage of films passing the Bechdel test as a function of revenue. Using a Spearman correlation test we find a statistically significant negative correlation. In the future we aim to correct for inflation on top of this.

**Step 2.3 Country and Genre** : We found the ten most represented countries in the merged dataset, in order to have large enough samples. Then, we first look the proportion of passing Bechdel movies for each of the ten countries. The Movie genres are investigated with the same method: for each of the ten major genres, we compute the propotion of each Bechdel rate. 

### Part 3 : Critical study of the Bechdel test

**Step 3.1 Quantity of actresses** : The purpose of this step is to see whether films pass the Bechdel test because they have more actresses or, on the contrary, if the number of actresses is limited but their characters are developed. By "developed," we mean that we know their names, and they engage in conversations on topics other than men. To achieve this, we need to examine the number of actresses and actors per film as well as their ratio.

**Step 3.2 Director gender** : while women have been an integral part of the film industry since the beginning, the opportunity to direct was rarely given to them. A director's job description involves participation in nearly every phase of a project. Because their vision largely impacts the final product, it can be interesting to assess the impact of the presence of female directors. For this, we need to add a new dataset that provides the genders of film directors for each movie, we do not have the Wikipeida ID or IMDb ID for a movie, therefore we will merge this new dataset with the old one based on the title of a movie and the year it was released. We can then explore the proportion of films directed by women that pass the Bechdel test compared to films with male directos. 

**Step 3.3 Age ratio between actresses and actors**
A question of interest might be whether the average age of actresses in a given movie is lower or higher than that of actors. Therfeore, we compute the average actress age and average actor age for each movie where all age values are available. Then, we compute the ratio of the two. A ratio value below one indicated that the average actress age is below that of actors.
Secondly, we look at the ratio distribution across different ratings values, that is whether a movie passes the Bechdel test (rating = 3) or not (ratings = 0,1,2).

**Step 3.4 Presence of misogynistic tropes** : We take inspiration from Bamman O'Connor and Smith's study on [Learning Latent Personas of Film Characters](https://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman+oconnor+smith.acl13.pdf), in which they aim to predict character tropes using movie summary data. What is of interest to us is the classification into specific tropes, instead of the work of grouping characters into personas. For this, we focus on their manually collected test dataset of induced personas, based on information from [tvtropes.com](https://tvtropes.org/pmwiki/pmwiki.php/Main/Tropes) which classifies 501 characters from different movies into 72 distinct tropes such as "young gun" or "absent minded professor". To answer the question of whether films perpetrating misogynistic tropes can be just as likely to pass the Bechdel test, we proceed by adding a trope coefficient to the regression, and analysing both goodness of fit and statistical significance. Of course, we first isolate tropes which have misogynistic undertones as supported by relevant literary and cinematic studies.


### Part 4 : Prediction and determination of confounding factors
** Step 4.1 Analysis of the initial bias of the Bechdel dataset **: The dataset we refer to is constructed through contributions at [bechdeltest.com](https://bechdeltest.com/). Anyone can freely fill out a movie form indicating whether a movie has passed or failed the test along with specific information on the criteria met or missed. Users can also leave comments on movie pages if they disagree with the result assigned to a movie. We want to determine whether this database is truly a random collection of movies, or if there is some inherent bias of choice which would represent a confounding element for our analyses.

To do so, we determine a dependent variable for the CMU corpus which takes value 1 if the corresponding movie appears in the Bechdel database and 0 if not. Then, we perform a logistic regression of this variable on several factors: country, box office revenue, genre, result of the Bechdel test, release year, female presence, as well as crossfactors. Then, we execute a chi-squared test to determine dependence of the binary dependent variable. We complement with post hoc tests depending on the outcome.


**Step 4.2 Feature based prediction** : In this final part, we are going to use a supervised classification method based on the film features to predict whether a film passes the Bechdel test or not. We will construct a classification tree. We of course will divide our dataset into two or more sets for testing training and validation.

## Proposed timeline

* 17-11-23 Milestone 2 submission
* 24-11-23 Perform statistical tests between the distribution of passing and failing tests for: revenue, age ratio, number of female characters
* 01-12-23 Feature selection
* 08-12-23 Logistic regression Pass/Fail with features: director gender, quantity of actresses, genre
* 15-12-23 Machine Learning
* 22-12-23 Milestone 3 submission

## Organisation within the team
| Contributor | Tasks                     | 
|-------------|---------------------------------------------|
| **Juliette** | - Data processing, dataset merging  |
|             | - Analysis of genres, production company, and revenue         |
|             | - Card flip development                       |     
| **Zoë**     | - Website construction and datastory writing, plots  |    
|             | - Inflation analysis                          |
|             | - Interpretation of results and dataset analysis                         |
| **Anabelle** | - Study of quantity of actresses, director and writer gender             |  
|             | - Datastory writing                  | 
| **Nicola**   | - Dataframe homogenization               | 
|             | - Study of misogynistic tropes, propensity score analysis    | 
| **Thibault** |- Machine learning, feature based prediction          |   
|              |- Dataframe homogenization                                             |  




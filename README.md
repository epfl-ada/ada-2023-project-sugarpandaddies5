# From Damsels to Dialogue: A Critical Examination of the Bechdel Test and Female Representation in Cinema
## Abstract
Cinema is an art reflecting society and therefore, lays bare its inequalities, particularly concerning the portrayal of women on screen. The [Bechdel Test](https://en.wikipedia.org/wiki/Bechdel_test) provides a simple criterion to assess this representation in films and works of fiction. It highlights the underrepresentation of women, often relegated to secondary roles or romantic interests when they do appear in movies. The test has three criteria that a film must meet to pass: 
- It must have at least two named female characters. 
- These characters must have a conversation with each other. 
- The conversation must be about something other than a man 

Although this test appears like a bare minimum, [less than half](https://psycnet.apa.org/fulltext/2022-95091-001.html) of noteworthy films from the past 40 years have passed. Using the CMU Movie Corpus we will proceed with a critical analysis of the Bechdel test and what it truly says about female representation in cinema. 

## Research Questions
- Does the country of production and/or the genre of the film impact the likelihood of passing the Bechdel test ?
- Does the result of the test impact box office success ?
- How has the proportion of films that pass the Bechdel test changed over time ?
- What is the impact of the quantity of female characters on the result of the test ?
- Can films that uphold misogynistic character tropes still pass the test ?
- What is the relationship between actress age, character age, and the test ?
- Can we accurately predict the result of the test based only on information contained in the MCU Movie Corpus ?

## Additional Datasets
- Bechdel Test results : dataset containing a pass/fail marker for about 10000 films.
- CPI per country : dataset giving inflation information for a range of countries. It is important to adjust box office revenue for inflation, especially considering that certain movies studied were produced over 100 years ago when money had a very different value.
- [Directors Gender]() : dataset of 5056 directors with their gender (male or female)

## Methods
### Part 1 : Data clean up and pre-processing
**Step 1** Merging the datasets

**Step X** Assumptions

Check necessary assumptions for subsequent statistical tests

### Part 2 : General analysis 
**Step X** Time

**Step X** Revenue and budget

**Step X** Country

### Part 3 : Critical study of the Bechdel test

**Step X** Age of actresses

**Step X** Director gender

While women have been an integral part of the film industry since the beginning, the opportunity to direct was rarely given to them. A director's job description involves participation in nearly every phase of a project. Because their vision largely impacts the final product, it can be interesting to assess the impact of the presence of female directors. For this, we need to add a new dataset that provides the genders of film directors for each movie, we do not have the Wikipeida ID or IMDb ID for a movie, therefore we will merge this new dataset with the old one based on the title of a movie and the year it was released. We can then explore the proportion of films directed by women that pass the Bechdel test compared to films with male directos. 

**Step X** Presence of misogynistic tropes

We take inspiration from Bamman O'Connor and Smith's study on [Learning Latent Personas of Film Characters](https://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman+oconnor+smith.acl13.pdf), in which they aim to predict character tropes using movie summary data. What is of interest to us is the classification into specific tropes, instead of the work of grouping characters into personas. For this, we focus on their manually collected test dataset of induced personas, based on information from [tvtropes.com](https://tvtropes.org/pmwiki/pmwiki.php/Main/Tropes) which classifies 501 characters from different movies into 72 distinct tropes such as "young gun" or "absent minded professor". To answer the question of whether films perpetrating misogynistic tropes can be just as likely to pass the Bechdel test, we proceed by adding a trope coefficient to the regression, and analysing both goodness of fit and statistical significance. Of course, we first isolate tropes which have misogynistic undertones as supported by relevant literary and cinematic studies.

**Step X** Quantity of actresses

### Part 4 : Prediction and determination of confounding factors
**Step X** Analysis of the initial bias of the Bechdel dataset

The dataset we refer to is constructed through contributions at [bechdeltest.com](https://bechdeltest.com/). Anyone can freely fill out a movie form indicating whether a movie has passed or failed the test along with specific information on the criteria met or missed. Users can also leave comments on movie pages if they disagree with the result assigned to a movie. We want to determine whether this database is truly a random collection of movies, or if there is some inherent bias of choice which would represent a confounding element for our analyses.

To do so, we determine a dependent variable for the CMU corpus which takes value 1 if the corresponding movie appears in the Bechdel database and 0 if not. Then, we perform a logistic regression of this variable on several factors: country, box office revenue, genre, result of the Bechdel test, release year, female presence, as well as crossfactors. Then, we execute a chi-squared test to determine dependence of the binary dependent variable. We complement with post hoc tests depending on the outcome.


**Step X** Feature based prediction

In this final part, we are going to use a supervised classification method based on the film features to predict whether a film passes the Bechdel test or not. We will construct a classification tree.

## Proposed timeline

* 17-11-23 Milestone 2 submission
* 24-11-23 
* 01-12-23 
* 08-12-23 
* 15-12-23 
* 22-12-23 Milestone 3 submission

## Organisation within the team
| Contributor | Task                                        |
|-------------|---------------------------------------------|
| **Juliette** | - Initial data analysis and plots           |
|             | - Statistical analysis                      |
|             | - Overview of notebook                       |
| **Zoé**      | - Step X: Analysis of the initial bias of the Bechdel dataset |
|             | - Step X: Presence of misogynistic tropes   |
|             | - Overview of README                          |
| **Anabelle** | - Step X: Quantity of actresses             |
|             | - Step X: Director gender                    |
|             | - Overview of README                          |
| **Nicola**   | - Step X: Age of actresses                   |
|             | - Step X: Feature-based prediction           |
| **Thibault** |                                             |


#Question to the TA

**Step X** Age of characters vs. age of actresses
We found it relevant to compare the ages of actors and actresses with the ages of the fictional characters they portray. For example, in the film 'Eiffel,' 47-year-old Romain Duris portrays Gustave Eiffel, who is 55. Actress Emma Mackey, at 25, portrays Adrienne Bourgès, his youthful love... aged 44. There's a 9-year age difference in reality, more than double between the actors. One could criticize this film for reflecting a form of sexism as the script doesn't justify this casting choice. The issue here is that we couldn't find any dataset with the ages of characters in a film. We considered two options to address this gap: either use the Freebase ID from Wikidata to try to find ages on Wikipedia pages of characters, or look into the film summaries dataset and, with a machine learning method, find the respective ages of the characters.






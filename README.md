# AIRBNB DATA ANALYSIS - BOSTON AND SEATTLE

Airbnb is an online community marketplace that allows homeowners to list their bedrooms, apartments or their entire homes for short term lodging. It has become a global holiday phenomenon spreading to every major city in the world, as people can travel to new places and stay at ready-to-go homes at a reasonable price. As Forbes states, *in collaborative consumption, the sharing economy or the peer economy, owners rent out something they are not using, such as a car, house or bicycle to a stranger using a peer-to-peer service. The company typically has a rating or review system so people on both sides of the transaction can trust the other. With the popularity of these services, many people don't need to buy when they can rent from others*

However, despite being the poster child for the sharing economy, Airbnb also has its share of controversies. All across the world from the US to Europe and beyond, city authorities are either clamping down on Airbnb because of cases of either flouting local laws (in New York owners or tenants cannot legally rent their apartments out for short periods (less than 30 days) unless they are also living in the property), avoiding taxes, or inadvertently raising housing prices (in Berlin, Airbnb has been partly blamed for increasing rents, city officials have created a new housing law banning regular short-term letting of rooms without permission from the authorities).

![Airbnb](https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/boston.png)


This post will attempt to analyse the Airbnb data for both the cities as available on Kaggle. It will try to look for trends in prices, seasonal and by neighbourhood, availability and distribution of listings. It will also try to predict ratings for the listings based on the data available. The analyses and modelling associated with this post is included in the accompanying Jupyter notebooks

### What are we working with
We have data available on Kaggle for both Seattle and Boston. This data includes property listing details and descriptions, customer reviews and availability schedules in both cities. The original data source is the Inside Airbnb project that scrapes publicly available information from the Airbnb site.

## Overview
We have a year's data for both the cities. The data for Boston data was sourced in September, 2016 and the Seattle data in January, 2016 for a year. There are a total of 3585 Boston listings and 3818 Seattle listings. This isn't a lot of data to work with and may affect our modelling.

## Price analysis and comparison
Let's begin by looking at seasonal prices of trends in both the cities. How did prices change over the year?
<p align="center">
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Boston_seasonal_prices.png" width="420" />
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Seattle_seasonal_prices.png" width="420" />
</p>
As can be seen from the graphs above prices are highest in September and October in Boston and lowest in January and February. In Seattle, prices are highest in June, peaking in July and are lowest in January and February. This should be obvious because of the weather. Another insight that can be gleaned from here is that price bands are higher for Boston than for Seattle. The lowest avergae price in Boston is around $180 whereas that in Seattle is $120. The prices have been analysed for listings that are available in that month.

![weekly](https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/weekly_prices.png)
Now we look at weekly prices for both the cities and no surpise here, average prices go up on Friday and Saturday. Since weekend visitors must be checking in on Friday or Saturday and checking out on Sunday. The price gap between both cities is clearly evident here.

## Availability comparison
Next we will move on to seeing how availability of listings changes over the course of 2016 for both Boston and Seattle. For this analysis availability is measured as the proportion of available listings of the total listings.
<p align="center">
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Boston_availability.png" width="420" />
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Seattle_availability.png" width="420" />
</p>

The graphs above shows that in Boston, availability is lowest in the months of December, January and February (there is one dip in availability in December) and after availabiltiy rises in March, it almost plateaus till September before peaking again. In Seattle, availability is lowest in November and December. It is highest in January and then falls from January till April and then sort of plateaus from April to June and peaks mildly in July.

## Neighbourhood analysis and comparison
Onto neighbourhoods, we will look at the spread of listings by neighbourhood, their prices and also at number of listings per host distribution. We will explore them city by city since the neighbourhood denominator for the comparisons are different. This will mostly be an intra-city comparison.
## Boston
### Spread of Listings
<img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Boston_listings_by_nhood.png" width="825" height="460">
There are 25 neighbourhoods with Jamaica Plan having the highest number of listings and Leather District having the least. The most Airbnb populated neighbourhood, Jamaica Plain has 343 listings and the least has 5 listings.

### Prices
<img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Boston_prices_by_nhood.png" width="825" height="460">
Few neighbourhoods have very highly priced listings, i.e. over $1000 - South Boston, South Boston Waterfront and South End. Allston and Beacon Hill too.
Mattapan has lower prices and lesser number of units too. Bay Village, on the other hand though, has the same number of listings but has a wider range of prices. Allston, Brighton, Dorchester have most listings below $250.

<p align="center">
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Boston_avg_prices_by_nhood.png"/>
</p>
This shows the average price across neighbourhoods however this is influenced by total number of listings in that area. As in the case of Leather District, the number of listings are smaller leading to a higher average.
<p align="center">
 <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Boston_price_dist.png" width="600" height="600"/>
</p>
This is a plot showing the same average price distribution plotted spatially by neighbourhood. It also shows that average prices are higher near the bay.

### Listings per Host
<p align="center">
 <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Boston_host_listings_count.png" width="700" height="800"/>
</p>
The above figure shows the number of listings per host in Boston as spread across the city. It is evident that hosts with more than four listings are mostly centred in the city. Hosts with single listings or with 2-4 listings are spread out over the city, with the ones with a single listing having the most homogeeous spread.

## Seattle

### Spread of Listings
<p align="center">
 <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Seattle_listings_by_nhood.png" />
</p>
Broadway has the most number of listings, nearly 400. There are a lot more neighbourhoods in Seattle as can be seen from the height of this graph. Almost half the neighbourhoods have lesser than 35 listings.

### Prices
<p align="center">
 <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Seattle_prices_by_nhood.png" />
</p>
The above stripplot shows the scattering of listing prices across neighbourhoods. Belltown and Broadway have more number of listings. University District, Ravenna, Mount Baker, Loyal Heights and Greenwood have most prices lower than $200. There are only a smattering of values above $400 with the majority of listings falling under $200.

<p align="center">
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Seattle_avg_prices_by_nhood.png" />
</p>
This shows the average price across neighbourhoods however this is influenced by total number of listings in that area.
<p align="center">
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Seattle_price_dist.png" width="600" height="600" />
</p>
This is a plot showing the same average price distribution plotted spatially by neighbourhood. Sharing the same trend with Boston, average prices are higher near the bay.

### Listings per Host
<p align="center">
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Seattle_host_listings_count.png" width="700" height="800"/>
</p>
This figure shows the distribution of listings per host in Seattle. It shows the same trend as shown by the Boston data. There is concentration of hosts with more than four listings towards the city center and the hosts with single or two to four listings are more evenly spread out.

## Predict ratings for Boston listings
Now, let's look at predicting ratings for Boston listings based on the available listing details and descriptions.
## Analyze ratings
We begin by looking at the ratings available for the data that we have. Creating plots for the Boston ratings gives us -
<p align="center">
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Boston_review_scores_dist.png" />
  <br>
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Boston_review_scores_dist_wdnums.png" />
</p>
As is evident from the graphs, we have a very skewed distribution here. There are more than 800 reviews which arent rated, if we scrap that unlabeled data we will have even lesser data to work with. The plot is skewed to the higher side. There are hardly any negative reviews. Does Airbnb remove negatively listed reviews, or do the hosts remove them or is Airbnb listing reviews as very highly positive though they may not be. These arent questions we will try to answer right now, however.

We will try to bin the ratings and look -
<p align="center">
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Boston_review_scores_5bins.png" />
</p>
This gives a clearer picture with the numbers. Half of the reviews fall in the 90-100 range. And 23% of the listings are unrated. It is surprising that the site has less than 1% low reviews.

To finally make the predictions we will categorize the ratings into two bins to make the wisest use of our data. We will create two categories - ratings greater than 90 and ratings lesser than 90. We will take this step because more bins will mean lesser precision since we do not have enough data.

This is how the distribution looks like binned into two categories - still skewed, but with more data points in the second category.
<p align="center">
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/Boston_review_scores_2bins.png" />
</p>

To predict we will create new features that may help with the predictions. These are and not limited to distance of each listing from the city center, the various kinds of amenities, the lengths of the descriptive fields in the listing.  Finally after modelling we are able to predict the 90+ category with 75% precision and 90- category with 66% precision. These are decent results with the number of data points that we have.

<p align="center">
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/precision_rf_2bins.png" />
</p>

And the features which most contribute to the prediction are -
<p align="center">
  <img src="https://github.com/SmritiMohapatra/airbnb-data-analysis/blob/master/img/feature_importance_2bins.png" />
</p>
The number of days the host has been with Airbnb and whether the host is a superhost or not matters. Also lengths of descriptive fields matter implying conscientiousness. Distance to the city center also matters

### Recap
With the data we have we can predict ratings however to improve predictions we would want to -
* Collect more data
* Engineer more complex features - like distance to nearest subway stations, cleanliness from the cleanliness reviews  etc

With the current data however we are able to decipher trends in prices and availiability, across seasons and neighbourhoods.

##### Libraries Used
* Anaconda
* python
* pandas
* sklearn
* matplotlib
* seaborn

##### Software Used
* Tableau

##### Files
This repo contains the following files -
* data folder - contains the data segregated by city
* airbnb_data_analysis_AssessExplore.ipynb - Notebook containing the assessment and exploration of data
* airbnb_data_analysis_Model.ipynb - Notebook containing the predictive modeling

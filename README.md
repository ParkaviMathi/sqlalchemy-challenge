# sqlalchemy-challenge

I've decided to treat myself to a long holiday vacation in Honolulu, Hawaii! To help with my trip planning,I'll need to do some climate analysis on the area. The following sections outline the steps I will take to accomplish this task.

## Part 1: Climate Analysis and Exploration

In this section, I’ll use Python and SQLAlchemy to perform basic climate analysis and data exploration of my climate database. The following tasks have been completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.


The provided starter notebook and hawaii.sqlite files have been used to complete my climate analysis and data exploration.


SQLAlchemy’s create_engine has been used to connect to my SQLite database.


SQLAlchemy’s automap_base() has been used to reflect my tables into classes and a reference to those classes called Station and Measurement have been saved.


Python was linked to the database by creating a SQLAlchemy session.




### Precipitation Analysis

To perform an analysis of precipitation in the area,the following steps were taken:


The most recent date in the dataset was analysed.


Using this date, the previous 12 months of precipitation data was retrieved by querying the 12 previous months of data. 


Only the date and prcp values were selected.


The query results were loaded into a Pandas DataFrame, and the index wasset to the date column.


The DataFrame values were sorted by date.


The results were ploted by using the DataFrame plot method.



Pandas was used to print the summary statistics for the precipitation data.



### Station Analysis

To perform an analysis of stations in the area, the following steps were taken:


A query was designed to calculate the total number of stations in the dataset.


A query was designed to find the most active stations (the stations with the most rows).


The stations and observation counts in descending order were listed.


The station id that has the highest number of observations was found.


Using the most active station id, the lowest, highest, and average temperatures were calculated.





A query was designed to retrieve the previous 12 months of temperature observation data (TOBS).


Filtered by the station with the highest number of observations.


The previous 12 months of temperature observation data for this station was queried.


The results were plotted as a histogram with bins=12.





Session Closed.




## Part 2: Designing the Climate App

I’ll design a Flask API based on the queries that I have just developed.
Flask was used to create the routes, as follows:


/


Homepage.


All available routes are listed.




/api/v1.0/precipitation


The query results were converted to a dictionary using date as the key and prcp as the value.


The JSON representation of the dictionary was returned.




/api/v1.0/stations

A JSON list of stations from the dataset was returned.



/api/v1.0/tobs


The dates and temperature observations of the most active station for the previous year of data was queried.


A JSON list of temperature observations (TOBS) for the previous year was returned.




/api/v1.0/<start> and /api/v1.0/<start>/<end>


A JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range was returned.


When given the start only,  TMIN, TAVG, and TMAX for all dates greater than or equal to the start date was calculated.


When given the start and the end date, the TMIN, TAVG, and TMAX for dates from the start date through the end date (inclusive) was calculated.

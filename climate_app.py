import datetime as dt
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import os
print(os.curdir,"-"*10)

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create session from Python to the DB
session = Session(engine)

# Set up Flask and landing page
app = Flask(__name__)

@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"<p>Hawaii weather API</p>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>Returns a JSON list of percipitation data.<br/><br/>"
        f"/api/v1.0/stations<br/>Returns a JSON list of the weather stations.<br/><br/>"
        f"/api/v1.0/tobs<br/>Returns a JSON list of the Temperature Observations (tobs) for each station for the dates between 8/23/16 and 8/23/17.<br/><br/>"
        f"/api/v1.0/<start><br/>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and 8/23/17.<br/><br/>"
        f"/api/v1.0/<start>/<end><br/>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and end date.<br/><br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitaion():
    maxDate = dt.date(2017, 8 ,23)
    last_year = maxDate - dt.timedelta(days=365)

    preci_data = (session.query(Measurement.date, Measurement.prcp)
                .filter(Measurement.date <= maxDate)
                .filter(Measurement.date >=  last_year)
                .order_by(Measurement.date).all())

    preci_df = pd.DataFrame(preci_data, columns=['Date', 'Precipitation'])
    preci_sorted = preci_df.sort_values(by='Date')
    
    
    
    return preci_sorted.to_json()

@app.route('/api/v1.0/stations')
def stations():

    stations_all = session.query(Station.station).all()
    station_df = pd.DataFrame( stations_all)

    return station_df.to_json()

@app.route('/api/v1.0/tobs') 
def tobs():  
   
    obsdata = [Measurement.date, Measurement.tobs, Measurement.station]
    maxDate_format = dt.date(2017, 8 ,23)
    last_year = maxDate_format - dt.timedelta(days=365)
    obs_data = session.query(*obsdata).\
    filter(Measurement.station=='USC00519281').\
    filter(Measurement.date <= maxDate_format).\
    filter(Measurement.date >= last_year).all()

    
    tobs_df = pd.DataFrame(obs_data,  columns=['date','tobs','station'])
    tobs_df = tobs_df.set_index(['date'])
    

    return tobs_df.to_json()
    
    

@app.route('/api/v1.0/<start>') 
def startdate(start):
 
    day_temp_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    start_date_df = pd.DataFrame( day_temp_results, columns=['min','avg','max'])
    return start_date_df.to_json()

    
    

@app.route('/api/v1.0/<start>/<end>') 
def startend(start,end):

    multi_day_temp_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    start_end_df = pd.DataFrame( multi_day_temp_results, columns=['min','avg','max'])
    return start_end_df.to_json()



if __name__ == "__main__":
    app.run(debug=True)
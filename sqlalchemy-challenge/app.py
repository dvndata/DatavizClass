import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Return the JSON representation of your dictionary.
    # Convert list of tuples into normal list
    records = []
    for date, prcp in results:
        record_dict = {}
        record_dict["date"] = date
        record_dict["prcp"] = prcp
        records.append(record_dict)

    return jsonify(records)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Return a JSON list of stations from the dataset.
    results = session.query(Station.station).all()

    session.close()

    return jsonify(results)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # query for the dates and temperature observations from a year from the last data point.

    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= '2016-08-23').all()

    session.close()

    
    # Return a JSON list of Temperature Observations (tobs) for the previous year.
    all_temperatures = []
    for date, tobs in results:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["tobs"] = tobs
        all_temperatures.append(temp_dict)

    return jsonify(all_temperatures)


    @app.route("/api/v1.0/<start>")
    def stations():
        # Create our session (link) from Python to the DB
        session = Session(engine)

        # Return a JSON list of the minimum temperature, the average temperature, 
        # and the max temperature for a given start or start-end range.

        # When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` 
        # for all dates greater than and equal to the start date.

        # results = session.query(Station.station).all()

        session.close()

        return jsonify(results)

    
    @app.route("/api/v1.0/<start>/<end>")
    def stations():
        # Create our session (link) from Python to the DB
        session = Session(engine)

        # Return a JSON list of the minimum temperature, the average temperature, 
        # and the max temperature for a given start or start-end range.

        # * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` 
        # for dates between the start and end date inclusive.

        # results = session.query(Station.station).all()

        session.close()

        return jsonify(results)
    

if __name__ == '__main__':
    app.run(debug=True)

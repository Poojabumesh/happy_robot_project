import pandas as pd
from datetime import datetime

def load_available(csv_path, origin=None, destination=None, equipment_type=None):
    df = pd.read_csv(csv_path, parse_dates=['pickup_datetime', 'delivery_datetime'])

    #filter by origin, destination, and equipement
    if origin:
        df = df[df['origin'].str.lower() == origin.lower()]
    if destination:
        df = df[df['destination'].str.lower() == destination.lower()]
    if equipment_type:
        df = df[df['equipment_type'].str.lower() == equipment_type.lower()]
    
    return df.to_dict(orient='records')

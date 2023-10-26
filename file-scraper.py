from datetime import datetime, timedelta
import requests
import sqlalchemy
import json
import pandas as pd

pd.read_excel(
    "https://www.iso-ne.com/static-assets/documents/2023/01/2023_daygenbyfuel.xlsx"
)

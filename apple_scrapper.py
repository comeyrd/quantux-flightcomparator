import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore
applerev = AppStore(country='us', app_name='kayak', app_id = '305204535')

applerev.review(how_many=5000)
df = pd.DataFrame(applerev.reviews)
df['year'] = df['date'].dt.year

new_df = df[["year", "rating", "review", "title"]]
new_df.to_csv("apple.csv", index=False)
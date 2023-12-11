
import pandas as pd
import numpy as np

from google_play_scraper import reviews_all,reviews

#result = reviews_all('com.kayak.android')
result, continuation_token = reviews('com.kayak.android',count=100)
df = pd.DataFrame(result)
df['year'] = df['at'].dt.year
new_df = df[["year", "score", "content"]]
new_df.columns = ["year", "rating", "review"]

new_df.to_csv("android.csv", index=False)
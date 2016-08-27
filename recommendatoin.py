import pandas as pd

ratings_df = pd.read_table('ml-1m/ratings.dat',header=None,sep='::',names=['user_id','movie_id','rating','timestamp'])

del ratings_df['timestamp']

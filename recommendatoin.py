import pandas as pd

movies_df = pd.read_table('ml-1m/movies.dat',header=None,sep='::',names=['movie_id','movie_title','movie_genre'],engine='python')

ratings_df = pd.read_table('ml-1m/ratings.dat',header=None,sep='::',names=['user_id','movie_id','rating','timestamp'],engine='python')

del ratings_df['timestamp']

ratings_df = pd.merge(ratings_df,movies_df,on='movie_id')[['user_id','movie_title','movie_id','rating']]

ratings_mtx_df = ratings_df.pivot_table(values='rating',index='user_id',columns='movie_title')

ratings_mtx_df.fillna(0,inplace=True)

movie_index = ratings_mtx_df.columns

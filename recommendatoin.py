import pandas as pd

import numpy as np

movies_df = pd.read_table('ml-1m/movies.dat',header=None,sep='::',names=['movie_id','movie_title','movie_genre'],engine='python')

ratings_df = pd.read_table('ml-1m/ratings.dat',header=None,sep='::',names=['user_id','movie_id','rating','timestamp'],engine='python')

del ratings_df['timestamp']

ratings_df = pd.merge(ratings_df,movies_df,on='movie_id')[['user_id','movie_title','movie_id','rating']]

ratings_mtx_df = ratings_df.pivot_table(values='rating',index='user_id',columns='movie_title')

ratings_mtx_df.fillna(0,inplace=True)

movie_index = ratings_mtx_df.columns

corr_matrix = np.corrcoef(ratings_mtx_df.T)

def get_movie_similarity(movie_title):

    movie_idx = list(movie_index).index(movie_title)

    return corr_matrix[movie_idx]

def get_movie_recommendation(user_movies):

    movie_similarity = np.zeros(corr_matrix.shape[0])

    for movie_id in user_movies:

        movie_similarity = movie_similarity + get_movie_similarity(movie_id)

    similarity_df = pd.DataFrame({
        'movie_title' : 'movie_index',
        'sum_similarity' : 'movie_similarity'
        })

    similarity_df = similarity_df[~(similarity_df.movie_title.isin(user_movies))]

    similarity_df = similarity_df.sort_values(by=['sum_similarity'],ascending=False)

    return similarity_df

sample_user = 30

sample_user_movies = ratings_df[ratings_df.user_id==sample_user].movie_title.tolist()

recommendation = get_movie_recommendation(sample_user_movies)

recommendation.movie_title.head(20)

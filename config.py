class Config:
    '''
    General configuration parent class
    '''
    
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{550}?api_key={b7fe728244a843091e8a18442c4fd6b7'
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

import os

class Config:

    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{550}?api_key={b7fe728244a843091e8a18442c4fd6b7'
    MOVIE_API_KEY = os.environ.get('b7fe728244a843091e8a18442c4fd6b7')
    SECRET_KEY = os.environ.get('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiN2ZlNzI4MjQ0YTg0MzA5MWU')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
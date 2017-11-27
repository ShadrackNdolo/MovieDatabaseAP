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
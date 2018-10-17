import os

class Config:
    '''
    General configuration parent class
    '''
    pass
'''
    General configuration parent class
    '''
SECRET_KEY = 'os.environ.get'


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
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}

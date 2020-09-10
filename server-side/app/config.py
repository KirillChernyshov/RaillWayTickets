

class Config:
    SECRET_KEY = 'we4fh%gC_za:*8G5v=fbv'
    JWT_SECRET_KEY = 'we4fh%gC_za:*8G5v=fbv'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
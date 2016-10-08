DEBUG = True
SECRET_KEY = 'dev'
SERVER_NAME = '127.0.0.1:5000'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:SniperX4@localhost/scrapy'
SQLALCHEMY_TRACK_MODIFICATIONS = False

ALEMBIC_CONTEXT = {
    'compare_type': True,
    'compare_server_default': True,
    'user_module_prefix': 'user',
}

# Set the following in <app.instance_path>/config.py
# On dev that's <project>/instance/config.py
# On prod that's <env>/var/sopy-instance/config.py

# SE_API_KEY = str
# SE_CONSUMER_KEY = int
# SE_CONSUMER_SECRET = str

# GOOGLE_ANALYTICS_KEY = str

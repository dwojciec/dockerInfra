my_settings = {
    'MONGO_HOST': 'db',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'test',
    'DOMAIN': {'contacts': {}}
}

from eve import Eve

app = Eve(settings=my_settings)
app.run(host='0.0.0.0', debug=True)

import os

RESOURCE_METHODS = ['GET','POST','DELETE']

ITEM_METHODS = ['GET','PATCH','DELETE']

#MONGO_HOST = 'db' 
#MONGO_PORT = '27017'

MONGO_HOST = os.environ['DB_PORT_27017_TCP_ADDR']
MONGO_PORT = os.environ['DB_PORT_27017_TCP_PORT']

#MONGO_USERNAME = 'reloca'
#MONGO_PASSWORD = 'reloca123'
MONGO_DBNAME = 'relocaDB'

X_DOMAINS = '*'
X_HEADERS = ['Authorization','If-Match','Access-Control-Expose-Headers','Content-Type','Pragma','Cache-Control']
X_EXPOSE_HEADERS = ['Origin', 'X-Requested-With', 'Content-Type', 'Accept']

DOMAIN = {
    'user': {
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'username',
            },
        'schema': {
            'firstname': {
                'type': 'string'
            },
            'lastname': {
                'type': 'string'
            },
            'username': {
                'type': 'string',
		'unique': True
            },
	    'password': {
		'type': 'string'
	    },
            'phone': {
                'type': 'string'
            }
        }
    },
    'item': {
	'MONGO_QUERY_BLACKLIST' : ['$where'],
        'schema': {
            'name':{
                'type': 'string'
                },
            'username': {
                'type': 'string'
                }
            },
        'resource_methods': ['GET', 'POST','DELETE'],
        }
}

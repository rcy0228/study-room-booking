'''
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.',  # Replace with your database engine (e.g., 'mysql.connector.django')
        'NAME': 'Application_programing_project',
        'USER': 'root',
        'PASSWORD': 'rituyadav',
        'HOST': '<your_database_host>',
        'PORT': '<your_database_port>',
    }
}
'''

import mysql.connector
 
# Connect to the database
connection = mysql.connector.connect(host='localhost',
                                     database='application_programing_project',
                                     user='root',
                                     password='rituyadav')
 
cursor = connection.cursor()

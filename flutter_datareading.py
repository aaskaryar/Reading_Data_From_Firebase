# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



# Initialize Firebase app with credentials
cred = credentials.Certificate('/path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# Retrieve data from Firestore collection
docs = db.collection('Count').get()

# Create list of dictionaries to store data
data_list = []
for doc in docs:
    data_dict = doc.to_dict()
    data_dict['id'] = doc.id
    data_list.append(data_dict)

# Create Pandas dataframe from list of dictionaries
df = pd.DataFrame(data_list)

# Print dataframe
print(df)




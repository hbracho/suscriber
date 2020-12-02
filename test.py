from pymongo import MongoClient
# pprint library is used to make the output look more pretty
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
#client = MongoClient('localhost:27017',username='training',password='password',authSource='training',authMechanism='SCRAM-SHA-256')
client = MongoClient('localhost:27017',username='admin',password='password',authSource='admin',authMechanism='SCRAM-SHA-256')
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
print(serverStatusResult)
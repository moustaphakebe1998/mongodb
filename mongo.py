from pymongo import MongoClient

# Configuration de la connexion
username = "test"
password = "test"
host = "127.0.0.1"
port = 27017

# Création de l'URI de connexion
uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"

# Connexion à MongoDB
client = MongoClient(uri)

# Accès à la base de données 'test'
db = client.test

# Exécuter une requête pour compter les documents dans la collection 'restaurants'
count = db.restaurants.count_documents({"address.street": "Franklin Street"})

print(f"Number of restaurants on Franklin Street: {count}")


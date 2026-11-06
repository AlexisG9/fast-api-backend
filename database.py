from motor.motor_asyncio import AsyncIOMotorClient

# URL de conexión a mongodb
MONGO_URL="mongodb+srv://ricardoguerrero9191_db_user:Eg1NdW7LZvBydThT@cluster0.vwoiglw.mongodb.net/"

# Conexión al cliente
client = AsyncIOMotorClient(MONGO_URL)

# Selección de base de datos
database = client.mibasededatos

# Selección de una colección
collection = database.get_collection("micoleccion")

import os
import pymysql

# Load the environment variables from the .env file in this directory
DB_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(DB_DIR, '.env')
if os.path.exists(dotenv_path):
    with open(dotenv_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ[key.strip()] = val.strip().strip("'\"")

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "tech_platform")

seed_resources = [
    {
        "Id": "095a6d7f-4893-4a3b-9c35-ff595d4bfa0c",
        "Name": "208",
        "State": "filthy",
        "FloorNumber": "2",
        "LocationNotes": "1"
    },
    {
        "Id": "0943f364-491f-4590-a207-fc92dc9ab92e",
        "Name": "107",
        "State": "DoNotDisturb",
        "FloorNumber": "1",
        "LocationNotes": None
    },
    {
        "Id": "eeb095d1-e8ed-40e9-9b4f-f5a91bf85bc4",
        "Name": "810",
        "State": "Dirty",
        "FloorNumber": "8",
        "LocationNotes": None
    },
    {
        "Id": "731aaefd-1f84-47cb-858a-ef701f6a375a",
        "Name": "108",
        "State": "Dirty",
        "FloorNumber": "1",
        "LocationNotes": ""
    },
    {
        "Id": "ec06ad34-be1a-40f9-b934-dc7b561d2f12",
        "Name": "309",
        "State": "Clean",
        "FloorNumber": "3",
        "LocationNotes": None
    },
    {
        "Id": "359fecf8-2bd3-4bdb-ada7-d2a2e6ae661c",
        "Name": "802",
        "State": "Clean",
        "FloorNumber": "8",
        "LocationNotes": "2"
    },
    {
        "Id": "6f8bdb5b-86ad-47c2-8378-d14350a38eaa",
        "Name": "407",
        "State": "Dirty",
        "FloorNumber": "4",
        "LocationNotes": "0506"
    },
    {
        "Id": "baade5a4-9dd9-43b2-90d8-c936c115bc99",
        "Name": "116",
        "State": "Dirty",
        "FloorNumber": "8",
        "LocationNotes": None
    },
    {
        "Id": "5ee074b1-6c86-48e8-915f-c7aa4702086f",
        "Name": "0101",
        "State": "DoNotDisturb",
        "FloorNumber": "1",
        "LocationNotes": "A1"
    },
    {
        "Id": "9868b6d9-1e6d-4e85-a64a-b731628a0da2",
        "Name": "203",
        "State": "Dirty",
        "FloorNumber": "2",
        "LocationNotes": None
    }
]

def seed_db():
    print(f"Connecting to MySQL server at {DB_HOST}:{DB_PORT} as {DB_USER}...")
    
    # Connect without specifying a database to create the database if not exists
    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()
    
    print(f"Ensuring database '{DB_NAME}' exists...")
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
    conn.select_db(DB_NAME)
    
    print("Recreating 'resources' table...")
    cursor.execute("DROP TABLE IF EXISTS resources")
    cursor.execute("""
        CREATE TABLE resources (
            id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            state VARCHAR(255) NOT NULL,
            floor_number VARCHAR(255) NOT NULL,
            location_notes TEXT
        )
    """)
    
    print("Inserting seed resources...")
    for res in seed_resources:
        cursor.execute(
            "INSERT INTO resources (id, name, state, floor_number, location_notes) VALUES (%s, %s, %s, %s, %s)",
            (res["Id"], res["Name"], res["State"], res["FloorNumber"], res["LocationNotes"])
        )
    
    conn.commit()
    conn.close()
    print("MySQL Database successfully initialized and seeded.")

if __name__ == "__main__":
    seed_db()

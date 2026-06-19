import os
import pymysql
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Tech Platform API")

# Enable CORS to allow the frontend to access the backend API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.get("/api/resources")
def get_resources():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, state, floor_number, location_notes FROM resources")
        rows = cursor.fetchall()
        conn.close()
    except pymysql.MySQLError as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Database query error: {str(e)}"
        )

    resources = []
    for row in rows:
        resources.append({
            "Id": row["id"],
            "Name": row["name"],
            "State": row["state"],
            "Data": {
                "Discriminator": "Space",
                "Value": {
                    "FloorNumber": row["floor_number"],
                    "LocationNotes": row["location_notes"]
                }
            }
        })
    
    return resources

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5001)

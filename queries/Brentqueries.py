import psycopg
from database import get_connection

def create_tables():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS seasonal_tips (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL UNIQUE,
                    content TEXT NOT NULL,
                    season VARCHAR(50) NOT NULL
                );
            """)
            conn.commit()
            print("Seasonal tips table checked/created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")
    finally:
        conn.close()

def add_sample_data():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # Sample Data
            cur.execute("""
                INSERT INTO seasonal_tips (title, content, season) VALUES
                ('Spring Planting', 'Start planting your seeds indoors for an early harvest!', 'spring'),
                ('Summer Watering', 'Water your plants in the early morning to prevent evaporation.', 'summer'),
                ('Fall Harvest', 'It''s time to harvest root vegetables like carrots and potatoes.', 'fall')
                ON CONFLICT (title) DO NOTHING;
            """)
            conn.commit()
            print("Sample data added successfully.")
    except Exception as e:
        print(f"Error adding sample data: {e}")
    finally:
        conn.close()
import os
from dotenv import load_dotenv

# Încărcăm variabilele de mediu din .env
load_dotenv()

class Settings:
    # Obține variabilele de mediu necesare
    DATABASE_URL: str = os.getenv("DATABASE")
    URL_KEYS: str = os.getenv("URL_KEYS")  # Valoare implicită dacă nu e setată în .env

# Creează o instanță a configurației
settings = Settings()
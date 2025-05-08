import os

# Fetch credentials from environment variables
DB_USERNAME = os.getenv("DB_USERNAME", "SYSTEM")
DB_PASSWORD = os.getenv("DB_PASSWORD", "oracle")
DB_DSN = os.getenv("DB_DSN", "localhost/ORCLCDB")
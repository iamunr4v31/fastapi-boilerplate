class Config:
    DATABASE = "sqlite"
    DATABASE_URI = "database.db"
    SQLALCHEMY_ENGINE_OPTIONS = {
        "echo": True,
        "connect_args": {
            "check_same_thread": False
        }
    }

class DevConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    DEBUG=False
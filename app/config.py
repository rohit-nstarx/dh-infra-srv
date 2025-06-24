import os

class EnvironmentVariables:

    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG")

env_var = EnvironmentVariables()

import os
from server.configuration import settings
# Load the development "mode". Use "developmen" if not specified
env = os.environ.get("PYTHON_ENV", "development")
port = os.environ.get("PORT", 8080)
# Configuration for each environment
# Alternatively use "python-dotenv"
video_file_path = settings['common']['videopath']
all_environments = {
    "development": {"port": 5001, "debug": True, "swagger-url": "/swagger/ui"},
    "production": {"port": port, "debug": False, "swagger-url": None}
}

# The config for the current environment
environment_config = all_environments[env]

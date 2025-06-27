from dotenv import load_dotenv, find_dotenv

env_file = find_dotenv()
if env_file:
    load_dotenv(env_file)

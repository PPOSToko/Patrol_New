from dotenv import load_dotenv
import os

# APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
# dotenv_path = os.path.join(APP_ROOT, '.env')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)
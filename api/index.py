import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from app import app as application
from app import init_extensions

# Initialize extensions now that the runtime environment is ready
init_extensions(application)

app = application
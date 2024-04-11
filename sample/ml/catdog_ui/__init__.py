from flask import Flask, render_template
from pathlib import Path
import os

cfg_env_name = f"FLASKAPP_CATDOG_UI_{os.environ['ENV']}_CFG_PATH"

app = Flask(__name__)

app.config.from_envvar(str(cfg_env_name))

from catdog_ui.views import views, entries, predict

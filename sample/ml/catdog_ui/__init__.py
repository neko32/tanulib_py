from flask import Flask, render_template
from pathlib import Path
from keras.models import Model, load_model
import os
from os.path import exists
from sqlite3 import Connection

cfg_env_name = f"FLASKAPP_CATDOG_UI_{os.environ['ENV']}_CFG_PATH"
model_store_loc = os.path.join(os.environ["TANUAPP_ML_DIR"], "catdog")
if not exists(model_store_loc):
    raise Exception("model dir doesn't exist")

model: Model = load_model(model_store_loc)
model.summary()
app = Flask(__name__)

app.config.from_envvar(str(cfg_env_name))
db_name = app.config.get("DB_NAME")

db_path = str(Path(os.environ['HOME_DB_PATH']).joinpath(db_name))
db_conn = Connection(db_path, check_same_thread=False)


from catdog_ui.views import views, entries, predict

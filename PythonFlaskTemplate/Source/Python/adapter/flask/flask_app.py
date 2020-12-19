import os
from logging import error
from pathlib import Path

from flask import Flask, render_template
from ruamel.yaml import YAML

from adapter.main import PythonFlaskTemplateApp


_FLASK_ENV_VAR_NAME = "FLASK_ENV"

if _FLASK_ENV_VAR_NAME not in os.environ:
    # There does not appear to be a way to provide the FLASK_ENV setting at runtime. Fail loudly
    error(f"Environment Variable '{_FLASK_ENV_VAR_NAME}' needs to be configured.")
    exit(-1)


def _run_app(*, app_config: dict, flask_construction_config: dict, flask_run_config: dict) -> None:
    flask_web_app = Flask(__name__, **flask_construction_config)

    app = PythonFlaskTemplateApp(**app_config)

    @flask_web_app.route("/")
    @flask_web_app.route("/index")
    def hello_world():
        return render_template("index.html", **{
            "title": app.name,
            "summary": app.description,
        })

    flask_web_app.run(**flask_run_config)


if __name__ == "__main__":
    import sys
    config_file = sys.argv[1]
    config: dict = YAML(typ="safe").load(Path(config_file))
    _run_app(**config)
else:
    error("Run this script directly instead of importing via another service")

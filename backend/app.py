"""
NEXUS AI backend — start the Flask REST API.

    python app.py            -> API on http://127.0.0.1:5000
    python app.py --reset    -> rebuild the database from scratch first

First run: creates the database, generates training data, tunes and evaluates the model.
Then start the React frontend from the ../frontend folder with `npm run dev`.
"""
import os
import sys

from nexus import create_app
from nexus.config import Config
from nexus.seed import seed_database
from nexus.train import train_and_evaluate

if __name__ == "__main__":
    reset = "--reset" in sys.argv
    fresh = reset or not os.path.exists(Config.DATABASE)
    seed_database(reset=reset)
    if fresh or not os.path.exists(os.path.join(Config.MODEL_DIR, "metrics.json")):
        train_and_evaluate()
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    print(f"\n  NEXUS AI API running at http://127.0.0.1:{port}"
          "\n  Now start the React app:  cd ../frontend  &&  npm run dev"
          "\n  Admin login: admin@nexus.ai / admin123  |  Demo login: demo@nexus.ai / demo123\n")
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("FLASK_DEBUG") == "1")

from app import create_app
import os

app = create_app()

if __name__ == "__main__":
    # FLASK_RUN_HOST first，default 0.0.0.0
    # FLASK_RUN_PORT first，next pick PORT，otherwise use 5000

    # read var host/port from env
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    
    port = int(os.environ.get("FLASK_RUN_PORT", os.environ.get("PORT", 5000)))

    # app.run
    app.run(host=host, port=port, debug=True)

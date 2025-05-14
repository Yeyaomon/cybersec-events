if __name__ == "__main__":
    import os

    # FLASK_RUN_HOST first，default 0.0.0.0
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    # FLASK_RUN_PORT first，next pick PORT，otherwise use 5000
    port = int(os.environ.get("FLASK_RUN_PORT", os.environ.get("PORT", 5000)))

    app.run(host=host, port=port, debug=True)

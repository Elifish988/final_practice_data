from  flask import Flask

from Blueprints.students_analysis.performance_analysis_bp import bp_performance
from postges.db import engine, Base
from postges.load import load_json, load_all_csv

app = Flask(__name__)

app.register_blueprint(bp_performance)

@app.route("/load", methods=["GET"])
def initialize_database():
    """Drop, Create, and Load data into the database."""
    Base.metadata.drop_all(engine)
    print("Dropped all tables.")

    Base.metadata.create_all(engine)
    print("Created all tables.")

    load_all_csv()
    load_json()
    return "Database initialized successfully."





if __name__ == '__main__':
    app.run(debug=True)
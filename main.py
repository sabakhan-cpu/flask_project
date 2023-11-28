from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import create_engine, text

app = Flask(__name__)


def load_data_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('select * from JOBS'))
        job = result.all()
        return job


def Convert(db_data, di):
    for a, b in db_data:
        di.setdefault(a, []).append(b)
    return di


# Driver Code

dictionary = {}
Convert(load_data_from_db(), dictionary)


# JOBS = [
#     {
#         'id': 1,
#         "title": "Iron Man",
#         "location": "Chicago, New York",
#         "Salary": "130 gold coin/month",
#
#     },
#     {'id': 2,
#      "title": "Thor",
#      "location": "Asgard,Planet",
#      "Salary": "135 gold coin/month",
#      },
#     {
#         'id': 3,
#         "title": "Black Widow",
#         "location": "Volgograd, Russian SFSR, USSR",
#         "Salary": "125 gold coin/month",
#     }
# ]


@app.route("/")
def home():
    job = load_data_from_db()
    return render_template('index.html', job=job)


# @app.route('/api/jobs/')
# def call():
#     return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

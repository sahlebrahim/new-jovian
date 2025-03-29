from flask import Flask,render_template
from database import engine
from sqlalchemy import text

app = Flask(__name__)



def load_jobs():
    with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      result_dicts = []
      for row in result.all():
          #The ._mapping attribute in SQLAlchemy Row objects provides dictionary-like access to the data in a database row.
          result_dicts.append(dict(row._mapping))
      
    return result_dicts


@app.route("/")
def hello_world():
    jobs = load_jobs()
    return render_template("home.html",jobs = jobs)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
from flask import Flask,render_template,jsonify
from database import engine,load_jobs,load_job_id
from sqlalchemy import text

app = Flask(__name__)






@app.route("/")
def hello_world():
    jobs = load_jobs()
    return render_template("home.html",jobs = jobs)


@app.route("/job/<id>")
def job(id):
    job = load_job_id(id)
    if not job:
        return "Job not found", 404
    
    #print(job)
    return render_template("jobpage.html",job = job)


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)

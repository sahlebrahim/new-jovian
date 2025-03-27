from flask import Flask,render_template

app = Flask(__name__)

JOBS = [
    {'id': 1,
     'title': 'data analyst',
     'location': 'Bengaluru,india',
     'salary': 'Rs. 8,00,000',
    },
    {'id': 2,
     'title': 'software engineer',
     'location': 'Hyderabad,india',
     'salary': 'Rs. 10,00,000',
    },
    {'id': 3,
     'title': 'project manager',
     'location': 'Chennai,india',
     #'salary': 'Rs. 12,00,000',
    },
    {'id': 4,
     'title': 'Backend Engineer',
     'location': 'San francisco,USA',
     'salary': '$120000',
    }
]


@app.route("/")
def hello_world():
    return render_template("home.html",jobs = JOBS)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
from flask import Flask, render_template, request, session
from flask_session import Session

from cs50 import SQL

db = SQL("sqlite:///actors_overlap.db")

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        guessed = True
        answer = session.get('answer')
        image1 = session.get('image1')
        image2 = session.get('image2')
        person1 = session.get('person1')
        person2 = session.get('person2')
        if request.form.get('guess').title() == answer:
            result = 'Correct!'
            return render_template('index.html', answer=answer,result=result, image1=image1, image2=image2, person1=person1, person2=person2, guessed=guessed)
        else:
            result = 'Incorrect!'
            return render_template('index.html', answer=answer,result=result, image1=image1, image2=image2, person1=person1, person2=person2, guessed=guessed)
    else:
        guessed = False
        answer = db.execute("""SELECT pairs.shared_name AS shared,
                            image1.filepath AS image1,
                            image2.filepath AS image2,
                            person1.first_name AS first_name,
                            person2.last_name AS last_name
                            FROM pairs
                            JOIN image AS image1 ON pairs.person_id1 = image1.person_id
                            JOIN image AS image2 ON pairs.person_id2 = image2.person_id
                            JOIN person AS person1 ON pairs.person_id1 = person1.person_id
                            JOIN person AS person2 ON pairs.person_id2 = person2.person_id
                            ORDER BY RANDOM() LIMIT 1""")
        shared = answer[0]['shared']
        image1 = answer[0]['image1']
        image2 = answer[0]['image2']
        person1 = answer[0]['first_name']
        person2 = answer[0]['last_name']
        session['answer'] = shared
        session['image1'] = image1
        session['image2'] = image2
        session['person1'] = person1
        session['person2'] = person2

        return render_template('index.html', image1=image1, image2=image2, person1=person1, person2=person2, shared=shared, guessed=guessed)

if __name__ == '__main__':
    app.run(debug=True)

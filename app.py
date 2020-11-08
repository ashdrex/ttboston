from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profiles.db'
db = SQLAlchemy(app)

class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repre__(self):
        return '<Profile %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['POST', 'GET'])
@app.route('/quiz.html', methods=['POST', 'GET'])
def quiz():
    return render_template('quiz.html')

@app.route('/profile', methods=['POST', 'GET'])
@app.route('/profile.html', methods=['POST', 'GET'])
def profile():
    if request.method == 'POST':
        username = request.form['content']
        new_prof = Profiles(content=username)

        try:
            db.session.add(new_prof)
            db.session.commit()
            return render_template('quiz.html', username = username)
        except:
            return 'Error adding profile.'

    else:
        user_prof = Profiles.query.order_by(Profiles.date_created).all()
        return render_template('profile.html', user_prof=user_prof)

if __name__ == "__main__":
    app.run(debug=True)
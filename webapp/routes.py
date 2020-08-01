from webapp import app, mongo
from flask import render_template, request
import datetime


@app.route('/')
def form():
    return render_template('form.html')

@app.route('/process', methods=['GET', 'POST'])
def process_feedback():
    rating = request.form.get('inlineRadioOptions')
    text = request.form.get('feedbackText')
    date = datetime.datetime.today()
    mongo.db.feedbacks.insert({'rating': int(rating), 'feedback': text, 'date': date})
    return '<h2>Thank you for your feedback</h2>'
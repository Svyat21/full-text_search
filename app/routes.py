from app import app
from app.models import Document
from flask import request, render_template


@app.route('/')
@app.route('/index')
def index():
    q = request.args.get('q')
    if q:
        posts, total = Document.search(q, 1, 20)
    else:
        posts, total = None, None
    return render_template('index.html', posts=posts, total=total)

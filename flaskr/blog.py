import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/blogs')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    data = []
    for post in posts:
        data.append({
            'id': post['id'],
            'title': post['title'],
            'body': post['body'],
            'created': post['created'],
            'author_id': post['author_id'],
            'username': post['username']
        })
    return jsonify(data)

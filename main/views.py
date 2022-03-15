from flask import Blueprint, render_template, request, flash
from functions import by_word_search

blueprint_main = Blueprint('blueprint_main', __name__, template_folder='templates', static_folder='static')


@blueprint_main.route('/')
def index():
    return render_template('index.html', title='Поиск постов')


@blueprint_main.route('/search')
def search_page():
    s = request.args.get('s')
    posts = by_word_search(s)
    return render_template('post_list.html', posts=posts, s=s)
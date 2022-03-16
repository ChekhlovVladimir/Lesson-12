import logging

from flask import Blueprint, render_template, request, flash

import functions

blueprint_loader = Blueprint('blueprint_loader', __name__, template_folder='templates', static_folder='static')


@blueprint_loader.route('/post')
def page_form():
    return render_template('post_form.html', title='Добавить пост')


@blueprint_loader.route('/post', methods=['POST'])
def uploaded_page():
    picture = request.files.get('picture', None)
    content = request.values.get('content', None)
    pic_path = functions.path_uploaded_pic(picture)
    if not content or not picture:
        return "Данные внесены не полностью "

    try:
        picture_url = '/' + pic_path
    except TypeError:
        logging.info("Ошибка типа")
        return"Файл не найден. Ошибка типа."
    else:
        make_post = {'pic': picture_url, 'content': content}
        functions.post_add_to_json(make_post)
        logging.info(f'Новый пост добавлен')
        return render_template('post_uploaded.html', picture=picture_url, content=content)

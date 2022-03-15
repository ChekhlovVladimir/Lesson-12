from flask import Blueprint, render_template, request, flash

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

blueprint_loader = Blueprint('blueprint_loader', __name__, template_folder='templates', static_folder='static')


@blueprint_loader.route('/post')
def page_form():
    return render_template('post_form.html', title='Добавить пост')


@blueprint_loader.route('/post', methods=['POST'])
def uploaded_page():
    picture = request.files.get("picture")
    content = request.values.get("content")
    filename = picture.filename
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        picture.save(f'./uploads/images/{filename}')
        return render_template('post_uploaded.html', picture=picture, content=content)
    else:
        return f"Неподдерживаемый формат файла {extension}"

import json
import logging
from json import JSONDecodeError

logging.basicConfig(filename="basic.log", encoding='utf-8')


def json_loaded_file():
    try:
        with open('posts.json', 'r', encoding='utf-8') as my_file:
            posts = json.load(my_file)
    except FileNotFoundError:
        logging.exception("Файл не найден.")
        return "Файл для загрузки  не найден!"
    except JSONDecodeError:
        logging.exception("Ошибка декодирования JSON")
        return "Декодирование не произошло!"
    else:
        return posts


def by_word_search(user_input):
    posts_found = []
    posts = json_loaded_file()
    lowered_user_input = user_input.lower()

    for post in posts:
        if lowered_user_input in post["content"].lower().split(", "):
            posts_found.append(post)
            return posts_found
        else:
            raise TypeError("По запросу ничего не найдено! Повторите ввод с другим значением!")


def path_uploaded_pic(picture):
    allowed_extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    filename = picture.filename
    extension = filename.split(".")[-1]
    if extension not in allowed_extensions:
        logging.info("Добавляемый файл не картинка")
        raise TypeError("Картинка не найдена.Неподдерживаемый формат файла")
    try:
        picture.save(f'./uploads/images/{filename}')
        logging.info("Файл успешно сохранён")
        return f'./uploads/images/{filename}'
    except FileNotFoundError:
        logging.info("Ошибка в указании пути к файлу")
        return "Не найден файл"


def post_json_recording(posts):
    with open('posts.json', 'w', encoding='utf-8', ) as post_file:
        json.dump(posts, post_file, ensure_ascii=False)


def post_add_to_json(post):
    posts = json_loaded_file()
    posts.append(post)
    post_json_recording(posts)
    return posts

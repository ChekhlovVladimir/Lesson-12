import json


def json_loaded_file():
    with open('posts.json', 'r', encoding='utf-8') as my_file:
        posts = json.load(my_file)
        return posts


def by_word_search(user_input):
    posts_found = []
    posts = json_loaded_file()
    lowered_user_input = user_input.lower()

    for post in posts:
        if lowered_user_input in post["content"].lower().split(" "):
            posts_found.append(post)
    return posts_found


def post_json_recording(post):
    with open('posts.json', 'w', encoding='utf-8') as post_file:
        json.dump(post, post_file)

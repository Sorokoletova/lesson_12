import json
def get_posts_list():
    """ Получаем список всех постов"""

    with open("posts.json", encoding='utf8') as file:
        posts_list = json.load(file)

    return posts_list



def get_post_content(content):
    """Получаем пост по контенту"""

    posts = get_posts_list()
    content_l = content.lower()
    for post in posts:
        postes_list = post["content"].lower().split(", ")
        print(postes_list)
        for position in postes_list:
            if content_l in position:
                post_content = post

    return post_content


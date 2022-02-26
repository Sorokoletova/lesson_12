from flask import Blueprint, render_template, request

from function12 import get_post_content
find_post = Blueprint('find_post', __name__, template_folder='templates')
post_list = Blueprint('post_list', __name__, template_folder='templates')

@find_post.route('/')
def find_post():
    return render_template("index.html")

# @post_list.route('/search',)
# def post_list():
#     post = request.form.get("search_input")
#     postes = get_post_content(post)
#     return render_template("post_list.html", postes=postes)



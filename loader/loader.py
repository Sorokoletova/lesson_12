from flask import Blueprint, render_template, request

from function12 import get_post_content
loader_post = Blueprint('loader_post', __name__, template_folder='templates')


@loader_post.route('/',)
def loader_post():
    return render_template("post_form.html")

# @post_list.route('/search',)
# def post_list():
#     post = request.form.get("search_input")
#     postes = get_post_content(post)
#     return render_template("post_list.html", postes=postes)

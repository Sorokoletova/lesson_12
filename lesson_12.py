from flask import Flask, Blueprint, render_template, request
# from functions import ...
from main.main import find_post

# POST_PATH = "posts.json"
# UPLOAD_FOLDER = "uploads/images"
app = Flask(__name__)

app.register_blueprint(find_post)

# @app.route("/")
# def page_index():
#     return render_template("index.html")
# 
# 
# @app.route("/list")
# def page_tag():
#     pass
# 
# 
# @app.route("/post", methods=["GET", "POST"])
# def page_post_form():
#     pass
# 
# 
# @app.route("/post", methods=["POST"])
# def page_post_upload():
#     pass
# 
# 
# @app.route("/uploads/<path:path>")
# def static_dir(path):
#     return send_from_directory("uploads", path)
# 

app.run()

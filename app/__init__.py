from flask import Flask

app = Flask(__name__)

# 普通importは一番上に書くが、appがフォルダ名と被っていてエラーになるので一番下に書いている
from app import routes

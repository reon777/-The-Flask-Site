# The-Flask-Site

・以下のチュートリアルをベースに作成したサイト  
　https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

・Flaskの勉強目的のため実用性は特にない

・venv環境を利用する場合  
　.\venv\Scripts\activate  
　deactivate

・起動コマンド  
 `flask run`  
http://127.0.0.1:5000/

DEBUG MODE
$env:FLASK_ENV="production"
$env:FLASK_DEBUG="0"

※メールは2段階認証を無効と安全性の低いアプリの許可を有効にしないと来ない
$env:MAIL_SERVER="smtp.gmail.com"
$env:MAIL_PORT="587"
$env:MAIL_USE_TLS="1"
$env:MAIL_USERNAME="reon777.3313@gmail.com"
$env:MAIL_PASSWORD="reosuke3313"

# 必要なモジュールのインポート
from flask import Flask, request, render_template
from wtforms import Form, StringField, validators, SubmitField

# appという変数名で Flask オブジェクトをインスタンス化
app = Flask(__name__)

# WTforms を使い、index.html 側で表示させるフォームを構築
class InputForm(Form):
  # validators:条件に当てはまっているかどうかを管理する, InputRequired:フォームへの入力を必須とする
	InputFormTest = StringField("文字を入力してください", [validators.InputRequired()])
 
	# Html 側で表示する submit ボタンを表示
	submit = SubmitField("送信")
 
# URL にアクセスがあった場合の挙動の設定
@app.route("/", methods = ["GET", "POST"])
def input():
	# WTForms で構築したフォームをインスタンス化
	form = InputForm(request.form)
	
	# POST メソッドの条件の定義（送信ボタンが押された場合）
	if request.method == 'POST':
   	
    # 条件に当てはまらない場合（入力フォームが空欄）
		if form.validate() == False:
			return render_template('index.html', forms=form)
		# 条件に当てはまった場合の処理の実行を定義（入力フォームに何らかの文字が入力された）
		else:
			outputname_ = request.form['InputFormTest']
			return render_template('result.html', outputname=outputname_)
	
	# GET メソッドの定義（Webページへのアクセス要求があった場合）
	elif request.method == 'GET':
		return render_template('index.html', forms=form)

# アプリケーションの実行の定義
if __name__ == "__main__":
  app.run(debug=True)
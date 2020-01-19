from flask import render_template

class UserModule:
	def home(self):
		return render_template('index.html')
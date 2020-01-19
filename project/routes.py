from project import app
from project.user_module import UserModule

um = UserModule()

@app.route('/')
def home():
	return um.home()
from app import app
# from flask_compress import Compress
#import os

#app.config.from_pyfile(os.path.join(".", "config.cfg"), silent=False)
# Compress(app)
#app.jinja_env.auto_reload = True
#app.secret_key = app.config.get('SECRET_KEY')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=9090, threaded=True, use_reloader=True)
   # app.run()

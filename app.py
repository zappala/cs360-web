import sys

from views import fall2012
from views import fall2013
from views import winter2014
from views import fall2014
from views import fall2015

from flask import Flask, render_template
from flask_frozen import Freezer
# from flaskext.markdown import Markdown
from flask.ext.misaka import Misaka

from config import app, freezer

# Markdown(app)
Misaka(app,fenced_code=True)

@app.route('/',defaults={'directory':None,'page':'index'})
@app.route('/<page>',defaults={'directory':None})
@app.route('/<path:directory>/',defaults={'page':'index'})
@app.route('/<path:directory>/<page>')
def show(directory,page):
    try:
        if not directory:
            return render_template(page + '.html', active='home')
        try:
            prev = directory.split('/')[-1]
        except:
            prev = None
        return render_template(directory+"/" + page + '.html', active=page, previous=prev)
    except:
       return render_template('404.html'), 404

@freezer.register_generator
def custom404():
    yield '/404'

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.debug = True
        app.run(port=8080)

import sys

from views import fall2012

from flask import Flask, render_template
from flask_frozen import Freezer

from config import app

@app.route('/',defaults={'directory':None,'page':'index'})
@app.route('/<directory>',defaults={'page':''})
@app.route('/<path:directory>/',defaults={'page':'index'})
@app.route('/<path:directory>/<page>')
def show(directory,page):
    if not directory:
        return render_template(page + '.html')
    if not page:
        return render_template(directory+'.html')
    return render_template(directory+"/" + page + '.html')
    

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.debug = True
        app.run(port=8080)

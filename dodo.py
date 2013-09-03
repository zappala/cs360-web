def task_install():
    """install """
    return {
        'actions': ['python app.py build','rsync -rav --delete build/* zappala@cs360.byu.edu:/var/www/cs360.byu.edu'],
        }

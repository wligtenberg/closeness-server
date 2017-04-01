# closeness-server
A Flask-diamond based server to be used with the closeness-android app.

## How to deploy
Ensure that you have virtualenvwrapper installed

    workon closeness
    mkvirtualenv -a . closeness
    pip install Flask-Diamond
    make test db server

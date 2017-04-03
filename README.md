# closeness-server
A Flask-diamond based server to be used with the closeness-android app.

The social thermoregulation app can be used in experience sampling studies to measure individual regulation or co-regulation of temperature in human participants. The app was designed to test Social Thermoregulation Theory ([IJzerman & Hogerzeil, 2017](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2844963); [IJzerman et al., 2015](http://journal.frontiersin.org/article/10.3389/fpsyg.2015.00464/full)) and is ultimately intended to be applied in the real world in social thermoregulation therapy ([IJzerman, Heine, Nagel, & Pronk, 2017](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2808019)). 

If you want to use this app for your own research (and build on the app for novel use), please refer to it as: 

IJzerman, H., Ligtenberg, W., & Verbeke, W. (2017). The Social Thermoregulation App. Available at Github: https://github.com/wligtenberg/closeness-android. 

## How to deploy
Ensure that you have virtualenvwrapper installed

    workon closeness
    mkvirtualenv -a . closeness
    pip install Flask-Diamond
    make test db server

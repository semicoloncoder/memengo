from flask import Flask, render_template
import requests, os
from typing import Final

APP_NAME: Final = 'Memengo'

app = Flask(__name__, static_folder = 'assets')

# getAMeme
def getAMeme():
    memeInfo = None

    try:
        response = requests.get('https://meme-api.herokuapp.com/gimme/wholesomememes')

        if response and response.ok and response.status_code == 200:
            jsonResponse = response.json()

            if jsonResponse and type(jsonResponse) is dict and 'preview' in jsonResponse:
                memeFileName = os.path.basename(jsonResponse['url'])

                memeInfo = {
                    'dispURL': jsonResponse['preview'][-2],
                    'postTitle': jsonResponse['title'],
                    'postLink': jsonResponse['postLink'],
                    'postSubReddit': jsonResponse['subreddit'],
                    'postAuthor': jsonResponse['author'],
                    'downloadLink': jsonResponse['preview'][-1],
                }

                if memeFileName:
                    memeInfo['memeFileName'] = memeFileName
    except Exception as e:
        memeInfo = None

    return memeInfo
# getAMeme

# indexPage
@app.route('/')
def indexPage():
    memeInfo = getAMeme()

    return render_template(
        'indexPage.template.html',
        appName = APP_NAME,
        memeInfo = memeInfo,
    )
# indexPage

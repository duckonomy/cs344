from __future__ import print_function
from tensorflow.keras.models import model_from_json
from tensorflow.keras.optimizers import Adam

import pandas as pd
import numpy as np

from urllib.request import urlopen
import json
import io
import random
import sys
from flask import Flask, render_template, request, Response, jsonify

app = Flask(__name__)

load_weights_dcinside = 'models/model-dcinside.h5'
load_model_dcinside = 'models/model.json'
data_file_dcinside = 'models/dcinside.json'

load_weights_opgg = 'models/model-opgg.h5'
load_model_opgg = 'models/model.json'
data_file_opgg = 'models/opgg.json'

data_new = {}
data_title = {}
data_content = {}

with open(data_file_dcinside, encoding='utf-8') as json_file:
    j = 0

    data = json.load(json_file)

    for i in data:
        title = i['title']
        title = [c for c in title if '\xa0' not in c]
        title = [c for c in title if '\n' not in c]
        title = [c for c in title if 'jpg' not in c]
        title = [c for c in title if 'gif' not in c]
        title = [c for c in title if 'fact' not in c]
        title_str = ''.join(map(str, title))
        data_title[str(j)] = title_str.strip()
        content = i['content']
        content = [c for c in content if 'http' not in c]
        content = [c for c in content if '\xa0' not in c]
        content = [c for c in content if '\n' not in c]
        content = [c for c in content if '- dc official App' not in c]
        content = [c for c in content if '\.jpg' not in c]
        content = [c for c in content if '\.gif' not in c]
        content = [c for c in content if '\.' not in c]
        content_str = ''.join(map(str, content))
        data_content[str(j)] = content_str.strip()
        j += 1

    data_new['title'] = data_title
    data_new['content'] = data_content

json_final = json.dumps(data_new, ensure_ascii=False)

df = pd.read_json(json_final)
title_text_arr = df['title'].to_numpy()
content_text_arr = df['content'].to_numpy()


text = df['content'].str.lower()
text_content = df['title'].str.lower()

text = text.append(text_content)

text = text.map(lambda s: ' '.join([x for x in s.split() if 'http' not in x]))
text = text.map(lambda s: ' '.join([x for x in s.split() if 'gif' not in x]))
text = text.map(lambda s: ' '.join([x for x in s.split() if 'jpg' not in x]))
text = text.map(lambda s: ' '.join([x for x in s.split() if 'fact' not in x]))
text = text.map(lambda s: ' '.join([x for x in s.split() if '\.' not in x]))
text = text.map(lambda s: ' '.join([x for x in s.split() if '\u200b' not in x]))

text = text[text.map(len) > 13]

chars = sorted(list(set(''.join(text))))
print('total chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

maxlen = 20
step = 2

json_file = open(load_model_dcinside, 'r')
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights(load_weights_dcinside)
print("Loaded model from disk")

optimizer = Adam()
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

def blacklist_contains(blacklist, seed):
    for i in blacklist:
        if i in seed[-2:]:
            return True
    return False

blacklist = [
    "어",
    "듬",
    "음",
    "슴",
    "지",
    "삼",
    "듯",
    "음",
    "야",
    "럼",
    "옴",
    "임",
    "며",
    "좀",
    "김",
    "ㄷㄷ",
    "림",
    "금"
    "구나",
    "조음",
    "웃김",
    "ㅅㄱ",
    "나",
    "ㅋㅋ",
    "들아",
    "다",
    "네",
    "있노",
    "냐",
    "냐고",
    "점",
    "함",
    "네ㅔ",
    "셈",
    "앗서",
    "자",
    "써",
    "ㄹㅇ",
    "데",
    "요",
    "라",
    "퍼",
    "중",
    "됨",
    "셈",
    "ㅜㅜ",
    "ㅎㅎ",
    "까",
    "짐",
    "당",
    "님",
    "분",
    "니",
    "햇",
    "가",
    "죠",
    "잖아",
    "븃"]

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def generate_w2_seed(sentence, diversity):
    sentence = sentence[0:maxlen]
    generated = ''
    # generated += sentence

    sys.stdout.write(generated)

    for i in range(40):
        x_pred = np.zeros((1, maxlen, len(chars)))
        for t, char in enumerate(sentence):
            x_pred[0, t, char_indices[char]] = 1.

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, diversity)
        next_char = indices_char[next_index]

        generated += next_char
        sentence = sentence[1:] + next_char

    return generated

print('Model loaded. Check http://127.0.0.1:5000/')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/generate', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        print(request.json)

        my_title = random.choice(list(text))
        my_content = random.choice(list(text))

        while True:
            if (blacklist_contains(blacklist, my_content)):
                my_content = random.choice(list(text))
            else:
                break

        while True:
            if (blacklist_contains(blacklist, my_title)):
                my_title = random.choice(list(text))
            else:
                break

        title = generate_w2_seed(my_title, 0.2)
        content = generate_w2_seed(my_content, 0.2)

        return jsonify(title=title, content=content)

    return None


if __name__ == '__main__':
    app.run(port=5000, threaded=False, debug=True)

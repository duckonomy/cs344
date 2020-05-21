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

weight_path = 'models/model-dcinside.h5'
model_path = 'models/model.json'
data_path = 'models/dcinside.json'

data_new = {}
data_title = {}
data_content = {}

char_length = 0
text = []
chars = []
char_indices = {}
indices_char = {}

max_sequence_length = 20
step = 2

def select_data(model_str):
    if (model_str == 'opgg'):
        weight_path = 'models/model-opgg.h5'
        model_path = 'data_path'
        data_path = 'models/opgg.json'
        print("OP.GG")
    else:
        weight_path = 'models/model-dcinside.h5'
        model_path = 'models/model.json'
        data_path = 'models/dcinside.json'
        print("DCINSIDE")


        with open(data_path, encoding='utf-8') as json_file:
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

            global text

            text = df['content'].str.lower()
            text_content = df['title'].str.lower()

            text = text.append(text_content)

            text = text.map(lambda s: ' '.join([x for x in s.split() if '\u200b' not in x]))

            # Eliminate text that isn't as long
            text = text[text.map(len) > 13]

            global chars
            global char_indices
            global indices_char
            # Map the characters bidirectionally for encoding
            chars = sorted(list(set(''.join(text))))
            char_indices = dict((c, i) for i, c in enumerate(chars))
            indices_char = dict((i, c) for i, c in enumerate(chars))

            chars_length = len(chars)

def create_model():
    json_file = open(model_path, 'r')
    model_json = json_file.read()

    json_file.close()
    model = model_from_json(model_json)
    model.load_weights(weight_path)
    print("Loaded model from disk")

    optimizer = Adam()
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)
    return model

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
    "림",
    "금"
    "나",
    "네",
    "다",
    "점",
    "함",
    "셈",
    "자",
    "써",
    "데",
    "요",
    "라",
    "퍼",
    "중",
    "됨",
    "셈",
    "까",
    "짐",
    "당",
    "님",
    "분",
    "니",
    "햇",
    "가",
    "냐",
    "븃",
    "죠",
    "구나",
    "조음",
    "웃김",
    "들아",
    "있노",
    "냐고",
    "앗서",
    "잖아",
    "ㅅㄱ",
    "ㅋㅋ",
    "ㄹㅇ",
    "ㄷㄷ",
    "ㅜㅜ",
    "ㅎㅎ",
    "네ㅔ",
]

def sample(predictions, temperature=0.2):
    predictions = np.asarray(predictions).astype('float64')
    predictions = np.log(predictions) / temperature
    exp_preds = np.exp(predictions)
    predictions = exp_preds / np.sum(exp_preds)
    probabilities = np.random.multinomial(1, predictions, 1)
    return np.argmax(probabilities)

# Similar to print_current_model() in lstm_train.ipynb
def generate_text(sequence, diversity, model):
    sequence = sequence[0:max_sequence_length]
    generated = ''
    generated += sequence

    sys.stdout.write(generated)

    for i in range(20):
        x_pred = np.zeros((1, max_sequence_length, len(chars)))
        for t, char in enumerate(sequence):
            x_pred[0, t, char_indices[char]] = 1.

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, diversity)
        next_char = indices_char[next_index]

        generated += next_char
        sequence = sequence[1:] + next_char

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
        select_data(request.json['community'])
        print(text)
        model = create_model()

        title_seed = random.choice(list(text))
        content_seed = random.choice(list(text))

        while True:
            if (blacklist_contains(blacklist, content_seed)):
                content_seed = random.choice(list(text))
            else:
                break

        while True:
            if (blacklist_contains(blacklist, title_seed)):
                title_seed = random.choice(list(text))
            else:
                break

        title = generate_text(title_seed, 0.2, model)
        content = generate_text(content_seed, 0.2, model)

        return jsonify(title=title, content=content)

    return None


if __name__ == '__main__':
    app.run(port=5000, threaded=False, debug=True)

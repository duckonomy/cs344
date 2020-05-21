import pandas as pd
import json

import re
import base64

import numpy as np

from PIL import Image
from io import BytesIO


def clean_data(file_in, file_out):
    data_new = {}

    with open(file_in, encoding='utf-8') as json_file:
        data = json.load(json_file)
        data_title = {}
        data_content = {}
        j = 0

    for i in data:
        data_title[str(j)] = i['title']
        content = i['content']
        content = [c for c in content if 'http' not in c]
        content = [c for c in content if '\xa0' not in c]
        content_str = ''.join(map(str, content))
        data_content[str(j)] = content_str
        j += 1

    data_new['title'] = data_title
    data_new['content'] = data_content

    with open(file_out, 'w', encoding='utf-8') as outfile:
        json.dump(data_new, outfile, ensure_ascii=False)

def base64_to_pil(img_base64):
    """
    Convert base64 image data to PIL image
    """
    image_data = re.sub('^data:image/.+;base64,', '', img_base64)
    pil_image = Image.open(BytesIO(base64.b64decode(image_data)))
    return pil_image


def np_to_base64(img_np):
    """
    Convert numpy image (RGB) to base64 string
    """
    img = Image.fromarray(img_np.astype('uint8'), 'RGB')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return u"data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode("ascii")


if __name__ == "__main__":
    clean_data('ilbe-other.json', 'ilbe-other-clean.json')
    df = pd.read_json('ilbe-other-clean.json')
    print(df.head(33))

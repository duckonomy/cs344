# Korean Online Community Website Post Generator

## Vision
Like my primary influence, the Microsoft Twitter bot, Tay, I wanted to generate text that reflected the culture of an online community. Because I wanted to capture the style of certain online communities through a machine learning model, I needed a comprehensive platform to easily do that. So, in addition to creating a nice model that generates somewhat structured text, I concocted a loose framework that has most of what one would need to build a text generator for an online community site. The pieces I used to accomplish this are listed below. Furthermore, to add some spice to the project, I attempted to generate Korean, my native language.

## Primary libraries used
 - [Scrapy](https://scrapy.org/): This was used to scrape the dataset for generating the posts.
 - [Keras](https://keras.io/): This is what I built my primary LSTM model with.
 - [KoGPT2](https://github.com/SKT-AI/KoGPT2)/[transformers](https://github.com/huggingface/transformers): This was more for playing around. I included it in this list because I also include the source to what I did. I also include the library itself as a git submodule just in case.
 - [Flask](https://flask.palletsprojects.com/en/1.1.x/): This is a really nice python web framework that is useful for prototyping tools made with python. I will use this for my demonstration and it is the preferred way to check out my model.

## Sites I scraped from
 - DCInside's Comic Gallery/Board: https://gall.dcinside.com/board/lists?id=comic_new2
   - DCInside is the Reddit of Korea. It is notoriously for creating a lot of issues on Korea's internet.
 - Talk OP GG's League of Legends Board: https://talk.op.gg/s/lol
   - Op.gg is a game analysis site that also has a vibrant community in its discussion board.

## Running the code
My main demonstration is through the Flask web application that reads in my model and its weights.

First you want to create a virtual environment.
```
python -m venv path-to-environment
```

Once created, source/activate that environment.

```
source path-to-environment/bin/activate
```

Then install the packages in the `requirements.txt` file.

```
pip install -r requirements.txt
```

If you need to run the `gpt2.ipynb` notebook you should also install the submodule and `pip install` that folder.
However, this is not officially part of the primary demonstration.

```
git submodule update
pip install ./KoGPT2
```

Otherwise, once you're in the virtual environment, you can run your notebook.

```
jupyter notebook
```

Or you could go into the `api/` directory and run
```
python app.py
```

Then a web server should run on port 5000 (`http://localhost:5000` from your browser)

There you can start generating text with the model.

## The Dataset  
I included the dataset with the repository (around 17mb in total) for ease of use with the website, which is how I will showcase my project. It is located in `api/models/`

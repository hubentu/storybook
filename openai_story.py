import openai
import streamlit as st
import urllib.request
from PIL import Image

# Set up the OpenAI API client
openai.api_key = st.secrets["key"]

def gen_story(prompt):
    # Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = "make a story for kids. {}".format(prompt)
    
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    #print(response)
    return response

def gen_img(prompt, path="/tmp/story.png"):
    ## img
    prompt = "children comic, picture book, illustration. cute eyes, detail face, not scary. {}".format(prompt)
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    urllib.request.urlretrieve(image_url, path)
    return path


prompt = st.sidebar.text_area("Start your story:")
start = st.sidebar.button("Submit")

if start:
    story = gen_story(prompt) 
    st.write(story)

    img_url = gen_img(prompt)
    image = Image.open(img_url)
    st.image(image)

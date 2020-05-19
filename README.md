# RESTful Wiki Entity Extractor
 
A simple Flask REST API for extracting entities from wikipedia pages. Useful for constructing knowledge graphs over a set of wikipedia pages. Do not use anything here in production!

## To use the app, you have two options: Dockerfile or source

1. Dockerfile
The Dockerfile that exists here will build most of what you need, but it requires some manual work right now. I'll upload instructions soon for how to use it.

2. Source
Having `conda` installed, you can run `conda env create -f environment.yml` in this repo. From there, activate your environment with `conda activate entity-env`. In the environment, cd into `app/`, and then run `python app.py`. Ta-da! Your app should now be running on localhost.

## Accessing the data

This app expects a GET request looking like:
```json
{
    "data": "https://en.wikipedia.org/wiki/Manhattan_Project"
}
```

The endpoint you want is `/wiki-entities`.



### Thanks for reading! I'll update soon with more thorough examples of usage. 

# -*- coding: utf-8 -*-
import spacy
import json
import logging

from bs4             import BeautifulSoup
from wikipedia_utils import import_url_data, format_content

nlp    = spacy.load('en_core_web_sm')
logger = logging.getLogger(__name__)


def get_wiki_entities(url):
    response = {}
    # test url = "https://en.wikipedia.org/wiki/Manhattan_Project"

    page_data = import_url_data(url)
    logger.info('Getting page data...')
    if page_data is not None:
        parsed    = BeautifulSoup(page_data, 'html.parser')
        sentences = format_content('p', parsed_html=parsed)

        ents, labels = [], []
        for sent in nlp.pipe(sentences):
            new_entities = list(sent.ents)
            labels += [str(e.label_) for e in new_entities]
            ents   += [str(e)        for e in new_entities]

        response['response_data'] = {
            "entities":  ents,
            "ent_types": labels
        }

    else:
        error_message = 'Page not found'
        logger.info(error_message)
        response['error'] = {
            "message": error_message,
        }

    return json.dumps(response)

# -*- coding: utf-8 -*-
import logging
from flask import Flask, request
from wiki_parser import get_wiki_entities

logger  = logging.getLogger(__name__)
app     = Flask(__name__)


@app.route('/')
def main():
    return "<h1>Main</h1>"


@app.route("/wiki-entities", methods=['POST', 'GET'])
def wik():
    """
    Request format
    {
        "data": "https://en.wikipedia.org/wiki/Manhattan_Project"
    }
    """
    if request.method == 'GET':
        if "data" in request.args.keys():
            req_path = request.args.get('data')
            logger.info(f"Request for data at url: {req_path}")
            response = get_wiki_entities(req_path)
            return response
        else:
            return {'error': f"bad GET {request.json}"}
    else:
        return "<h1>Nothing to see here</h1>"


if __name__ == "__main__":
    """
    This keeps things running.
    Make debug=False if this ever faces 
    outward. debug=True isn't safe outside of
    development.
    """

    app.run(debug=True)

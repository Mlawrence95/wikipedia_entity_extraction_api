import re
import logging
import requests
import contextlib

from typing import Iterable
# global regex for cleaning tags out of wikipedia text
reference_tags = re.compile(r'\[\d+\]')
logger         = logging.getLogger(__name__)


def import_url_data(url):
    try:
        with contextlib.closing(requests.get(url)) as webpage_response:
            if webpage_response:
                logger.info(f'Received data from {url}')
                return webpage_response.content
            else:
                logger.info(f'Failed to receive data for {url}')
                return None
    except Exception as e:
        logger.info(f'Import of data from {url} failed with exception: ')
        logger.exception(e)
        return None


def format_content(tag_type, parsed_html) -> Iterable[str]:
    formatted_outputs = []
    html_subset = parsed_html.select(tag_type)
    if len(html_subset) > 0:
        for section in html_subset:
            section = section.text.replace('\xa0', ' ')
            section = reference_tags.sub('', section)
            section = section.strip()

            if len(section) > 0:
                formatted_outputs += [section]

    return formatted_outputs

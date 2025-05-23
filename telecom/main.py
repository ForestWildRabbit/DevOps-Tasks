
import requests
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

status_code_ranges = {'100-103', '200-226', '300-308', '400-499', '500-561'}

for i, status_code_range in enumerate(status_code_ranges):

    request_number = i + 1

    try:
        response = requests.get(f'https://httpstat.us/random/{status_code_range}', timeout=5)
    except requests.exceptions.ReadTimeout:
        raise Exception(f'Request {request_number} timed out')

    if response.status_code < 400:
        logging.info('Request #%d', request_number)
        logging.info('STATUS CODE: %s', response.status_code)
        logging.info('HEADERS: %s', response.headers)
        logging.info('RESPONSE BODY: %s', response.text)

    else:
        logging.info('Request #%d', request_number)
        logging.error('STATUS CODE: %s', response.status_code)
        raise Exception(f'STATUS CODE: {response.status_code}')



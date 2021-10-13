from django.conf import settings
from decouple import config
from dateutil.parser import parse

from apps.utils.service_mock import ServiceMock
from apps.api import models

from datetime import datetime, timedelta
import logging
import requests
import json
import logging

logger = logging.getLogger(__name__)


class RestAbstraction:

    def __init__(self):
        """
            Initialize the variables end_date reuse on the methods
        """

        self.base_url = config("URL_MB", "http://localhost:8000/api/")

    def get_mb_candles(self, pair, initial_date, end_date):
        """
            Get a list of addressess based on a date range
        """

        if settings.DEBUG:
            return ServiceMock().get_mb_candles_mock({})

        response = requests.get(
            url=self.base_url + "/{}/candle?from={}&to={}&precision=1d".format(pair, initial_date, end_date),
            verify=False,
            headers={
                "Content-Type": "application/json; charset=utf-8"
            })

        return json.loads(response.content)


class Format():
    
    @staticmethod
    def limit_string_size(string, tam):
        if isinstance(string, str):
            return string[:tam]
        return string

    @staticmethod
    def format_error_limit_string(**kwargs):
        err = {
            "error": [{
                "code": kwargs["code"],
                "title": Format.limit_string_size(kwargs["title"], 60),
                "description": Format.limit_string_size(kwargs["description"], 255)
            }]
        }
        return err

    @staticmethod
    def format_date(timestamp):
        formated_date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
        formated_date = datetime.strptime(formated_date, '%Y-%m-%d')
        return formated_date

    @staticmethod
    def get_today():
        formated_date = datetime.now() - timedelta(days=365)
        formated_date = formated_date.timestamp()
        return formated_date
    
    @staticmethod
    def get_yesterday():
        formated_date = datetime.now() - timedelta(days=1)
        formated_date = formated_date.timestamp()
        return formated_date


class Validate():
    
    @staticmethod
    def validate_parameters(pair, mms=None, initial_date=None, end_date=None, range_days=None):
        initial_date = Format.format_date(initial_date)
        date_between = datetime.now() - initial_date
        initial_date = date_between.days

        logger.info(('pair: {} - mms: {} - '
                    'initial_date: {} - end_date: {} - '
                    'range_days: {}'.format(pair, mms, initial_date, end_date, range_days)))

        if pair not in ['BRLBTC', 'BRLETH']:
            logger.error('INVALID PAIR: {}'.format(pair))
            return Format.format_error_limit_string(
                code=400,
                title="INVALID PAIR",
                description="Please enter a valid PAIR, accepted pairs are BRLBTC and BRLETH."
            )

        if range_days not in [20, 50, 200]:
            logger.error('INVALID RANGE: {}'.format(range_days))
            return Format.format_error_limit_string(
                code=400,
                title="INVALID RANGE",
                description="Please insert a valid RANGE, accepted ranges are 20, 50 and 200."
            )

        if  initial_date < 365:
            logger.error('INVALID FROM - LESS THAN 365: {}'.format(initial_date))
            return Format.format_error_limit_string(
                code=400,
                title="INVALID FROM",
                description="Please enter a valid FROM, accepted from are more than 365 days - number of days {}.".format(initial_date)
            )

        return True


class QuerySaveApi():

    @staticmethod
    def save_db_price(pair, initial_date, end_date, range_days):

        rest = RestAbstraction()
        result = rest.get_mb_candles(pair, initial_date, end_date) 
        logger.info('result: {}'.format(result))

        try:
            candles = result.get('candles')

            i = 0
            list_close = []

            while i < len(candles):
                timestamp = candles[i]['timestamp']
                close = candles[i]['close']

                list_close.append(close)
                avg_group = sum(list_close) / range_days

                pair = models.Pair.objects.get(description=pair, range_days=range_days)
                
                obj = models.Price()
                obj.pair = pair
                obj.mms = avg_group
                obj.timestamp = timestamp
                obj.save()
                
                i += 1

            return True

        except Exception as e:
            logger.debug(str(e))
            return False
                

class FloatUrlParameterConverter:
    regex = '[0-9]+\.?[0-9]+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)
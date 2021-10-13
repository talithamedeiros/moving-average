from celery.task.schedules import crontab
from celery.decorators import periodic_task

from apps.api import models
from apps.utils.views import QuerySaveApi

import logging

logger = logging.getLogger(__name__)

@periodic_task(run_every=crontab(minute=0, hour='5'), name="insert_price_db", ignore_result=True)
def insert_price_db():
    initial_date = '1577836800'
    end_date = '1606565306'
    
    logger.debug("initial_date: {} - end_date: {}".format(initial_date, end_date))

    for pair in models.Pair.objects.all():
        query = QuerySaveApi()
        result = query.save_db_price(pair.description, initial_date, end_date, pair.range_days)

        logger.debug('result', result)
        

    return(initial_date)
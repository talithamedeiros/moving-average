from django.conf import settings
from rest_framework import status, views
from rest_framework.response import Response

from django.conf import Settings

from timeit import default_timer as timer
from datetime import timedelta
import logging

from apps.api import models
from apps.utils.views import Validate, Format
from apps.utils.service_mock import ServiceMock
import logging

logger = logging.getLogger(__name__)


class RangeMeasureView(views.APIView):
    """
        .
    """
    def get(self, request, *args, **kwargs):
        total_time_start = timer()

        mms = kwargs.get("mms", "")

        end_date = Format.get_yesterday()
        end_date = int(request.query_params.get("to", end_date))

        try:
            pair = kwargs.get("pair", "")
            initial_date = int(request.query_params.get("from", ""))
            range_days = int(request.query_params.get("range", ""))
        except:
            logger.error('Invalid required parameters')
            return Response(Format.format_error_limit_string(
                                error=400,
                                title="INVALID REQUIRED PARAMENTERS",
                                description="Please enter the required parameters."
                            ),
                            status=status.HTTP_400_BAD_REQUEST,
                            content_type='application/json; charset=utf-8')

        validate_params = Validate.validate_parameters(pair, mms, initial_date, end_date, range_days)

        if validate_params is not True:
            return Response(validate_params,
                            status=status.HTTP_400_BAD_REQUEST,
                            content_type='application/json; charset=utf-8')

        if settings.DEBUG:
            mock = ServiceMock().range_measure_mock([])
            return Response(mock,
                        status=status.HTTP_200_OK,
                        content_type='application/json; charset=utf-8')
        
        price_obj = models.Price.objects.filter(pair__description=pair, 
                                                pair__range_days=range_days)

        prices = []
        for obj in price_obj:
            prices.append({
                "timestamp": int(obj.timestamp),
                "mms": float(obj.mms)
            })
        total_time_end = timer()
        
        total_time = str(timedelta(seconds=total_time_end-total_time_start))
        logger.info('total_time: {}'.format(total_time))

        return Response(prices,
                        status=status.HTTP_200_OK,
                        content_type='application/json; charset=utf-8')
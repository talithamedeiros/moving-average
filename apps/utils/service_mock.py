import logging
import json

logger = logging.getLogger(__name__)


class MockedResponse:

    def __init__(self):
        self.content = {}
        self.status_code = 200


class ServiceMock:
    """Mocked data for LOCAL envs
    """

    @staticmethod
    def get_mb_candles_mock(data):
        result = MockedResponse()
        result.content = json.loads(json.dumps({
                "status_code":100,
                "status_message":"Success",
                "server_unix_timestamp":1612689940,
                "candles":[
                    {
                        "timestamp":1577836800,
                        "open":29288.89999,
                        "close":29199,
                        "high":29398.99999,
                        "low":29100,
                        "volume":16.36533085
                    },
                    {
                        "timestamp":1577923200,
                        "open":29199,
                        "close":28200.58005,
                        "high":29999.99,
                        "low":28100,
                        "volume":143.68446981
                    },
                    {
                        "timestamp":1578009600,
                        "open":28200.00001,
                        "close":29776.15066,
                        "high":30350,
                        "low":28003,
                        "volume":222.27899319
                    },
                    {
                        "timestamp":1578096000,
                        "open":29929.89697,
                        "close":29761.03,
                        "high":29980,
                        "low":29611.00001,
                        "volume":37.23518071
                    },
                    {
                        "timestamp":1578182400,
                        "open":29820,
                        "close":29741,
                        "high":30200,
                        "low":29650,
                        "volume":65.53665459
                    }
                ]
            }))
        return result.content

    @staticmethod
    def range_measure_mock(data):
        result = MockedResponse()
        result.content = json.loads(json.dumps([
                    {
                        "timestamp":1577836800,
                        "mms":29288.89999
                    },
                    {
                        "timestamp":1577923200,
                        "mms":29199
                    },
                    {
                        "timestamp":1578009600,
                        "mms":28200.00001
                    },
                    {
                        "timestamp":1578096000,
                        "mms":29929.89697
                    },
                    {
                        "timestamp":1578182400,
                        "mms":29820
                    }
                ]))
        return result.content

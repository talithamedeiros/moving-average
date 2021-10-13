## API documentation

Access via swagger: `http://localhost:9000/api/`

1. Moving average endpoint

GET `/api/range-measure/{pair}/{mms}/`

Example:  `http://localhost:9000/api/range-measure/BRLBTC/10?from=1577836800&to=1606565306&range=200`
#### Query parameters
```
pair: BRLBTC and BRLETH
mms (optional): mms value
from: timestamp
to: timestramp, default: Previous day
range: 20, 50 ou 200 (days)
```

___

### Response

1. Status `200 OK`
```json
[
    {
        "timestamp": 1577836800,
        "mms": 29288.89999
    },
    {
        "timestamp": 1577923200,
        "mms": 29199
    },
    {
        "timestamp": 1578009600,
        "mms": 28200.00001
    },
    {
        "timestamp": 1578096000,
        "mms": 29929.89697
    },
    {
        "timestamp": 1578182400,
        "mms": 29820
    }
]
```

2. Exception example
```json
{
    "error": [
        {
            "code": 400,
            "title": "INVALID FROM",
            "description": "Please enter a valid FROM, accepted from are more than 365 days - number of days 500."
        }
    ]
}
```
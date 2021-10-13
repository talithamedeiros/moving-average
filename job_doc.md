## Job documentation

### Schema

**Pair**

| Field | Type |   
|---|---|
| description  | CharField |
| range_days  | IntegerField |


**Price**

| Field | Type |   
|---|---|
| pair  | FK |
| mms  | CharField |
| timestamp  | CharField |


### Daily Table Increment

Job is done daily at 5am. Celery and Redis were used to call the Mercado Bitcoin API, calculate the mms and insert the data in the Price table.


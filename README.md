# Simple Moving Average Variation

Service that returns simple moving averages, from 20, 50 and 200 days, of the Bitcoin and Etherium currencies that are listed on Mercado Bitcoin.

## Prerequisites

* Docker

## Running

1. Clone repo

`git clone https://github.com/talithamedeiros/moving-average`

2. Set environment variables

`mv sample.env .env`

3. Build and start

`docker-compose up -d --build`

4. Migrate database

`docker-compose run --rm application python3 manage.py migrate`

5. Collect statics

`docker-compose run --rm application python3 manage.py collectstatic --no-input`

6. Insert data on Pair table

`docker-compose run --rm application python3 manage.py loaddata moving_average/fixtures/*`

___

* [Job documentation](https://github.com/talithamedeiros/moving-average/blob/master/job_doc.md)
* [API Documentation](https://github.com/talithamedeiros/moving-average/blob/master/api_doc.md)


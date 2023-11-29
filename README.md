
## Build docker image
```
$ docker build -t mysite .
```

## Start docker compose
```
$ docker compose up -d
```

## Exec inside mysite
```
$ docker exec -it mysite bash
```

## Inside the container, Migration and seed data
```
$ python manage.py migrate
$ python manage.py seedorders
```

## Assignment
```
$ python manage.py select_cancelled_orders
```

Results of both 2 task: Using ORM & Optimized solution. Source code of the assignment can be found at directory `mysite/order`

```
# python manage.py select_cancelled_orders
=============== USING ORM ===========
{'Order': 1, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 846586, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
{'Order': 2, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 850849, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
{'Order': 4, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 856949, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
{'Order': 5, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 860920, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
{'Order': 7, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 866761, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
{'Order': 8, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 870360, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
{'Order': 10, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 878309, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
{'Order': 11, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 885620, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
{'Order': 13, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 897295, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
{'Order': 14, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 903881, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
{'Order': 16, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 913691, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
{'Order': 17, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 920104, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
{'Order': 19, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 929217, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
{'Order': 20, 'Created': datetime.datetime(2023, 11, 29, 9, 12, 26, 933311, tzinfo=datetime.timezone.utc), 'Status': 'CANCELLED'}
=============== USING Optimized Models ===========
{'ID': 1, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 26, 937527, tzinfo=datetime.timezone.utc)}
{'ID': 2, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 26, 946897, tzinfo=datetime.timezone.utc)}
{'ID': 4, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 26, 959858, tzinfo=datetime.timezone.utc)}
{'ID': 5, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 26, 969516, tzinfo=datetime.timezone.utc)}
{'ID': 7, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 26, 983764, tzinfo=datetime.timezone.utc)}
{'ID': 8, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 26, 995119, tzinfo=datetime.timezone.utc)}
{'ID': 10, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 27, 10724, tzinfo=datetime.timezone.utc)}
{'ID': 11, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 27, 21921, tzinfo=datetime.timezone.utc)}
{'ID': 13, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 27, 36888, tzinfo=datetime.timezone.utc)}
{'ID': 14, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 27, 47304, tzinfo=datetime.timezone.utc)}
{'ID': 16, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 27, 60047, tzinfo=datetime.timezone.utc)}
{'ID': 17, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 27, 69649, tzinfo=datetime.timezone.utc)}
{'ID': 19, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 27, 80121, tzinfo=datetime.timezone.utc)}
{'ID': 20, 'LatestStatus': 'CANCELLED', 'LatestStatusAt': datetime.datetime(2023, 11, 29, 9, 12, 27, 88572, tzinfo=datetime.timezone.utc)}
```

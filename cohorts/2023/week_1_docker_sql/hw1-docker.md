# HW1

# docker

1.

```bash
$ docker build --help | grep iid
--iidfile string          Write the image ID to the file
```

2.

```bash
$ docker run -it --entrypoint bash python:3.9
root@0168d51a6f90:/# pip list
Package    Version
---------- -------
pip        22.0.4
setuptools 58.1.0
wheel      0.38.4
```

3.

```bash
docker build -t green_taxi:v001 -f Dockerfile-green .

docker run -it \
	--network=2_docker_sql_default \
	green_taxi:v001 \
	--user=root \
	--password=root \
	--host=pgdatabase \
	--port=5432 \
	--db=ny_taxi \
	--table_name=green_taxi_trips \
	--url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz"

```

```sql
select count(1)
from green_taxi_trips
where date(lpep_pickup_datetime) = '2019-01-15'
	and date(lpep_dropoff_datetime) = '2019-01-15'
;
```

20530

4.

```sql
select 
	date(lpep_pickup_datetime) dt
	,max(trip_distance) distance
from green_taxi_trips
group by date(lpep_pickup_datetime)
order by 2 desc
;
```

2019-01-15 117.99

5.

```sql
select 
	passenger_count
	,count(index)
from green_taxi_trips
where date(lpep_pickup_datetime) = '2019-01-01'
group by passenger_count
;
```

2: 1532 ; 3: 126


6.

```sql
select 
	zdo."Zone"
	,t."tip_amount" 
from green_taxi_trips t
join zones zpu
	on t."PULocationID" = zpu."LocationID"
join zones zdo
	on t."DOLocationID" = zdo."LocationID"
where zpu."Zone" = 'Astoria'
order by t."tip_amount" desc;
;
```

Long Island City/Queens Plaza

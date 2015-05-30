This sample demonstrates how to setup continuous integration for a Python+Redis project.

This sample is built for DaoCloud, a docker based continuous integration and deployment platform.

## Default Redis Connection that recommand link a redis docker with 'redis' alias
* REDIS_PASSWORD = /* don't need password by default */
* REDIS_PORT_6379_TCP_ADDR=localhost
* REDIS_PORT_6379_TCP_PORT=6379

## Run Container
docker run --link your_redis:redis -p 3000:3000 python-redis-sample

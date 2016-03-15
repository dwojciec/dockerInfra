# dockerInfra

docker compose build
docker compose up

docker run -it --link reloca/mongodb --rm mongo sh -c 'exec mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT/test"'

to connect to your Mongodb container
docker exec -it reloca_db_1 bash
docker exec -it reloca_db_1 tail -f /var/log/mongodb/mongod.log

docker exec -it reloca_db_1 mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT"

Issue found with --volumes option for Mongodb :

2016-03-14T15:45:13.313+0000 E STORAGE  [initandlisten] WiredTiger (22) [1457970313:313814][1:0x7fd837f7ddc0], connection: ���: fsync: Invalid argument
2016-03-14T15:45:13.315+0000 I -        [initandlisten] Fatal Assertion 28561
2016-03-14T15:45:13.315+0000 I -        [initandlisten]

docker run --name mongodbtest -d --restart=always --publish 27018:27017 --volume /Users/didierwojciechowski/RELOCA/mongodb:/var/lib/mongo reloca/mongodb
see https://github.com/mvertes/docker-alpine-mongo/issues/1


# Inserting data into our Mongodb database
docker inspect --format="{{.Config.Hostname}}" reloca_db_1

docker exec -it reloca_db_1 sh -c 'exec mongo "1417768a7c2c:27017/relocadb"'


dockhostname() {
  docker inspect --format='{{.Config.Hostname}}' "$@"
}
dockhostname reloca_db_1

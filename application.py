import os
import flask
import redis

application = flask.Flask(__name__)
application.debug = True

@application.route('/')
def hello_world():
  storage = Storage()
  storage.populate()
  score = storage.score()
  return "Hello world, %s!" % score

class Storage():
  def __init__(self):
    self.redis = redis.Redis(
      # Fields (password) have fixed value provided by image daocloud/ci-redis
      # While fields (host, port) have dynamic values, please use env vars to fetch them
      host = os.getenv('REDIS_PORT_6379_TCP_ADDR'),
      port = int(os.getenv('REDIS_PORT_6379_TCP_PORT')),
      password = ''
    )

  def populate(self):
    self.redis.set('score', '1234')

  def score(self):
    return self.redis.get('score')

if __name__ == "__main__":
  application.run(host='0.0.0.0', port=3000)

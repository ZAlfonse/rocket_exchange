# rocket_exchange

You need:
--
- python3 
- docker
- docker-compose

Steps:
--
#### Run startup script 
`python init_project.py`
It will ask you for a steam api key which you can create [here](https://steamcommunity.com/dev/apikey)

This generates an env file with your `SECRET_KEY` in a file called `env`

#### Run compose
`docker-compose up`

#### Run the migrations
`docker-compose run web migrate`

#### Make a superuser
`docker-compose run web createsuperuser`

#### Try it
[Here](http://localhost:8000/admin)

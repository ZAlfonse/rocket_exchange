# rocket_exchange

You need:
--
- python3 
- docker

Steps:
--
#### Run startup script 
`python init_project.py`
It will ask you for a steam api key which you can create [here](https://steamcommunity.com/dev/apikey)

This generates an env file with your `SECRET_KEY` in a file called `env`

#### Build the image
`docker build -t rocketexchange .`

#### Test the image
`docker run -it -v "$(pwd)"/:/usr/src/app --rm --env-file env -p 8000:8000 rocketexchange:latest`

Stop it with `ctrl+c`

#### Run the migrations
`docker run -it -v "$(pwd)"/:/usr/src/app --rm --env-file env rocketexchange:latest migrate`

#### Make a superuser
`docker run -it -v "$(pwd)"/:/usr/src/app --rm --env-file env rocketexchange:latest createsuperuser`

#### Everything should work
`docker run -it -v "$(pwd)"/:/usr/src/app --rm --env-file env -p 8000:8000 rocketexchange:latest`

#### Try it
`open index.html`

# rocket_exchange

You need:
--
- python3 
- docker

Steps:
--
#### Run `init_project.py`
This generates an env file with your `SECRET_KEY` in a file called `env`

#### Build the image
`docker build -t rocketexchange .`

#### Test the image
`docker run -it -v "$(pwd)"/:/usr/src/app --rm --env-file env -p 8000:8000 rocketexchange:latest`

Stop it with `ctrl+c`

#### Run the migrations
`docker run -it -v "$(pwd)"/:/usr/src/app --rm --env-file env rocketexchange:latest migrate`

#### Run collectstatic
`docker run -it -v "$(pwd)"/:/usr/src/app --rm --env-file env rocketexchange:latest collectstatic`

#### Load the fixture data
`docker run -it -v "$(pwd)"/:/usr/src/app --rm --env-file env rocketexchange:latest loaddata fixtures/initial.json`

#### Make a superuser
`docker run -it -v "$(pwd)"/:/usr/src/app --rm --env-file env rocketexchange:latest createsuperuser`

#### Everything should work
`docker run -it -v "$(pwd)"/:/usr/src/app --rm --env-file env -p 8000:8000 rocketexchange:latest`

Go [here](http://localhost:8000)

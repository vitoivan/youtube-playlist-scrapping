
all: dev

prod:
	@FLASK_ENV=production flask run --port=3333 --host=0.0.0.0


dev: 
	@FLASK_ENV=development flask run --port=3333 --host=0.0.0.0
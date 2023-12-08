build-base: 
	docker build -t app-base-img ./build

build: build-base
	docker build -t app-img .

start: build
	docker-compose up

stop:
	docker-compose down
	rm -rf ./data

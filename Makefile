build-base: 
	docker build -t app-base-img ./build

build: build-base
	docker build -t app-img .

start: build
	docker-compose up -d

stop:
	docker-compose down
	rm -rf ./data
	docker rmi app-image
	docker rmi app-base-image
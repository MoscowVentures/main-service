build-base: 
	docker build -t app-base-img ./build

clear: 
	docker-compose down && true
	rm -rf ./data && true
	docker rmi app-image && true
	docker rmi app-base-image && true

build: build-base
	docker build -t app-img .

start: build
	docker-compose up -d

stop: clear

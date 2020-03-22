build-images:
	docker-compose build libsvm

run-tests: build-images
	docker-compose run pytest

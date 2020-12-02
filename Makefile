PROJECT_APP_NAME=een-annotations-generator

build:
	docker build -t ${PROJECT_APP_NAME}:latest -f Dockerfile .

run:
	docker run -it ${PROJECT_APP_NAME}

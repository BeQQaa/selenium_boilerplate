clean:
	pip freeze | xargs pip uninstall -y

up:
	docker-compose -f docker-compose.yml up -d --build
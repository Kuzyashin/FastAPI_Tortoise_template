
up:
	docker-compose up -d

upb:
	docker-compose up -d --force-recreate --build

down:
	docker-compose down

connect:
	docker exec -it $(c) su

attach:
	docker container logs -f $(c)

run:
	./.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 80

up:
	docker-compose up -d

upb:
	docker-compose up -d --force-recreate --build

upb-prod-slim:
	docker-compose -f docker-compose.prod.slim.yml up -d --force-recreate --build

upb-prod-full:
	docker-compose -f docker-compose.prod.full.yml up -d --force-recreate --build

generate-slim-swarm:
	docker-compose -f docker-compose.prod.slim.swarm.yml config > docker-stack.yml

generate-full-swarm:
	docker-compose -f docker-compose.prod.full.swarm.yml config > docker-stack.yml

deploy-swarm:
	docker stack deploy --compose-file docker-stack.yml $(c)

down:
	docker-compose down

docker-network:
	docker network create --driver overlay webgateway



connect:
	docker exec -it $(c) su

attach:
	docker container logs -f $(c)

run:
	./.env/bin/uvicorn app.main:app --host 0.0.0.0 --port 80
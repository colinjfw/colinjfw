start:
	@docker run --rm -d -i \
		--name blog \
		--workdir /usr/src/app \
		-p 3000:3000 \
		-v $$PWD:/usr/src/app ruby:2.4

shell:
	@docker exec -it blog bash

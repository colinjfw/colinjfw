shell:
	@docker build -t blog .
	@docker run --rm -it \
		--name blog \
		--workdir /usr/src/app \
		-p 3000:3000 \
		-v $$PWD:/usr/src/app \
		blog \
		bash

release:
	jekyll build
	s3_website push

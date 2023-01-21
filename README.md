# functions_from_zero_lab
live training 

[![Python application test with Github Actions](https://github.com/tchuam0215/functions_from_zero_lab/actions/workflows/main.yml/badge.svg)](https://github.com/tchuam0215/functions_from_zero_lab/actions/workflows/main.yml)


### To call Microservices

We can do something like this : 
```
curl -X 'POST' \
  'https://tchuam0215-ominous-meme-64gxgv9ggvghjgr-8080.preview.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

### Build container

`docker build .`
`docker image ls`


### Run container 

something like this
`docker run -p 127.0.0.1:8080:8080 d4c15acf0259`

### Invoque your POST request 

`bash invoque.sh`
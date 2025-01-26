# For local debugging

## SSH Session to the EC2

```
ssh -i /home/diego/ssh_keys/deep-learning-kp.pem -L 8888:localhost:8888 ubuntu@<public_ipv4_
```


## Docker on the EC2 SSH Session 
 `List all docker containers on server, running or not running`

```bash
docker ps -a 
```

 - Example output





 `Re-run stopped docker containers (containing ollama)`

``` bash
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

# Command to see if ollama is running

```
REST API

curl http://<ipv4_address>:11434/api/embed -d '{
  "model": "mxbai-embed-large",
  "input": "Llamas are members of the camelid family"
}'

#3.23.102.245
curl http://18.117.8.58:11434/api/embed -d '{
  "model": "mxbai-embed-large",
  "input": "Llamas are members of the camelid family"
}'
```

## Conda packages
 
- I like mini conda, use what you like
```bash
# packages in environment at C:\Users\diego\miniconda3\envs\rag_test:
#
# environment.yml
# environment.yml

name: rag-test
channels:
  - conda-forge
  - defaults
dependencies:
  - python = 3.12
  - aiohappyeyeballs=2.4.4
  - aiohttp=3.11.10
  - aiosignal=1.2.0
  - annotated-types=0.6.0
  - anyio=4.6.2
  - asgiref=3.8.1
  - async-timeout=4.0.3
  - attrs=24.3.0
  - backoff=2.2.1
  - bcrypt=4.2.1
  - blas=1.0
  - blinker=1.9.0
  - brotli-python=1.0.9
  - bzip2=1.0.8
  - c-ares=1.34.4
  - ca-certificates=2024.12.31
  - cachetools=5.3.3
  - certifi=2024.12.14
  - cffi=1.17.1
  - charset-normalizer=3.3.2
  - chroma-hnswlib=0.7.6
  - chromadb=0.6.3
  - click=8.1.7
  - colorama=0.4.6
  - coloredlogs=15.0.1
  - cryptography=43.0.3
  - dataclasses-json=0.6.5
  - deprecated=1.2.13
  - durationpy=0.9
  - expat=2.6.4
  - fastapi=0.112.2
  - filelock=3.13.1
  - frozenlist=1.5.0
  - fsspec=2024.12.0
  - google-auth=2.29.0
  - googleapis-common-protos=1.63.2
  - greenlet=3.1.1
  - grpcio=1.62.2
  - h11=0.14.0
  - httpcore=1.0.2
  - httptools=0.6.4
  - httpx=0.27.0
  - httpx-sse=0.4.0
  - huggingface_hub=0.24.6
  - humanfriendly=10.0
  - idna=3.7
  - importlib-metadata=7.0.1
  - importlib-resources=6.4.0
  - importlib_resources=6.4.0
  - iniconfig=1.1.1
  # - intel-openmp=2023.1.0
  - jmespath=1.0.1
  - jsonpatch=1.33
  - jsonpointer=2.1
  - krb5=1.21.3
  - langchain=0.3.15
  - langchain-community=0.3.12
  - langchain-core=0.3.31
  - langchain-text-splitters=0.3.5
  - langsmith=0.1.147
  - libabseil=20240116.2
  - libcurl=8.11.1
  - libexpat=2.6.4
  - libgrpc=1.62.2
  - liblzma=5.6.3
  - liblzma-devel=5.6.3
  - libprotobuf=4.25.3
  - libpulsar=3.5.1
  - libre2-11=2023.09.01
  - libsqlite=3.48.0
  - libssh2=1.11.1
  - libzlib=1.3.1
  - markdown-it-py=2.2.0
  - marshmallow=3.19.0
  - mdurl=0.1.0
  - mkl=2023.1.0
  - mkl-service=2.4.0
  - mkl_fft=1.3.11
  - mkl_random=1.2.8
  - mmh3=5.0.1
  - monotonic=1.5
  - mpmath=1.3.0
  - multidict=6.1.0
  - mypy_extensions=1.0.0
  - numpy=2.0.1
  - numpy-base=2.0.1
  - oauthlib=3.2.2
  - ollama-python=0.4.7
  - onnxruntime=1.20.1
  - openssl=3.4.0
  - opentelemetry-api=1.26.0
  - opentelemetry-exporter-otlp-proto-common=1.26.0
  - opentelemetry-exporter-otlp-proto-grpc=1.26.0
  - opentelemetry-instrumentation=0.47b0
  - opentelemetry-instrumentation-asgi=0.47b0
  - opentelemetry-instrumentation-fastapi=0.47b0
  - opentelemetry-proto=1.26.0
  - opentelemetry-sdk=1.26.0
  - opentelemetry-semantic-conventions=0.47b0
  - opentelemetry-util-http=0.47b0
  - orjson=3.10.14
  - overrides=7.4.0
  - packaging=24.2
  - pip=24.2
  - pluggy=1.5.0
  - posthog=3.6.5
  - propcache=0.2.0
  - protobuf=4.25.3
  - pulsar-client=3.5.0
  - pyasn1=0.4.8
  - pyasn1-modules=0.2.8
  - pycparser=2.21
  - pydantic=2.10.3
  - pydantic-core=2.27.1
  - pydantic-settings=2.6.1
  - pygments=2.15.1
  - pyjwt=2.10.1
  - pyopenssl=24.2.1
  - pypdf=4.2.0
  - pypika=0.48.9
  - pyproject_hooks=1.0.0
  # - pyreadline3=3.4.1
  - pysocks=1.7.1
  - pytest=7.4.4
  - python=3.12.8
  - python-build=1.2.2.post1
  - python-dateutil=2.9.0post0
  - python-dotenv=0.21.0
  - python-flatbuffers=24.3.25
  - python-kubernetes=32.0.0
  - python_abi=3.12=5_cp312
  - pyyaml=6.0.2
  - re2=2023.09.01
  - requests=2.32.3
  - requests-oauthlib=2.0.0
  - requests-toolbelt=1.0.0
  - rich=13.9.4
  - rsa=4.7.2
  - setuptools=75.1.0
  - shellingham=1.5.0
  - six=1.16.0
  - snappy=1.2.1
  - sniffio=1.3.0
  - sqlalchemy=2.0.37
  - sqlite=3.48.0
  - starlette=0.38.2
  - sympy=1.13.3
  - tbb=2021.8.0
  - tenacity=9.0.0
  - tk=8.6.13
  - tokenizers=0.20.1
  - tqdm=4.66.5
  - typer=0.9.0
  - typing-extensions=4.12.2
  - typing_extensions=4.12.2
  - typing_inspect=0.9.0
  - tzdata=2025a
  - urllib3=2.3.0
  - uvicorn=0.32.1
  - uvicorn-standard=0.32.1
  - watchfiles=0.24.0
  - websocket-client=1.8.0
  - websockets=10.4
  - wheel=0.44.0
  - wrapt=1.17.0
  - xz=5.6.3
  - xz-tools=5.6.3
  - yaml=0.2.5
  - yarl=1.18.0
  - zipp=3.21.0
  - zlib=1.3.1
  - zstd=1.5.6
  - pip:
    - boto3==1.36.5
    - botocore==1.36.5
    - langchain-aws==0.2.11
    - s3transfer==0.11.2
```



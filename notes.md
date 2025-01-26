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
curl http://3.23.102.245:11434/api/embed -d '{
  "model": "mxbai-embed-large",
  "input": "Llamas are members of the camelid family"
}'
```

## Conda packages
 
- I like mini conda, use what you like
```bash
# packages in environment at C:\Users\diego\miniconda3\envs\rag_test:
#
# Name                    Version                   Build  Channel
aiohappyeyeballs          2.4.4           py312haa95532_0
aiohttp                   3.11.10         py312h827c3e9_0
aiosignal                 1.2.0              pyhd3eb1b0_0
annotated-types           0.6.0           py312haa95532_0
anyio                     4.6.2           py312haa95532_0
asgiref                   3.8.1           py312haa95532_0
async-timeout             4.0.3              pyhd8ed1ab_0    conda-forge
attrs                     24.3.0          py312haa95532_0
backoff                   2.2.1           py312haa95532_1
bcrypt                    4.2.1           py312h2615798_0    conda-forge
blas                      1.0                         mkl
blinker                   1.9.0           py312haa95532_0
boto3                     1.36.5                   pypi_0    pypi
botocore                  1.36.5                   pypi_0    pypi
brotli-python             1.0.9           py312h5da7b33_9
bzip2                     1.0.8                h2bbff1b_6
c-ares                    1.34.4               h2466b09_0    conda-forge
ca-certificates           2024.12.31           haa95532_0
cachetools                5.3.3           py312haa95532_0
certifi                   2024.12.14         pyhd8ed1ab_0    conda-forge
cffi                      1.17.1          py312h827c3e9_1
charset-normalizer        3.3.2              pyhd3eb1b0_0
chroma-hnswlib            0.7.6           py312hbaa7e33_1    conda-forge
chromadb                  0.6.3           py312h2e8e312_0    conda-forge
click                     8.1.7           py312haa95532_0
colorama                  0.4.6           py312haa95532_0
coloredlogs               15.0.1          py312haa95532_3
cryptography              43.0.3          py312hbd6ee87_1
dataclasses-json          0.6.5           py312haa95532_0
deprecated                1.2.13          py312haa95532_0
dlfcn-win32               1.4.1                h63175ca_0    conda-forge
durationpy                0.9                pyhd8ed1ab_1    conda-forge
expat                     2.6.4                h8ddb27b_0
fastapi                   0.112.2         py312haa95532_0
filelock                  3.13.1          py312haa95532_0
frozenlist                1.5.0           py312h827c3e9_0
fsspec                    2024.12.0       py312haa95532_0
google-auth               2.29.0          py312haa95532_0
googleapis-common-protos  1.63.2          py312haa95532_0
greenlet                  3.1.1           py312h5da7b33_0
grpcio                    1.62.2          py312h7894644_0    conda-forge
h11                       0.14.0          py312haa95532_0
httpcore                  1.0.2           py312haa95532_0
httptools                 0.6.4           py312h827c3e9_0
httpx                     0.27.0          py312haa95532_0
httpx-sse                 0.4.0           py312haa95532_0
huggingface_hub           0.24.6          py312haa95532_0
humanfriendly             10.0            py312haa95532_2
idna                      3.7             py312haa95532_0
importlib-metadata        7.0.1           py312haa95532_0
importlib-resources       6.4.0              pyhd3eb1b0_0
importlib_resources       6.4.0           py312haa95532_0
iniconfig                 1.1.1              pyhd3eb1b0_0
intel-openmp              2023.1.0         h59b6b97_46320
jmespath                  1.0.1           py312haa95532_0
jsonpatch                 1.33            py312haa95532_1
jsonpointer               2.1                pyhd3eb1b0_0
krb5                      1.21.3               hdf4eb48_0    conda-forge
langchain                 0.3.15          pymin312_hff2d567_1    conda-forge
langchain-aws             0.2.11                   pypi_0    pypi
langchain-community       0.3.12          py312haa95532_0
langchain-core            0.3.31             pyhd8ed1ab_0    conda-forge
langchain-text-splitters  0.3.5              pyhd8ed1ab_0    conda-forge
langsmith                 0.1.147         py312haa95532_0
libabseil                 20240116.2      cxx17_h5da7b33_0
libcurl                   8.11.1               h88aaa65_0    conda-forge
libexpat                  2.6.4                he0c23c2_0    conda-forge
libffi                    3.4.4                hd77b12b_1
libgrpc                   1.62.2               h5273850_0    conda-forge
liblzma                   5.6.3                h2466b09_1    conda-forge
liblzma-devel             5.6.3                h2466b09_1    conda-forge
libprotobuf               4.25.3               h47a098d_1    conda-forge
libpulsar                 3.5.1                h13e8e67_2    conda-forge
libre2-11                 2023.09.01           hf8d8778_2    conda-forge
libsqlite                 3.48.0               h67fdade_1    conda-forge
libssh2                   1.11.1               he619c9f_0    conda-forge
libzlib                   1.3.1                h2466b09_2    conda-forge
markdown-it-py            2.2.0           py312haa95532_1
marshmallow               3.19.0          py312haa95532_0
mdurl                     0.1.0           py312haa95532_0
mkl                       2023.1.0         h6b88ed4_46358
mkl-service               2.4.0           py312h827c3e9_2
mkl_fft                   1.3.11          py312h827c3e9_0
mkl_random                1.2.8           py312h0158946_0
mmh3                      5.0.1           py312h5da7b33_0
monotonic                 1.5                        py_0
mpmath                    1.3.0           py312haa95532_0
multidict                 6.1.0           py312h827c3e9_0
mypy_extensions           1.0.0           py312haa95532_0
numpy                     2.0.1           py312hfd52020_1
numpy-base                2.0.1           py312h4dde369_1
oauthlib                  3.2.2           py312haa95532_0
ollama                    0.1.17           cpu_h11720a3_0    conda-forge
ollama-python             0.4.7              pyhd8ed1ab_0    conda-forge
onnxruntime               1.20.1          py312h414cfab_0_cpu    conda-forge
openssl                   3.4.0                ha4e3fda_1    conda-forge
opentelemetry-api         1.26.0          py312haa95532_0
opentelemetry-exporter-otlp-proto-common 1.26.0          py312haa95532_1
opentelemetry-exporter-otlp-proto-grpc 1.26.0          py312haa95532_0
opentelemetry-instrumentation 0.47b0          py312haa95532_0
opentelemetry-instrumentation-asgi 0.47b0             pyhd8ed1ab_0    conda-forge
opentelemetry-instrumentation-fastapi 0.47b0             pyhd8ed1ab_0    conda-forge
opentelemetry-proto       1.26.0          py312haa95532_0
opentelemetry-sdk         1.26.0          py312haa95532_0
opentelemetry-semantic-conventions 0.47b0          py312haa95532_0
opentelemetry-util-http   0.47b0             pyhd8ed1ab_0    conda-forge
orjson                    3.10.14         py312h636fa0f_0
overrides                 7.4.0           py312haa95532_0
packaging                 24.2            py312haa95532_0
pip                       24.2            py312haa95532_0
pluggy                    1.5.0           py312haa95532_0
posthog                   3.6.5              pyhd8ed1ab_0    conda-forge
propcache                 0.2.0           py312h827c3e9_0
protobuf                  4.25.3          py312hf91db99_1
pulsar-client             3.5.0           py312h275cf98_1    conda-forge
pyasn1                    0.4.8              pyhd3eb1b0_0
pyasn1-modules            0.2.8                      py_0
pycparser                 2.21               pyhd3eb1b0_0
pydantic                  2.10.3          py312haa95532_0
pydantic-core             2.27.1          py312h636fa0f_0
pydantic-settings         2.6.1           py312haa95532_0
pygments                  2.15.1          py312haa95532_1
pyjwt                     2.10.1          py312haa95532_0
pyopenssl                 24.2.1          py312haa95532_0
pypdf                     4.2.0           py312haa95532_0
pypika                    0.48.9             pyhd8ed1ab_1    conda-forge
pyproject_hooks           1.0.0           py312haa95532_0
pyreadline3               3.4.1           py312haa95532_0
pysocks                   1.7.1           py312haa95532_0
pytest                    7.4.4           py312haa95532_0
python                    3.12.8          h3f84c4b_1_cpython    conda-forge
python-build              1.2.2.post1     py312haa95532_0
python-dateutil           2.9.0post0      py312haa95532_2
python-dotenv             0.21.0          py312haa95532_0
python-flatbuffers        24.3.25         py312haa95532_0
python-kubernetes         32.0.0             pyhd8ed1ab_0    conda-forge
python_abi                3.12                    5_cp312    conda-forge
pyyaml                    6.0.2           py312h827c3e9_0
re2                       2023.09.01           hd3b24a8_2    conda-forge
requests                  2.32.3          py312haa95532_1
requests-oauthlib         2.0.0           py312haa95532_0
requests-toolbelt         1.0.0           py312haa95532_0
rich                      13.9.4          py312haa95532_0
rsa                       4.7.2              pyhd3eb1b0_1
s3transfer                0.11.2                   pypi_0    pypi
setuptools                75.1.0          py312haa95532_0
shellingham               1.5.0           py312haa95532_0
six                       1.16.0             pyhd3eb1b0_1
snappy                    1.2.1                hcdb6601_0
sniffio                   1.3.0           py312haa95532_0
sqlalchemy                2.0.37          py312h54f65d0_0
sqlite                    3.45.3               h2bbff1b_0
starlette                 0.38.2          py312haa95532_0
sympy                     1.13.3          py312haa95532_0
tbb                       2021.8.0             h59b6b97_0
tenacity                  9.0.0           py312haa95532_0
tk                        8.6.13               h5226925_1    conda-forge
tokenizers                0.20.1          py312h482ea96_1
tqdm                      4.66.5          py312hfc267ef_0
typer                     0.9.0           py312haa95532_0
typing-extensions         4.12.2          py312haa95532_0
typing_extensions         4.12.2          py312haa95532_0
typing_inspect            0.9.0           py312haa95532_0
tzdata                    2025a                h04d1e81_0
ucrt                      10.0.20348.0         haa95532_0
urllib3                   2.3.0           py312haa95532_0
uvicorn                   0.32.1          py312haa95532_0
uvicorn-standard          0.32.1          py312haa95532_0
vc                        14.40                haa95532_2
vc14_runtime              14.42.34433         h6356254_24    conda-forge
vs2015_runtime            14.42.34433         hfef2bbc_24    conda-forge
watchfiles                0.24.0          py312h636fa0f_2
websocket-client          1.8.0           py312haa95532_0
websockets                10.4            py312h827c3e9_2
wheel                     0.44.0          py312haa95532_0
win_inet_pton             1.1.0           py312haa95532_0
wrapt                     1.17.0          py312h827c3e9_0
xz                        5.6.3                h208afaa_1    conda-forge
xz-tools                  5.6.3                h2466b09_1    conda-forge
yaml                      0.2.5                he774522_0
yarl                      1.18.0          py312h827c3e9_0
zipp                      3.21.0          py312haa95532_0
zlib                      1.3.1                h2466b09_2    conda-forge
zstd                      1.5.6                h0ea2cb4_0    conda-forge
```



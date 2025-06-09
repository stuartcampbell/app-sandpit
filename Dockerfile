FROM ghcr.io/astral-sh/uv:latest AS uv
FROM python:3.12
COPY --from=uv /uv /bin/uv

ENV UV_SYSTEM_PYTHON=1

WORKDIR /code

COPY requirements.txt .
RUN uv pip install wheel
RUN uv pip install -r /code/requirements.txt

COPY . .
RUN uv build
RUN uv pip install '.'

CMD ["uvicorn", "sandpit.main:app", "--proxy-headers", \
                "--host", "0.0.0.0", "--port", "8080",  \
                "--log-config=uvicorn_log_config.yml"]

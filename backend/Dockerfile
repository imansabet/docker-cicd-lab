LABEL org.opencontainers.image.source="https://github.com/imansabet/docker-cicd-lab"
# stage 1:  build (dependencies)
FROM python:3.12-slim AS builder
WORKDIR /build
ENV PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1
COPY requirements.txt .
RUN python -m venv /opt/venv \ 
 && /opt/venv/bin/pip install -r requirements.txt



FROM python:3.12-slim AS base
ENV PATH="/opt/venv/bin:$PATH" \ 
  PYTHONUNBUFFERED=1 \ 
  PYTHONDONTWRITEBYTECODE=1

RUN useradd --create-home --uid 10001 app
WORKDIR /home/app

COPY --from=builder /opt/venv /opt/venv
COPY --chown=app:app app ./app

USER app
EXPOSE 8000

HEALTHCHECK --interval=15s --timeout=3s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://localhost:8000/health', timeout=2).status==200 else 1)"
	

FROM base AS dev
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000","--reload" ]	

FROM base AS prod 
COPY --chown=app:app app ./app
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000" ]	



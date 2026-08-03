FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY . .

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip \
 && pip install "mcp>=1.0.0,<2.0.0" \
 && pip install -e . \
 && pip install mcp-proxy

EXPOSE 8080

CMD ["mcp-proxy", "--host", "0.0.0.0", "--port", "8080", "--", "python", "-m", "src"]

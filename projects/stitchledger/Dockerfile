FROM python:3.13-slim
WORKDIR /app/backend
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && useradd -u 10001 -m studio
COPY backend/ ./
COPY web-build/ /app/web-build/
RUN mkdir -p /app/backend/data && chown -R studio:studio /app
USER studio
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--no-proxy-headers"]

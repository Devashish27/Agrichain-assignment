FROM python:3-slim

WORKDIR /app

COPY . /app

# Combine virtual environment creation and dependency installation
RUN python -m venv env && \
    /app/env/bin/pip install --no-cache-dir -r requirements.txt

ENV PATH="/app/env/bin:$PATH"

CMD ["python", "main.py"]

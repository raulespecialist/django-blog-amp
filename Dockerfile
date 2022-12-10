FROM python:3.10.7 as compile-image

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ENV PYTHONUNBUFFERED 1
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /code
USER appuser
RUN chmod 777 /code/core/db.sqlite3
RUN chown appuser:appuser /code/core/db.sqlite3
COPY core/media/ /code/core/media/

# RUN python /code/data/import_review.py

#CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "core", "core.wsgi:application"]
ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
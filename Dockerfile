FROM python:2.7

WORKDIR /
RUN git clone https://github.com/TerryHowe/pymaze.git
WORKDIR /pymaze
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN python manage.py shell <populate.py

EXPOSE 8000

ENTRYPOINT ["/pymaze/run.sh"]

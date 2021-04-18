# install dependencies for redis support
# https://docs.celeryproject.org/en/stable/getting-started/brokers/redis.html
pip install -U "celery[redis]"


# terminal 01
celery -A tasks worker --loglevel=info

# terminal 02
python invoker.py

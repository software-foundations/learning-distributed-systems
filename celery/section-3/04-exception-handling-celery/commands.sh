# terminal 01
celery -A tasks worker --loglevel=info

# terminal 02
python invoker.py

# terminal 01
celery -A tasks worker --loglevel=info

# terminal 02
celery -A tasks beat --loglevel=info

# terminal 03
python invoker.py

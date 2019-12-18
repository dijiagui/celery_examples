
up:
	celery -A tasks worker -l=debug
up_feed:
	celery -A tasks worker -l=debug -Q feeds
up_slow:
	celery -A tasks worker -l=debug -Q slows
up_celery:
	celery -A tasks worker -l=debug -Q celery
run:
	python3 run.py
flower:
	flower -A tasks --port=5555 --basic_auth=kzydevops:090203 --loglevel=info
event_start:
	celery -A proj control enable_events
event_stop:
	celery -A proj control disable_events
event:
	celery -A tasks events

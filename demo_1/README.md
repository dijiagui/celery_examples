## for py
celery -A hello_world_for_py -c 1 worker --loglevel=debug

```python
from hello_world_for_py import run
run.delay()
```

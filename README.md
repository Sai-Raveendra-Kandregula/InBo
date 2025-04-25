# InBo

A Bot Framework for Gitlab.

## Usage

```py
from inbo import Inbo

class TestBot(Inbo):
    async def merge_request_event(self, gl, action, data):
        self.logger.info(f"Recieved MR {action} event")
        self.logger.info(data)

bot = TestBot()
bot.run()
```

## Run Tests

- Install `setuptools`
- Run `pip install -e .`
- Run `python test.py`
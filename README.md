# Slack Notifier

A Python Tool To Send Notifications To Your <b>Slack</b> App.

## VERSION 0.0.1 (Prototype)

version 1 only supports function task notification. When the function
is executed and finished, the python runtime sends notification to your
slack app configured in advance.

## Installation

1. install python package by pip  
    `pip install slacknotifer`
2. set the environment variable `DEFAULT_SLACK_FUNCTION_TASK_NOTIFIER_URL` to a webhook
URL for your workspace.  
    `export DEFAULT_SLACK_FUNCTION_TASK_NOTIFIER_URL="your_apps_webhook_url"` 



## Usage

- With Statement  
```python
from slacknotifier import FuncTaskNotifier

def any_task():
  pass

with FuncTaskNotifier():
    any_task()
```   

- As Decorator
```python
from slacknotifier import FuncTaskNotifier
@FuncTaskNotifier(notify_start=True)
def any_task():
    pass

any_task()
```


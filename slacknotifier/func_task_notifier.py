import os
import requests
import functools
from datetime import datetime

os.environ['DEFAULT_SLACK_FUNCTION_TASK_NOTIFIER_URL'] = "https://hooks.slack.com/services/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"
default_url = os.environ['DEFAULT_SLACK_FUNCTION_TASK_NOTIFIER_URL']


def send_message_to(msg, app_url=default_url):
  try:
    res = requests.post(app_url, json={"text": msg})
    if res.status_code != 200:
      raise RuntimeError
  except RuntimeError as e:
    print("Report to Slack failed.")


class FuncTaskNotifier:
  def __init__(self, app_url=default_url, task=None, notify_start=False, notify_end=True):
    self.app_url = app_url
    self.task = task
    self.notify_start = notify_start
    self.notify_end = notify_end
    self.start_time = None
    self.end_time = None
  
  def attach_task(self, f):
    self.task = f
  
  def run(self, *args, **kwargs):
    if self.task is not None:
      self.task(*args, **kwargs)
    else:
      print("no task is set to this notifier instance. Set task by attach_task(task)")
  
  def __call__(self, f):
    self.task = f
    @functools.wraps(f)
    def decorate_context(*args, **kwargs):
      with self:
        return f(*args, **kwargs)
    return decorate_context
  
  def notify(self, app_url=default_url, when='end'):
    if when != 'end' and when != 'start':
      raise KeyError("The timing of the notification supported is either 'start' or 'end'.")
    
    if when == 'start':
      self.start_time = datetime.now()
      task_name = "" if self.task is None else self.task.__name__
      time_string = self.start_time.strftime("%d-%m-%Y %H:%M:%S")
      start_msg = "function task: {:>16} started at {}.".format(task_name, time_string)
      send_message_to(start_msg, self.app_url)

    if when == 'end':
      self.end_time = datetime.now()
      time_string = self.end_time.strftime("%d-%m-%Y %H:%M:%S")
      
      task_name = ""
      if self.task is not None:
        task_name = self.task.__name__ if len(self.task.__name__) < 16 else (self.task.__name__[:14] + "...")
        
      end_msg = "function task: {} ended at {}.".format(task_name, time_string)
      if self.start_time is not None:
        duration_seconds = (self.end_time - self.start_time).seconds
        duration_string = self._get_strftime_from_seconds(duration_seconds)
        duration_msg = " Total executed in {}".format(duration_string)
        end_msg += duration_msg
      send_message_to(end_msg, app_url)
  
  def _get_strftime_from_seconds(self, seconds):
    duration = seconds
    duration_strings = []
    for unit in ("sec", "min", "hr", "day"):
      duration_strings.append(f"{duration % 60} {unit}")
      if duration // 60 == 0:  # min
        break
      duration //= 60
    return ' '.join(list(reversed(duration_strings)))
      
  def __enter__(self):
    if self.notify_start:
      self.notify(self.app_url, 'start')
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    if self.notify_end:
      self.notify(self.app_url, 'end')
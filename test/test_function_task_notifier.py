from slacknotifier import FuncTaskNotifier
import time


@FuncTaskNotifier(notify_start=True)
def sleep_in_1min():
  time.sleep(60)
  print("waited for 1 min")


if __name__ == '__main__':
  sleep_in_1min()
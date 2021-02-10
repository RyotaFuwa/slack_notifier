from slacknotifier import FuncTaskNotifier


@FuncTaskNotifier(app_url="https://hooks.slack.com/services/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")
def hello_world():
  print("hello world.")


if __name__ == '__main__':
  hello_world()
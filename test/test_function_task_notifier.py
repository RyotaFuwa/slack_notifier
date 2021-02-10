from slacknotifier import FuncTaskNotifier


@FuncTaskNotifier(app_url="https://example.com")
def hello_world():
  print("hello world.")


if __name__ == '__main__':
  hello_world()
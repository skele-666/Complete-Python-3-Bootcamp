#one.py
# Any code at indendation level 0 will be executed when this file is run.
# There is no main function in python. But implicitly, all code at indentation level 0 is executed

# If the script is ran directly, __name__ will be set to "__main__"
# So, you can check with an if statement (usually placed at the end):
# if __name__ == '__main__':
#     print('This script is being run directly')

def func():
    print("FUNC IN ONE.PY")

def function():
    pass

def function2():
    pass

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    # RUN THE SCRIPT!
    function2()
    function()
    func()
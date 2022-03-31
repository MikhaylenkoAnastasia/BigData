import sys


def my_precious_logger(text: str):
    line_stderr = sys.stderr
    line_stdout = sys.stdout
    if text.split()[0] == 'error:':
        line_stderr.write(text + '\n')
    else:
        line_stdout.write(text + '\n')
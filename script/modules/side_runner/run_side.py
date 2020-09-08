from colors import color

import sys
import subprocess
import shlex
import glob
import time
import fire


def colored_print(msg, color_name, *, end='\n'):
    """
    Apply color to the print function.

        Parameters:
            msg (str):              Message to print
            color_name (str): Color
            end (str) :              Same as end parameter of print function
    """

    print(color(msg, color_name), end=end)


class Pipeline(object):
    def __init__(self):
        pass

    def run_test(command: str):
        test_path = command.split(" ")[4]
        colored_print(test_path, 'cyan')  # print command

        result = subprocess.Popen(args=shlex.split(command), shell=False,
                                  stderr=subprocess.STDOUT, stdout=subprocess.PIPE)

        stdout, _ = result.communicate()
        # _ = result.poll()

        # print stdout
        print(stdout.decode('utf-8'))


if __name__ == "__main__":
    fire.Fire()
    # tests = glob.glob(
    #     "/root/IRIS-E2E-SAAS/**/*.side", recursive=True)

    # tests = glob.glob(
    #     "/Users/minsoo-web/Desktop/modigen/IRIS-E2E-SAAS/**/*.side", recursive=True)

    # for file in tests:
    #     run_test(
    #         command=f'selenium-side-runner -c "goog:chromeOptions.args=[headless,no-sandbox] browserName=chrome" {file} --output-directory=./ --output-format=junit >> temp.txt')
    #     time.sleep(0.5)

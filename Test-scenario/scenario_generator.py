import json
import sys
import glob
import os


help_message = ("\n"
        "==============================================================================================\n"
        "usage: python scenario_generator.py 'side 파일이 존재하는 경로' '결과 md파일을 저장할 경로'\n"
        "example: python scenario_generator.py ../01.ANALYZER_TESTS ./01.ANALYZER_SCENARIO\n"
        "==============================================================================================")

# 절차에서 제외할 명령어 리스트
ignore_commands = ["waitForElementPresent", "waitForElementVisible", "waitForElementEditable", "waitForElementNotVisible",
                   "pause", "open", "setWindowSize", "storeXpathCount", "if", "end", "selectFrame", "run"]
# 주석을 걸었을 경우, 앞에 "//" 이 붙는데, 이 경우도 절차에서 제외해야함
ignore_commands += ["//" + ignore_command for ignore_command in ignore_commands]

output_path = "./test"

if len(sys.argv) < 2:
    raise ValueError(help_message)

side_files = glob.glob(sys.argv[1] + "/*.side")

try:
    output_path = sys.argv[2]
except IndexError:
    raise ValueError("Please specify the output path\n" + help_message)

try:
    os.mkdir(output_path)
except FileExistsError:
    pass

for side_file in side_files:
    with open(side_file, "r") as f:
        data = json.load(f)

    scenario_file_name = side_file.split("/")[-1].replace("side", "md")
    with open(output_path + "/" + scenario_file_name, "w") as f:
        scenario_name = data["name"]
        f.write("# " + scenario_name + "\n\n")
        for test in data["tests"]:
            test_name = test["name"]
            f.write("## " + test_name + "\n")
            for command in test["commands"]:
                comment = command["comment"] if command["command"] not in ignore_commands else ""
                if comment != "":
                    f.write("- " + comment + "\n")
            f.write("\n")

import re

with open('a.txt') as file_obj:
    for node in file_obj:
        result = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", node.rstrip())
        if len(result) == 0:
            break
        # print(node.rstrip())
        print(*result)
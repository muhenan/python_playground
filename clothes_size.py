import re

# todo: Learn RE!!!!!!!!!!!!!!!!

def extract_size_info(size):
    # 使用正则表达式提取尺码中的数字部分和后缀
    match = re.search(r'(\d+)([A-Z]*)', size)
    if match:
        size_number = int(match.group(1))
        size_suffix = match.group(2)
        return size_number, size_suffix
    else:
        return 0, size

def compare_sizes(size1, size2):
    # 提取尺码中的数字部分和后缀
    number1, suffix1 = extract_size_info(size1)
    number2, suffix2 = extract_size_info(size2)

    # 比较数字部分
    if number1 < number2:
        return "Smaller"
    elif number1 > number2:
        return "Bigger"

    # 如果数字相等，比较后缀（X前缀）
    if suffix1 > suffix2:
        return "Smaller"
    elif suffix1 < suffix2:
        return "Bigger"

    return "Equal"

# 输入T
T = int(input())

# 逐行处理输入
for _ in range(T):
    size1, size2 = input().split()
    result = compare_sizes(size1, size2)
    print(result)

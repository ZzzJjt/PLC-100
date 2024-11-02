import json

with open('/home/zhengjiatong/json_generation/code_generation_tasks.json', 'r') as file:
    data = json.load(file)
    print("Total number of generated code entries:", len(data))


with open('/home/zhengjiatong/json_generation/reference_tasks.json', 'r') as file:
    data = json.load(file)
    print("Total number of generated code entries:", len(data))

# # 读取并格式化 code_generation_tasks.json
# with open('code_generation_tasks.json', 'r') as file:
#     code_data = json.load(file)
#
# formatted_code_data = [{"generated_candidates": [code]} for code in code_data]
#
# with open('formatted_code_generation_tasks.json', 'w') as file:
#     json.dump(formatted_code_data, file, indent=4)
#
# # 读取并格式化 reference_tasks.json
# with open('reference_tasks.json', 'r') as file:
#     reference_data = json.load(file)
#
# formatted_reference_data = [{"generated_candidates": [ref]} for ref in reference_data]
#
# with open('formatted_reference_tasks.json', 'w') as file:
#     json.dump(formatted_reference_data, file, indent=4)
#
# print("Both files have been formatted and saved.")
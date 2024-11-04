import requests
import base64
import json
import time


# Helper function to make a GET request to the GitHub API with authentication
def fetch_github_content(url):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token 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"  # 替换为你的 GitHub 访问令牌
    }

    for attempt in range(3):  # 尝试请求3次
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            time.sleep(1)  # 成功后延迟 1 秒，避免触发速率限制
            return response.json()
        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
            if attempt < 2:
                print("Retrying...")
                time.sleep(2)  # 等待 2 秒后重试
            else:
                return None  # 返回 None 表示请求失败


# Helper function to decode Base64 content from GitHub API
def decode_content(base64_content):
    return base64.b64decode(base64_content).decode('utf-8')


# Recursive function to explore folders and fetch .md files
def explore_folder(api_url, tasks):
    items = fetch_github_content(api_url)

    if items:
        for item in items:
            print(f"Processing: {item['name']} ({item['type']})")  # 调试信息

            if item['type'] == 'file' and item['name'].endswith('.md'):
                file_content = fetch_github_content(item['url'])
                if file_content and 'content' in file_content:
                    content = decode_content(file_content['content'])
                    task = {
                        "filename": item['name'],
                        "content": content,
                        "description": f"Markdown file from {item['name']}",
                        "path": item['path']
                    }
                    tasks.append(task)

            elif item['type'] == 'dir':
                explore_folder(item['url'], tasks)  # 递归调用


# Save the tasks to a JSON file
def save_tasks_to_json(tasks, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)


# Main function to generate JSON from a GitHub folder
def generate_json_from_github(api_url, output_file='code_generation_tasks.json'):
    tasks = []
    explore_folder(api_url, tasks)  # Start the exploration
    save_tasks_to_json(tasks, output_file)
    print(f"JSON file generated: {output_file}")


# Example usage
if __name__ == "__main__":
    api_url = "https://api.github.com/repos/ZzzJjt/PLC-ST-StructuredText/contents/Code%20Generation"
    generate_json_from_github(api_url)

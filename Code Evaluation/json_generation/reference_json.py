import requests
import base64
import json
import time


# Helper function to make a GET request to the GitHub API with authentication and rate limit check
def fetch_github_content(url):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "Bearer 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"  # 替换为你的 GitHub 访问令牌
    }
    check_rate_limit(headers)  # 检查速率限制
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        return None


# Function to check GitHub API rate limit
def check_rate_limit(headers):
    rate_limit_url = "https://api.github.com/rate_limit"
    response = requests.get(rate_limit_url, headers=headers)
    data = response.json()
    core_limit = data["resources"]["core"]
    remaining = core_limit["remaining"]
    reset_time = core_limit["reset"]

    if remaining == 0:
        wait_time = reset_time - int(time.time())
        print(f"Rate limit exceeded. Waiting {wait_time} seconds until reset.")
        time.sleep(wait_time + 5)  # 等待时间后继续


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
                # Fetch the content of the Markdown file
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
                # Recursively explore the subdirectory
                time.sleep(1)  # 延迟避免触发速率限制
                explore_folder(item['url'], tasks)


# Save the tasks to a JSON file
def save_tasks_to_json(tasks, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)


# Main function to generate JSON from a GitHub folder
def generate_json_from_github(api_url, output_file='reference_tasks.json'):
    tasks = []
    explore_folder(api_url, tasks)  # Start the exploration
    save_tasks_to_json(tasks, output_file)
    print(f"JSON file generated: {output_file}")


# Example usage
if __name__ == "__main__":
    # Provide the API URL of the top-level folder (with URL-encoded spaces)
    api_url = "https://api.github.com/repos/ZzzJjt/PLC-ST-StructuredText/contents/Reference%20Solutions"
    generate_json_from_github(api_url)

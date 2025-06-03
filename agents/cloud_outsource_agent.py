import requests
import json
import os

def route_task(task_type, prompt):
    config = load_yaml("agents/cloud_outsource.yaml")
    if not config.get("enabled"):
        return {"error": "Cloud outsourcing is disabled."}

    route = config["routes"].get(task_type)
    if not route:
        return {"error": f"No cloud route defined for task: {task_type}"}

    payload = {"input": prompt} if route["service"] == "replicate" else {"prompt": prompt}

    headers = {
        "Authorization": f"Bearer {os.getenv(route['api_key'].replace('${', '').replace('}', ''))}",
        "Content-Type": "application/json"
    }

    response = requests.post(route["endpoint"], headers=headers, json=payload)
    return response.json()

def load_yaml(path):
    import yaml
    with open(path, 'r') as f:
        return yaml.safe_load(f)

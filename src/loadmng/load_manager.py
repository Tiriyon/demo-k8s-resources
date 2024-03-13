from flask import Flask, render_template, request, redirect
import requests
from kubernetes import client, config

app = Flask(__name__)

config.load_incluster_config()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cpu_load = 'cpu' in request.form
        memory_load = int(request.form.get('memory', 0))
        update_load(cpu_load, memory_load)
        return redirect('/')
    return render_template('index.html')

def update_load(cpu_load, memory_load):
    v1 = client.CoreV1Api()
    pods = v1.list_namespaced_pod(namespace="default", label_selector="app=loader")
    for pod in pods.items:
        url = f"http://{pod.status.pod_ip}:5000/load"
        payload = {'cpu': cpu_load, 'memory': memory_load}
        requests.post(url, json=payload)

@app.route('/reset', methods=['POST'])
def reset():
    v1 = client.CoreV1Api()
    pods = v1.list_namespaced_pod(namespace="default", label_selector="app=loader")
    for pod in pods.items:
        url = f"http://{pod.status.pod_ip}:5000/reset"
        requests.post(url)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

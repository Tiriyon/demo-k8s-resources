import os
from flask import Flask, request
import threading
import time
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

cpu_load = False
memory_load = False
memory_usage = []

def consume_cpu():
    """Simulate CPU load."""
    while cpu_load:
        pass

def consume_memory(target_mb, step_mb=1):
    """Simulate memory load without exceeding the maximum limit."""
    global memory_usage

    # Get the memory limit from the environment variable
    max_mb = int(os.getenv('MEMORY_LIMIT_MB', '0'))

    current_mb = 0
    while current_mb < target_mb:
        if current_mb + step_mb > max_mb:
            break  # Stop if the next step exceeds the maximum limit
        memory_usage.extend([bytearray(1024 * 1024) for _ in range(step_mb)])
        current_mb += step_mb
        time.sleep(1)  # Simulate gradual increase


@app.route('/load', methods=['POST'])
def load():
    global cpu_load, memory_load
    content = request.json

    load_received = False

    if 'cpu' in content:
        cpu_load = content['cpu']
        if cpu_load:
            threading.Thread(target=consume_cpu).start()
            print("New CPU load received: Enabled")
            load_received = True
        else:
            print("CPU load updated: Disabled")

    if 'memory' in content:
        memory_load = True
        consume_memory(content['memory'])
        print(f"New memory load received: {content['memory']} MB")
        load_received = True

    if not load_received:
        print("No load update received")

    return 'Load updated'

@app.route('/reset', methods=['POST'])
def reset():
    global cpu_load, memory_load, memory_usage
    cpu_load = False
    memory_load = False
    memory_usage = []
    return 'Load reset'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


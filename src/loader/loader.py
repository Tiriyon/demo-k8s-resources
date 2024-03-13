from flask import Flask, request
import threading
import time

app = Flask(__name__)

cpu_load = False
memory_load = False
memory_usage = []

def consume_cpu():
    """simulate CPU load."""
    while cpu_load:
        pass

def consume_memory(size_mb):
    """simulate memory load."""
    global memory_usage
    memory_usage = [bytearray(1024 * 1024) for _ in range(size_mb)]

@app.route('/load', methods=['POST'])
def load():
    global cpu_load, memory_load
    content = request.json
    if 'cpu' in content:
        cpu_load = content['cpu']
        if cpu_load:
            threading.Thread(target=consume_cpu).start()
    if 'memory' in content:
        memory_load = True
        consume_memory(content['memory'])
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

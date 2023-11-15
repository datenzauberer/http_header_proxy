from flask import Flask, jsonify
import psutil

app = Flask(__name__)

def get_memory_usage(process_name):
    # Get all processes with the specified name
    processes = [p for p in psutil.process_iter(['pid', 'name']) if process_name.lower() in p.info['name'].lower()]

    if not processes:
        return None  # Process not found

    # Take the first matching process
    target_process = processes[0]

    # Get memory information for the target process
    memory_info = target_process.memory_info()
    
    # Convert memory usage to megabytes for better readability
    memory_mb = memory_info.rss / (1024 ** 2)
    
    # Create a dictionary to hold the memory information
    memory_data = {
        'process_id': target_process.info['pid'],
        'process_name': target_process.info['name'],
        'memory_usage_mb': memory_mb
    }

    return memory_data

@app.route('/memory/<process_name>')
def show_memory_usage(process_name):
    memory_data = get_memory_usage(process_name)

    if memory_data is None:
        return jsonify({'error': 'Process not found'}), 404

    # Return the memory information as JSON
    return jsonify(memory_data)

def get_all_processes():
    # Get a list of all processes and their information
    processes = [p.info for p in psutil.process_iter(['pid', 'name', 'memory_info'])]

    # Convert memory usage to megabytes for better readability
    for process in processes:
        process['memory_usage_mb'] = process['memory_info'].rss / (1024 ** 2)
        del process['memory_info']  # Remove the detailed memory info

    return processes

@app.route('/processes')
def list_all_processes():
    # Get the list of all processes
    all_processes = get_all_processes()

    # Return the processes information as JSON
    return jsonify(all_processes)

if __name__ == '__main__':
    app.run()


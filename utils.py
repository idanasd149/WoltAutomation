import os
import time


def get_profile_directory(base_dir, user_id):
    profile_dir = os.path.join(base_dir, f"user_{user_id}")
    if not os.path.exists(profile_dir):
        os.makedirs(profile_dir)
    return profile_dir


def wait_for_file(filename, timeout=30):
    elapsed_time = 0
    while not os.path.exists(filename) and elapsed_time < timeout:
        time.sleep(1)
        elapsed_time += 1
    if elapsed_time >= timeout:
        raise FileNotFoundError(f"{filename} not found within {timeout} seconds.")
    with open(filename, 'r') as f:
        return f.read().strip()

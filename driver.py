import subprocess

files = ["move.py", "determine_movement_by_poi_timestep.py"]

def run_file(file_name):
    print(f"Running {file_name}...")
    subprocess.run(["python3", file_name], check=True)
    print(f"{file_name} Done!")

for file in files:
    run_file(file)

print("\n--------All files executed successfully--------")
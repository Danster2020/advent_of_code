import os
import subprocess
import time


day_nr = input("day: ")
task_nr = input("task nr: ")

script_folder = os.path.dirname("day" + day_nr + "/")
script_to_run = "task" + task_nr + ".py"

start_time = time.time()
subprocess.run(["python3", script_to_run], cwd=script_folder, check=False)
end_time = time.time()

elapsed_time = end_time - start_time
print(f"\nExecution time for day {day_nr} {script_to_run}: {elapsed_time:.2f} seconds")

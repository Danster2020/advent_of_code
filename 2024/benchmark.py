import os
import subprocess
import time


day_nr = input("day: ")
task_nr = input("task nr: ")

script_folder = os.path.dirname("day" + day_nr + "/")
script_to_run = "task" + task_nr + ".py"

start_time = time.time()

subprocess.run(["python", script_to_run], cwd=script_folder)

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Execution time for {script_to_run}: {elapsed_time:.2f} seconds")

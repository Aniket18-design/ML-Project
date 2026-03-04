import time
import subprocess

start = time.time()

subprocess.run(["python", "run_pipeline.py"])

end = time.time()

print("Total Execution Time:", round(end - start, 2), "seconds")

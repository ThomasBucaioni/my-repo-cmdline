import subprocess
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print("stdout: ", result.stdout)
print("stderr: ", result.stderr)
print("rc: ", result.returncode)

result = subprocess.run(["ls", "non_existing_file"])
print("rc: ", result.returncode)

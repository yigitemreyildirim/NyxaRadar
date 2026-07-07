import shutil
import subprocess
import sys


def run_streaming_command(command):
    tool_name = command[0]
    tool_path = shutil.which(tool_name)
    if not tool_path:
        print(tool_name + " was not found in PATH.")
        return 1

    print("Running:", " ".join(command))
    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
    except FileNotFoundError:
        print(tool_name + " was not found.")
        return 1

    if process.stdout is None:
        return 1

    try:
        for line in process.stdout:
            print(line, end="")
    except KeyboardInterrupt:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
        print("\nInterrupted. Exiting.")
        sys.exit(0)

    process.stdout.close()
    return_code = process.wait()
    if return_code != 0:
        print("Command exited with code " + str(return_code))
    return return_code

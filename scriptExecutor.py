import subprocess
import time
import sys

def main():

    if len(sys.argv) != 3:
        print("Usage: pyhton scriptExecutor.py <code_file.py> <input_size>")
        sys.exit(1)
    
    code_file = sys.argv[1]
    code_input = sys.argv[2]

    try: 
        start_time = time.time()

        res = subprocess.run(["python", code_file],
                              input=code_input + "\n",
                                capture_output=True, 
                                text=True,
                                check=True
                                )
        
        end_time = time.time()

        print(res.stdout.strip())
        print("Execution time: ", end_time - start_time)

    except subprocess.CalledProcessError as e:
        print(f"Command faild with return code {e.returncode}")

if __name__ == "__main__":
    main()

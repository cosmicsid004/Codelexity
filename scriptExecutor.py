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
        runs = 10
        total_time = 0.0;

        #warm_up runs
        subprocess.run(
            [sys.executable, code_file],
            input=code_input + "\n",
            text=True,
            capture_output=True,
            check=True,
            timeout=2
        )

        for i in range(runs):
            start_time = time.perf_counter()

            subprocess.run(
                [sys.executable, code_file],
                input=code_input + "\n",
                text=True,
                capture_output=True,
                check=True, 
                timeout=2
            )
            
            end_time = time.perf_counter()

            # print(res.stdout.strip())
            total_time += (end_time - start_time)
            # print("Execution time: ", end_time - start_time)
        
        print("Average Execution time: ", total_time / runs)

    except subprocess.CalledProcessError as e:
        print(f"Command faild with return code {e.returncode}")
    except subprocess.TimeoutExpired:
        print("Code session time out")

if __name__ == "__main__":
    main()

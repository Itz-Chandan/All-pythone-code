import subprocess
import re

class TaskManager: # Usage:
    def __init__(self):
        self.logs = [] #Initializes an empty list logs to store the output of executed commands

        def execute_command(self, xommand): # Usage:
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            self.logs.append(result.stdout) # joins standard output to logs.
            self.logs.append(result.stderr) # # joins standard errors to logs.
            return result.stdout
        
        def pares_logs(self): #pares --> reading + extracting info from raw files. # Usage:
            error_pattern = r"(error|warning|cannot access|no such file or directory)"
            errors = []
            for log in self.logs:
                errors.extend(re.findall(error_pattern, log, re.IGNORECASE))
                return errors # Adds all matches to the errors list and returns it.
            
            # Usage:
            TaskManager = TaskManager()  # object is created.
            output = TaskManager.execute_command("ls /nonexistent_directory")
            errors = TaskManager.parse_logs()

            print(f"Errors Found: {err}")
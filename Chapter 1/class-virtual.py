class VirtualMachine: 
 def __init__(self, hostname, cpu, ram):
    self.hostname = hostname
    self.cpu = cpu
    self.ram = ram

    def start(self):
        return f"VM: {self.hostname} with {self.cpu} and {self.ram} GB RAM is starting."
    
    class WebServerVM(VirtualMachine): 
         def __init__(self, hostname, cpu, ram, domain):
       class.super().__init__(hostname, cpu, ram)  # Corrected super() usage
self.domain = domain

def host_website(self): 
         return f"Hosting website {self.domain} on {self.hostname}."
    
    # Create a WebServerVM object
web_server = WebServerVM ("webServer1", "4 vCPUs", 16, "example.com")

# Using both methods
print(web_server.start())  # Output: VM: webServer1 with 4 vCPUs and 16 GB RAM is starting.
print(web_server.host_website())  # Output: Hosting website example.com on webServer1.
class Server:
    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address

        def start(self):
             print(f"Server {self.name} is starting.")
        
        def stop(self):
            return(f"Server {self.name} is stopping.")
        
        # Creating an object of the Server class
       Server1 = Server("WebServer1","192.168.0.1")
        

        # Accessing attributes and methods

    print(server1.name)
        # Output: WebServer1

    print(server1.start())
        # Output: WebServer1 is starting
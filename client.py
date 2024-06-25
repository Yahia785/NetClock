import logging

from .chronometer import Chronometer


logger = logging.getLogger(__name__)

class ClockClient:
    """ The client communication module. 
        A single instance of this type is created in the main entry point of the client program.
    """
    
    def __init__(self, local_ip: str, local_port: int, server_ip: str, server_port: int, chronometer: Chronometer):
        """ Initializes a clock client instance.

        Args:
            local_ip (str): local IP address for the client's UDP socket
            local_port (int): local port for the client client's UDP socket
            server_ip (str): IP address for the server's UDP socket
            server_port (int): port for the server's UDP socket
            chronometer (Chronometer): the chronometer instance to be updated using
                network date and time
        """
        self.local_address = (local_ip, local_port)
        self.server_address = (server_ip, server_port)
        self.chronometer = chronometer

    def start(self):
        """ Starts the service thread for the client communication module.
            This method is called from the main thread of the client program. It
            must start a new thread and return to the caller.
            
            The entry point method for the new thread will subscribe to the server,
            receive and process date and time updates, and periodically renew the 
            subscription with the server.
        """
        pass
        
    def stop(self):
        """ Stops the service thread for the client communication module in preparation
            for client program shutdown. This method must signal to the service thread
            that it should exit and then it must `join` the service thread to await the
            thread's termination before returning.
        """
        pass

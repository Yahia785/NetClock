import logging
import socket
import threading
import datetime

from .repository import SubscriberRepository
from .subscriber import ClockSubscriber

MAX_DATAGRAM_SIZE = 65536

logger = logging.getLogger(__name__)

class ClockServer:
    """ The clock server.
        A single instance of this type is created in the main entry point of the server
        program.
    """
    
    def __init__(self, local_ip: str, local_port: int, dead_interval: float, refresh_interval: float,
                 subscriber_repository: SubscriberRepository):
        """ Initializes a server instance.

        Args:
            local_ip (str): local IP address to bind to the server's UDP socket
            local_port (int): local port address to bind to the server's UDP socket
            dead_interval (float): the time interval (in seconds) after which the
                server will assume a client is dead when no HELLO is received from
                the client
            refresh_interval (float): the time interval (in secones) between
                date and time broadcasts to all subscribed clients
            subscriber_repository (ClockSubscriberRepository): a repository that
                will be used to make client subscription's peristent across server
                restarts
        """
        self.dead_interval = dead_interval
        self.refresh_interval = refresh_interval
        self.local_address = (local_ip, local_port)
        self.subscriber_repository = subscriber_repository
        self._subscribers = set()
        self._lock = threading.Lock()
        self._timer = threading.Timer(self.refresh_interval, self.broadcast_time)
        
    # Broadcast the current time to all subscribers (refresh)
    def broadcast_time(self):
    #todo
        pass

    def schedule_timer(self):
        # Cancel existing timer if it's running
        if self._timer:
            self._timer.cancel()

        # Schedule next refresh
        self._timer = threading.Timer(self.refresh_interval, self.broadcast_time)
        self._timer.start()
       

    def run(self):
        """ Run the server.
            This method will be called from the main thread of the server program.
            It will use a loop to receive client messages and a Timer object to
            periodically send date and time broadcasts and age the set of subscribers.
        """

        # Open the UDP socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(self.local_address)
        logger.info(f"Server is listening on {self.local_address}")

        # Load existing subscribers
        self.subscribers = self.subscriber_repository.start()

        print(f"Address: {self.local_address}")
        try:
            while True:
                print("Waiting...")
                message, client_addr = self.socket.recvfrom(MAX_DATAGRAM_SIZE)
                print("Received: " + str(message))

        except KeyboardInterrupt:
            pass

        #cleanup
        self._timer.cancel()
        self.subscriber_repository.stop()
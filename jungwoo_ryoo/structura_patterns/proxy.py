"""
Proxy is handy when creating a highly-resource intensive object.

Problem:
    - Pospone object creating unless absolutely necessary.
    - Find a placeholder.

Solution:
    - Clients - interacting with a proxy
    - Proxy - responsible for creating the resource-intensive objects.
"""

import time


class Producer:
    """Define the 'resource-intensive' object to instantiate."""
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")


class Proxy:
    """Define the 'relatively less resource-intensive' proxy to instantiate"""
    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        """Check if Producer is available."""
        print("Artist checking if Producer is available...")

        if self.occupied == "No":
            # If the producer is available, create a producer object.
            self.producer = Producer()
            time.sleep(2)

            # Make the producer meet the guest!
            self.producer.meet()

        else:
            # Otherwise, don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")


if __name__ == "__main__":
    # Instantiate a Proxy
    p = Proxy()

    # Make the proxy: Artist produce until Producer is available
    p.produce()

    # Change the state to 'occupied'
    p.occupied = "Yes"

    # Make the Producer produce
    p.produce()

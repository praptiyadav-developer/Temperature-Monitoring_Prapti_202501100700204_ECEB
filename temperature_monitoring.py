import random
import time  # Used to create delay

# Function to generate random temperature
def read_temperature():
    return random.randint(0, 100)

# Function to monitor temperature continuously
def monitor_temperature():
    while True:  # Infinite loop
        temperature = read_temperature()
        print("Current temperature:", str(temperature) + "°C")
        
        # Check temperature condition
        if temperature < 0:
            print("Warning: Temperature is below freezing point!")
        elif temperature > 30:
            print("Warning: Temperature is above normal range!")
        else:
            print("Temperature is within the normal range.")
        
        print("----------------------")
        time.sleep(2)  # Wait for 2 seconds

# Start monitoring
monitor_temperature()
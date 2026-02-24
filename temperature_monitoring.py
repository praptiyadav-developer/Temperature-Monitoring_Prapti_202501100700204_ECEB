import random
import time  # Used to create delay

# Function to generate random temperature within user range
def read_temperature(min_temp, max_temp):
    return random.randint(min_temp, max_temp)

# Function to monitor temperature continuously
def monitor_temperature():
    # Take user input
    min_temp = int(input("Enter minimum temperature value: "))
    max_temp = int(input("Enter maximum temperature value: "))

    # Validate input
    if min_temp > max_temp:
        print("Minimum value cannot be greater than maximum value.")
        return

    while True:  # Infinite loop
        temperature = read_temperature(min_temp, max_temp)
        print("Current temperature:", str(temperature) + "°C")
        
        # Check temperature condition
        if temperature < 0:
            print("Warning: Temperature is below freezing point!")
        elif temperature > 30:
            print("Warning: Temperature is above normal range!")
        else:
            print("Temperature is within the normal range.")
        
        print("---------")
        time.sleep(2)  # Wait for 2 seconds

# Start monitoring
monitor_temperature()

# Start monitoring

monitor_temperature()


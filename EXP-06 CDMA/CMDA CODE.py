import numpy as np

# Walsh codes for CDMA (4x4 Hadamard matrix)
codes = {
    1: np.array([1,  1,  1,  1]),
    2: np.array([1, -1,  1, -1]),
    3: np.array([1,  1, -1, -1]),
    4: np.array([1, -1, -1,  1])
}

# Get data bits from user
data_bits = {}
print("Enter the data bits (1 or -1) for each channel:")

for i in range(1, 5):
    data_bits[i] = int(input(f"Enter D({i}): "))

# Encode and sum signals (CDMA encoding)
resultant_channel = sum(np.multiply(codes[i], data_bits[i]) for i in range(1, 5))
print("\nResultant Channel Signal:", resultant_channel)

# Select a channel to decode
channel = int(input("\nEnter the station to listen for (C1=1, C2=2, C3=3, C4=4): "))

if channel in codes:
    # Decode the signal using inner product
    inner_product = np.multiply(resultant_channel, codes[channel])
    received_bit = sum(inner_product) / len(inner_product)  # Normalize

    print("Decoded Data Bit:", received_bit)
else:
    print("Invalid channel selection.")
def setup_username(name):
    if len(name) > 7:
        print("Invalid Username. Must be within 7 character")
    else:
        print("Username setup completed!")


setup_username("masum")


def is_even(number):
    if number % 2 == 0:
        return True
    return False
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    
    # If there is a remainder, we need one additional block
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    
    # Otherwise, return the total size of the full blocks
    return full_blocks * block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
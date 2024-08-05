from luxtronik import Luxtronik

# Create a Luxtronik instance with the IP and port
l = Luxtronik('192.168.1.53', 8889)

# Open a file in write mode
with open('luxtronik.txt', 'w') as file:
    # Function to write to file instead of printing
    def write_to_file(content):
        file.write(content + '\n')
    
    # Write parameters
    write_to_file("=" * 80)
    write_to_file('{:^80}'.format(' Parameters '))
    write_to_file("=" * 80)

    for n, p in l.parameters.parameters.items():
        write_to_file(f"Number: {n:<5} Name: {p.name:<60} Type: {p.__class__.__name__:<20} Value: {p.value}")

    # Write calculations
    write_to_file("=" * 80)
    write_to_file('{:^80}'.format(' Calculations '))
    write_to_file("=" * 80)

    for n, c in l.calculations.calculations.items():
        write_to_file(f"Number: {n:<5} Name: {c.name:<60} Type: {c.__class__.__name__:<20} Value: {c.value}")

    # Write visibilities
    write_to_file("=" * 80)
    write_to_file('{:^80}'.format(' Visibilities '))
    write_to_file("=" * 80)

    for n, v in l.visibilities.visibilities.items():
        write_to_file(f"Number: {n:<5} Name: {v.name:<60} Type: {v.__class__.__name__:<20} Value: {v.value}")

print("Data has been written to luxtronik.txt")

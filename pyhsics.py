def calculate_force(mass, acceleration):
    """Calculate force using Newton's second law: F = m * a"""
    return mass * acceleration

def calculate_kinetic_energy(mass, velocity):
    """Calculate kinetic energy: KE = 0.5 * m * v^2"""
    return 0.5 * mass * velocity ** 2

def calculate_potential_energy(mass, height, gravity=9.81):
    """Calculate potential energy: PE = m * g * h"""
    return mass * gravity * height

def main():
    print("Select calculation:")
    print("1. Force")
    print("2. Kinetic Energy")
    print("3. Potential Energy")

    choice = input("Enter choice(1/2/3): ")

    if choice == '1':
        mass = float(input("Enter mass (kg): "))
        acceleration = float(input("Enter acceleration (m/s^2): "))
        print(f"Force = {calculate_force(mass, acceleration)} N")
    elif choice == '2':
        mass = float(input("Enter mass (kg): "))
        velocity = float(input("Enter velocity (m/s): "))
        print(f"Kinetic Energy = {calculate_kinetic_energy(mass, velocity)} J")
    elif choice == '3':
        mass = float(input("Enter mass (kg): "))
        height = float(input("Enter height (m): "))
        print(f"Potential Energy = {calculate_potential_energy(mass, height)} J")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
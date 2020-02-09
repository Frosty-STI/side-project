def break_primes():
    prime = int(input("Name one prime number."))
    print()
    reverse = 1/prime
    extrapolation = prime**2
    
    print(f"Sorry, that isn't a prime. {prime} is actually comprised of {reverse} * {extrapolation}. This is, in essence, {reverse*extrapolation}.")

def find_derivative():
    func = input("Enter a function to take the derivative of. Use x.")
    for i in range(len(func)):
        if func[i] == 0:
            pass


def main():
    print("what kind of mathematical fun do you want to have?")

if __name__ == "__main__":
    break_primes()
    print()
    
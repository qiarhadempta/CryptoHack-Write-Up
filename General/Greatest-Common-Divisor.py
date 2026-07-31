def findGCD(a, b):
    if a == 0:
        return b
    return findGCD(b % a, a)

# Main function
def main():
    a, b = 35, 15
    g = findGCD(a, b)
    print(g)

if __name__ == "__main__":
    main()

# reference: https://www.geeksforgeeks.org/dsa/euclidean-algorithms-basic-and-extended/

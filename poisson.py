import math

def poisson_pdf(k, lam):
    return lam**k * math.exp(-lam) / math.factorial(k)

if __name__ == "__main__":
    print(f"{poisson_pdf(5, 2.5):.3f}")
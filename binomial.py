def calc_table(n, k, n_k_table):

    # if already filled, don't calc again
    if n_k_table[n][k]:
        return n_k_table[n][k]

    # if hit limit return
    if (k == 0) or (k == n):
        n_k_table[n][k] = 1
        return n_k_table[n][k]

    n_k_table[n][k] = calc_table(n-1, k, n_k_table) + calc_table(n-1, k-1, n_k_table)
    return n_k_table[n][k]

def n_choose_k(n, k):
    # use relationship that (n, k) = (n-1, k) + (n-1, k-1)
    n_k_table = [[None for x in range(k+1)] for x in range(n+1)]
    
    return calc_table(n, k, n_k_table)

def binomial(n, k, p):
    return n_choose_k(n, k)*p**k*(1-p)**(n-k)

def geometric(n, p):
    return ((1-p)**(n-1))*p

def geo_cdf(n, p):
    return 1 - (1-p)**n

if __name__ == "__main__":
    # l, r = list(map(float, input().split(" ")))
    # p = float(l) / float(l + r)
    # all_chances = sum([binomial(6, k, p) for k in range(3,7)])
    # print(f"{all_chances:.3f}")

    # p, n = input().split(" ")
    # p = float(p) / 100.
    # n = int(n)
    # no_more_than_2 = sum([binomial(n, k, p) for k in range(3)])
    # at_least_2 = sum([binomial(n, k, p) for k in range(2, n)])
    # print(f"{no_more_than_2:.3f}")
    # print(f"{at_least_2:.3f}")

    p = 1. / 3.
    n = 5
    print(f"{geometric(n, p):.3f}")
    print(f"{geo_cdf(n, p):.3f}")

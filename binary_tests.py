from binary_to_mod8 import binary_to_mod8
import matplotlib.pyplot as plt


if __name__ == "__main__":
    e = binary_to_mod8("e.txt")
    pi = binary_to_mod8("pi.txt")
    sqrt2 = binary_to_mod8("sqrt2.txt")

    plt.hist(e, bins=8, density=True, rwidth=0.85, alpha=0.7)
    plt.ylim(0.12, 0.15)
    plt.title(r"Density histogram of $e$ transformed to modulo 8")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.show()
    plt.hist(pi, bins=8, density=True, rwidth=0.85, alpha=0.7, color="r")
    plt.ylim(0.12, 0.15)
    plt.title(r"Density histogram of $\pi$ transformed to modulo 8")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.show()
    plt.hist(sqrt2, bins=8, density=True, rwidth=0.85, alpha=0.7, color="orange")
    plt.ylim(0.12, 0.15)
    plt.title(r"Density histogram of $\sqrt{2}$ transformed to modulo 8")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.show()


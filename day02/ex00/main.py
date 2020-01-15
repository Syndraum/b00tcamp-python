import functools
from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce


def addition(n):
    return n + n


def afficher(a, b):
    return a + b


print("===== map =====")
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
result = ft_map(addition, numbers)
print(list(result))
chaine = ("a", "b", "c", "d")
result = map(addition, chaine)
print(list(result))
result = ft_map(addition, chaine)
print(list(result))

print("\n===== filter =====")
seq = [0, 1, 2, 3, 5, 8, 13]
result = filter(lambda x: x % 2, seq)
print(list(result))
result = filter(lambda x: x % 2, seq)
print(list(result))

print("\n===== reduce =====")
res = functools.reduce(afficher, range(10))
print("Résultat final", res)
res = ft_reduce(afficher, range(10))
print("Résultat final", res)

tout_est_vrai = [1, 1, 1, 1]
certains_sont_vrais = [1, 0, 1, 0]
tout_est_faux = [0, 0, 0, 0]
print(bool(functools.reduce(lambda a, b: a and b, tout_est_vrai)))
print(bool(ft_reduce(lambda a, b: a and b, tout_est_vrai)))
print(bool(functools.reduce(lambda a, b: a and b, certains_sont_vrais)))
print(bool(ft_reduce(lambda a, b: a and b, certains_sont_vrais)))

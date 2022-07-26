from functools import reduce

def main():
    n_raw = (input('Ingrese una lista de numeros enteros separados por espacios: ')).split(' ')
    n_raw = [int(x) for x in n_raw]
    n = list(filter(lambda x: x%2 != 0, n_raw))
    n = reduce(lambda a,b: a+b, n)
    print(f'Los numeros impares de la lista {tuple(n_raw)} suman {n}')

if __name__ == '__main__':
    main()

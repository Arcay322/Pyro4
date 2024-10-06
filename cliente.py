import Pyro4

def request_factorial(n):
    factorial_server = Pyro4.Proxy("PYRONAME:example.factorial")  # Usar el nombre registrado
    try:
        result = factorial_server.factorial(n)
        print(f"El factorial de {n} es: {result}")
    except Exception as e:
        print(f"Error al calcular el factorial: {e}")

if __name__ == "__main__":
    num = int(input("Ingresa un número para calcular su factorial: "))
    request_factorial(num)

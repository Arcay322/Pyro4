import Pyro4
from servidor import FactorialServer
import threading

# Función para iniciar el servidor de nombres
def start_nameserver():
    Pyro4.naming.startNS(host='0.0.0.0', port=9090)  # Escuchar en todas las direcciones
    print("Servidor de nombres iniciado en 0.0.0.0:9090")

# Crear un hilo para el servidor de nombres
ns_thread = threading.Thread(target=start_nameserver)
ns_thread.start()

# Iniciar el servidor Pyro
daemon = Pyro4.Daemon()  # Iniciar el servidor Pyro
uri = daemon.register(FactorialServer)  # Registrar el objeto remoto
ns = Pyro4.locateNS()  # Localizar el servicio de nombres
ns.register("example.factorial", uri)  # Registrar el objeto con un nombre

print("Servidor de nombres y servidor de factorial están corriendo.")
daemon.requestLoop()  # Iniciar el bucle del servidor

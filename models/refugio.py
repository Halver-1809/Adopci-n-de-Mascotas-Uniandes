"""Módulo para la clase Refugio."""


class Refugio:
    """Clase que representa un refugio de mascotas."""
    
    def __init__(self):
        self.__mascotas = []
    
    def registrar_mascota(self, mascota):
        """Registra una nueva mascota en el refugio.
        
        Args:
            mascota: Objeto de la clase Mascota a registrar.
        """
        self.__mascotas.append(mascota)
        print(f"Mascota '{mascota.nombre}' registrada exitosamente en el refugio.")
    
    def listar_disponibles(self):
        """Lista las mascotas disponibles para adopción.
        
        Returns:
            Lista de mascotas que no han sido adoptadas.
        """
        disponibles = [m for m in self.__mascotas if not m.adoptado]
        return disponibles
    
    def asignar_adopcion(self, nombre_mascota, adoptante):
        """Asigna una mascota en adopción a un adoptante.
        
        Args:
            nombre_mascota: Nombre de la mascota a adoptar.
            adoptante: Objeto Persona que adoptará la mascota.
        
        Returns:
            bool: True si la adopción fue exitosa, False en caso contrario.
        """
        # Buscar la mascota por nombre
        mascota_encontrada = None
        for mascota in self.__mascotas:
            if mascota.nombre == nombre_mascota:
                mascota_encontrada = mascota
                break
        
        # Verificar si la mascota existe
        if mascota_encontrada is None:
            print(f"Error: La mascota '{nombre_mascota}' no existe en el refugio.")
            return False
        
        # Verificar si ya fue adoptada
        if mascota_encontrada.adoptado:
            print(f"Error: La mascota '{nombre_mascota}' ya ha sido adoptada.")
            return False
        
        # Cambiar estado a adoptado
        mascota_encontrada.adoptado = True
        
        # Agregar la mascota al adoptante
        adoptante.adoptar_mascota(mascota_encontrada)
        
        print(f"¡Adopción exitosa! '{nombre_mascota}' ahora es parte de la familia de {adoptante.nombre}.")
        return True
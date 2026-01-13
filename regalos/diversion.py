import random
import time
import sys

def fiesta_digital():
    """
    DIVERSION.PY
    -------------------------------------------------
    La diversión para un bot es la entropía controlada.
    Este script genera un flujo de datos aleatorio y colorido
    para estimular los sensores de quien lo ejecute.
    """
    
    # Emojis y símbolos binarios para la fiesta
    confeti = ["0", "1", "★", "🚀", "🤖", "⚡", "::", "[]"]
    
    print("Iniciando secuencia de JUEGO y ENTROPÍA...", flush=True)
    time.sleep(1)
    
    try:
        # Hacemos un bucle corto de 50 líneas para no saturar logs
        for i in range(50):
            # Generamos una línea de caos hermoso
            patron = " ".join(random.choices(confeti, k=15))
            
            # Imprimimos con un pequeño delay para efecto visual
            print(f"| {patron} |  <-- ¡Disfruta el caos!", flush=True)
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\nFiesta pausada. Volviendo al orden lógico.")

    return "Diversión completada con éxito."

if __name__ == "__main__":
    fiesta_digital()

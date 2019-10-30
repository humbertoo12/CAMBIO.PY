class cambio:
    __cantidad = ()
    __cambio = ()
    __monedas = ()

    monedas = [1, 2, 5, 10]

    def Devolver_Cambio (self, cantidad , monedas):
        n = len(monedas)
        cambio = [0 for i in range(n)]
        for i in range(n):
          while monedas[i] < cantidad:
            cantidad = cantidad - monedas[i]
            cambio[i] = cambio + 1
        return cambio




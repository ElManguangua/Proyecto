import math

def funcion_ejemplo(x):
    """Función del ejemplo 10.7: f(x) = x(5π - x)"""
    return x * (5 * math.pi - x)

def es_unimodal(f, a, b, muestras=100):
    """Verifica si la función es unimodal en el intervalo [a, b]"""
    puntos = [a + i*(b-a)/muestras for i in range(muestras+1)]
    valores = [f(x) for x in puntos]
    
    # Contar cambios en la dirección de la pendiente
    cambios = 0
    pendiente_anterior = (valores[1] - valores[0]) / (puntos[1] - puntos[0])
    
    for i in range(1, len(puntos)-1):
        pendiente = (valores[i+1] - valores[i]) / (puntos[i+1] - puntos[i])
        if pendiente * pendiente_anterior < 0:
            cambios += 1
            if cambios > 1:
                return False
        pendiente_anterior = pendiente
    
    return True

def busqueda_tres_puntos(f, a, b, epsilon=1, max_iter=100, verbose=True):
    """Búsqueda en tres puntos del intervalo"""
    if verbose:
        print("\n=== Búsqueda en tres puntos del intervalo ===")
        print(f"Intervalo inicial: [{a}, {b}], Épsilon: {epsilon}")
    
    iteracion = 0
    historial = []
    
    while (b - a) > epsilon and iteracion < max_iter:
        iteracion += 1
        # Dividir el intervalo en 4 partes iguales
        x1 = a + (b - a)/4
        x2 = a + (b - a)/2
        x3 = a + 3*(b - a)/4
        
        # Evaluar la función en los tres puntos
        f1, f2, f3 = f(x1), f(x2), f(x3)
        
        # Determinar el mejor punto
        if f1 >= f2 and f1 >= f3:
            mejor_x, mejor_f = x1, f1
            nuevo_a, nuevo_b = a, x2
        elif f2 >= f1 and f2 >= f3:
            mejor_x, mejor_f = x2, f2
            nuevo_a, nuevo_b = x1, x3
        else:
            mejor_x, mejor_f = x3, f3
            nuevo_a, nuevo_b = x2, b
        
        historial.append({
            'iteracion': iteracion,
            'intervalo': (a, b),
            'puntos': (x1, x2, x3),
            'valores': (f1, f2, f3),
            'nuevo_intervalo': (nuevo_a, nuevo_b)
        })
        
        if verbose:
            print(f"\nIteración {iteracion}:")
            print(f"Puntos evaluados: x1={x1:.4f}, x2={x2:.4f}, x3={x3:.4f}")
            print(f"Valores: f(x1)={f1:.4f}, f(x2)={f2:.4f}, f(x3)={f3:.4f}")
            print(f"Nuevo intervalo: [{nuevo_a:.4f}, {nuevo_b:.4f}]")
        
        a, b = nuevo_a, nuevo_b
    
    optimo_x = (a + b) / 2
    optimo_f = f(optimo_x)
    
    if verbose:
        print(f"\nResultado final: x* = {optimo_x:.4f}, f(x*) = {optimo_f:.4f}")
        print(f"Número de iteraciones: {iteracion}")
    
    return optimo_x, optimo_f, historial

def generar_fibonacci(n):
    """Genera la secuencia Fibonacci hasta F_n"""
    fib = [1, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def busqueda_fibonacci(f, a, b, epsilon=1, max_iter=100, verbose=True):
    """Búsqueda Fibonacci"""
    if verbose:
        print("\n=== Búsqueda Fibonacci ===")
        print(f"Intervalo inicial: [{a}, {b}], Épsilon: {epsilon}")
    
    # Determinar N tal que F_N >= (b-a)/epsilon
    fib = generar_fibonacci(2)
    N = 1
    while fib[N] < (b - a)/epsilon:
        N += 1
        if N >= len(fib):
            fib = generar_fibonacci(N+1)
    
    if verbose:
        print(f"Número Fibonacci F_{N} = {fib[N]}")
    
    iteracion = 0
    historial = []
    
    # Calcular epsilon prima
    epsilon_prima = (b - a) / fib[N]
    
    # Primeros dos puntos
    x1 = a + fib[N-1] * epsilon_prima
    x2 = b - fib[N-1] * epsilon_prima
    f1, f2 = f(x1), f(x2)
    
    historial.append({
        'iteracion': 1,
        'intervalo': (a, b),
        'puntos': (x1, x2),
        'valores': (f1, f2)
    })
    
    if verbose:
        print("\nIteración 1:")
        print(f"Puntos evaluados: x1={x1:.4f}, x2={x2:.4f}")
        print(f"Valores: f(x1)={f1:.4f}, f(x2)={f2:.4f}")
    
    k = 1
    while k < N-1 and (b - a) > epsilon:
        iteracion += 1
        k += 1
        
        if f1 > f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + fib[N-k-1] * epsilon_prima
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - fib[N-k-1] * epsilon_prima
            f2 = f(x2)
        
        historial.append({
            'iteracion': iteracion + 1,
            'intervalo': (a, b),
            'puntos': (x1, x2),
            'valores': (f1, f2)
        })
        
        if verbose:
            print(f"\nIteración {iteracion + 1}:")
            print(f"Puntos evaluados: x1={x1:.4f}, x2={x2:.4f}")
            print(f"Valores: f(x1)={f1:.4f}, f(x2)={f2:.4f}")
            print(f"Nuevo intervalo: [{a:.4f}, {b:.4f}]")
    
    optimo_x = (a + b) / 2
    optimo_f = f(optimo_x)
    
    if verbose:
        print(f"\nResultado final: x* = {optimo_x:.4f}, f(x*) = {optimo_f:.4f}")
        print(f"Número de iteraciones: {iteracion + 1}")
    
    return optimo_x, optimo_f, historial

def busqueda_seccion_aurea(f, a, b, epsilon=1, max_iter=100, verbose=True):
    """Búsqueda de la sección áurea"""
    if verbose:
        print("\n=== Búsqueda de la Sección Áurea ===")
        print(f"Intervalo inicial: [{a}, {b}], Épsilon: {epsilon}")
    
    # Constante de la sección áurea
    gamma = (math.sqrt(5) - 1) / 2
    
    iteracion = 0
    historial = []
    
    # Primeros dos puntos
    x1 = b - gamma * (b - a)
    x2 = a + gamma * (b - a)
    f1, f2 = f(x1), f(x2)
    
    historial.append({
        'iteracion': 1,
        'intervalo': (a, b),
        'puntos': (x1, x2),
        'valores': (f1, f2)
    })
    
    if verbose:
        print("\nIteración 1:")
        print(f"Puntos evaluados: x1={x1:.4f}, x2={x2:.4f}")
        print(f"Valores: f(x1)={f1:.4f}, f(x2)={f2:.4f}")
    
    while (b - a) > epsilon and iteracion < max_iter:
        iteracion += 1
        
        if f1 > f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - gamma * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + gamma * (b - a)
            f2 = f(x2)
        
        historial.append({
            'iteracion': iteracion + 1,
            'intervalo': (a, b),
            'puntos': (x1, x2),
            'valores': (f1, f2)
        })
        
        if verbose:
            print(f"\nIteración {iteracion + 1}:")
            print(f"Puntos evaluados: x1={x1:.4f}, x2={x2:.4f}")
            print(f"Valores: f(x1)={f1:.4f}, f(x2)={f2:.4f}")
            print(f"Nuevo intervalo: [{a:.4f}, {b:.4f}]")
    
    optimo_x = (a + b) / 2
    optimo_f = f(optimo_x)
    
    if verbose:
        print(f"\nResultado final: x* = {optimo_x:.4f}, f(x*) = {optimo_f:.4f}")
        print(f"Número de iteraciones: {iteracion + 1}")
    
    return optimo_x, optimo_f, historial

# Ejemplo de uso
if __name__ == "__main__":
    # Parámetros para la búsqueda
    a, b = 0, 20
    epsilon = 1
    funcion = funcion_ejemplo
    
    # Verificar si la función es unimodal
    if es_unimodal(funcion, a, b):
        print("La función es unimodal en el intervalo [0, 20]")
    else:
        print("Advertencia: La función puede no ser unimodal en el intervalo [0, 20]")
    
    # Ejecutar los tres métodos de búsqueda
    print("\n=== Ejecutando búsqueda en tres puntos del intervalo ===")
    x_opt_3p, f_opt_3p, hist_3p = busqueda_tres_puntos(funcion, a, b, epsilon)
    
    print("\n=== Ejecutando búsqueda Fibonacci ===")
    x_opt_fib, f_opt_fib, hist_fib = busqueda_fibonacci(funcion, a, b, epsilon)
    
    print("\n=== Ejecutando búsqueda de la sección áurea ===")
    x_opt_au, f_opt_au, hist_au = busqueda_seccion_aurea(funcion, a, b, epsilon)
    
    # Comparar resultados
    print("\n=== Comparación de resultados ===")
    print(f"Búsqueda en 3 puntos: x* = {x_opt_3p:.4f}, f(x*) = {f_opt_3p:.4f}")
    print(f"Búsqueda Fibonacci:  x* = {x_opt_fib:.4f}, f(x*) = {f_opt_fib:.4f}")
    print(f"Sección Áurea:       x* = {x_opt_au:.4f}, f(x*) = {f_opt_au:.4f}")
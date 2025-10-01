import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from scipy import integrate

def f(x):
    return x**2 + 2 * x

# Intervalo p/ integração
a = 0
b = np.pi

# Dados da função
x = np.linspace(a, b, 200)
y = f(x)

# Figura
fig, ax = plt.subplots()
ax.plot(x, y, 'b-', label='f(x)')
ax.set_title("Área sob a curva (Trabalho total)")
ax.set_xlabel("x")
ax.set_ylabel("F(x)")
ax.legend()

area = ax.fill_between([], [], color='lightblue', alpha=0.5)
text = ax.text(0.05, 0.9, "", transform=ax.transAxes)

def update(frame):
    ax.collections.clear()
    current_x = x[:frame]
    current_y = y[:frame]

    ax.fill_between(current_x, current_y, color='lightblue', alpha=0.5)

    if len(current_x) > 1:
        dx = current_x[1] - current_x[0]
        integral_aproximada = np.sum(current_y * dx)
        text.set_text(f"Área ≈ {integral_aproximada:.2f}")

    return ax.collections + [text]

ani = FuncAnimation(fig, update, frames=len(x), interval=50, blit=False, repeat=False)
plt.show()

resultado, erro = integrate.quad(f, a, b)

print(f"A definição da integral de f(x) de {a} para {b} é: {resultado:.4f}")
print(f"Erro estimado: {erro}")

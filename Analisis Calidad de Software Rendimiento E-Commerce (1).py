import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("\n Análisis de Rendimiento — Plataforma E-commerce", fontsize=14, fontweight='bold', y=1.02)

# --- Gráfico 1: Latencia por escenario ---
ax1 = axes[0]
escenarios = ['Día normal', 'Hora pico', 'Día de Promoción']
promedio = [1.8, 3.5, 3.9]
pico = [6, 6, 12]
x = np.arange(len(escenarios))
width = 0.35

bars1 = ax1.bar(x - width/2, promedio, width, label='Promedio', color='#378ADD', zorder=3)
bars2 = ax1.bar(x + width/2, pico, width, label='Pico máximo', color='#E24B4A', zorder=3)
ax1.set_title('Latencia por escenario', fontweight='bold')
ax1.set_ylabel('Segundos')
ax1.set_xticks(x)
ax1.set_xticklabels(escenarios, fontsize=9)
ax1.legend(fontsize=9)
ax1.grid(axis='y', linestyle='--', alpha=0.4, zorder=0)
ax1.set_axisbelow(True)
for bar in bars1:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
             f'{bar.get_height()}s', ha='center', va='bottom', fontsize=8)
for bar in bars2:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
             f'{bar.get_height()}s', ha='center', va='bottom', fontsize=8)

# --- Gráfico 2: Usuarios concurrentes por escenario ---
ax2 = axes[1]
escenarios2 = ['Día normal', 'Día de Promoción']
usuarios = [900, 4500]
colores = ['#1D9E75', '#E24B4A']

bars3 = ax2.bar(escenarios2, usuarios, color=colores, width=0.4, zorder=3)
ax2.axhline(y=1000, color='#BA7517', linestyle='--', linewidth=1.5, label='Capacidad cómoda', zorder=4)
ax2.set_title('Usuarios concurrentes', fontweight='bold')
ax2.set_ylabel('Usuarios')
ax2.legend(fontsize=9)
ax2.grid(axis='y', linestyle='--', alpha=0.4, zorder=0)
ax2.set_axisbelow(True)
for bar, val in zip(bars3, usuarios):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 60,
             f'{val:,}'.replace(',', '.'), ha='center', va='bottom', fontsize=9, fontweight='bold')

# --- Gráfico 3: Disponibilidad objetivo vs real ---
ax3 = axes[2]
categorias = ['Escenario Objetivo', 'Escenario Real']
valores = [99.9, 98.7]
colores3 = ['#378ADD', '#E24B4A']

bars4 = ax3.bar(categorias, valores, color=colores3, width=0.35, zorder=3)
ax3.set_title('Disponibilidad (%)', fontweight='bold')
ax3.set_ylabel('Porcentaje (%)')
ax3.set_ylim(98, 100.2)
ax3.grid(axis='y', linestyle='--', alpha=0.4, zorder=0)
ax3.set_axisbelow(True)
for bar, val in zip(bars4, valores):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
             f'{val}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('graficos_rendimiento.png', dpi=150, bbox_inches='tight')
plt.show()
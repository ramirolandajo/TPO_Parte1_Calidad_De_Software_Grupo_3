# TPO – Calidad de Software | Parte I | Grupo 3

**Universidad Argentina de la Empresa (UADE)**
Facultad de Ingeniería y Ciencias Exactas (FAIN) — Ingeniería en Informática

**Materia:** Calidad de Software

**Profesor/a:** Dra. Ing. Martinez Roxana

**Día/Turno:** Jueves – Mañana

**Año:** 2026

---

## Integrantes

| Nombre | LU |
|---|---|
| Nicolas Facundo Llousas | 1147795 |
| Lucas Valentin Vazquez | 1148671 |
| Nicolas Casais | 1185300 |
| Ramiro Landajo | 1155576 |
| Santiago Larre | 1158242 |

---

## Contenido del repositorio


### Evaluación del Costo de Calidad (CoQ)
Hoja de cálculo Excel (`Costos_Calidad_MediSalud_Grupo3_TPO.xlsx`) con el análisis de costos de calidad aplicado al caso práctico del desarrollo de la app móvil de **MediSalud S.A.** Incluye:
- Clasificación de 20 ítems en las categorías: Prevención, Evaluación, Fallas Internas y Fallas Externas
- Subtotales por categoría y costo total de calidad (CoQ)
- Gráficos de barras y torta con distribución porcentual
- Hallazgos y recomendaciones de mejora

### Análisis de Rendimiento: Plataforma E-Commerce
Script Python (`Analisis Calidad de Software Rendimiento E-Commerce.py`) que genera gráficos comparativos de:
- Latencia por escenario (día normal, hora pico, día de promoción)
- Usuarios concurrentes soportados vs. capacidad límite
- Disponibilidad objetivo vs. real del sistema

**Requisitos:** `matplotlib`, `numpy`
```bash
pip install matplotlib numpy
python "Analisis Calidad de Software Rendimiento E-Commerce.py"
```

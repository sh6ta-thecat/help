# 🆘 help
> *"Ayuda innecesaria, [guía para dummies]"*

Este repositorio es una colección de scripts útiles (y quizá innecesarios) para automatizar tareas rápidas.

---

## 🗂️ Índice de Scripts

### 1. 🪟 ventana.py
**Descripción:** 
Un script corto que fuerza la apertura de sitios web en una ventana flotante independiente. Es ideal para sitios que se resisten a ser abiertos en marcos comunes o para tener una referencia siempre a la vista.

**¿Cómo funciona?**
*   **Independencia:** No depende de Chrome, Firefox o Safari; usa su propio motor (`pywebview`).
*   **Modo Siempre Arriba:** La ventana está configurada con `on_top=True`, lo que significa que no se perderá detrás de otras carpetas o programas.
*   **Evasión:** Al ser una instancia limpia, carga sitios que normalmente bloquean su visualización en navegadores convencionales.

**Uso rápido:**
1. Instala la dependencia: `pip install pywebview`
2. Ejecuta: `python ventana.py`

---

## 🛠️ Requisitos Generales
*   Python 3.x
*   Instalacion de la libreria *webview*
  ```bash
# Instalar la librería necesaria
pip install pywebview
```

---
*Próximamente más scripts...*

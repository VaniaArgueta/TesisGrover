# API REST búsqueda cuántica con Algoritmo de Grover

Este proyecto de tesis implementa una API REST utilizando Flask, desarrollada para ejecutar búsquedas sobre un conjunto de datos de objetos candidatos a ser catalogados como exoplanetas, aplicando el Algoritmo de Grover. La búsqueda se ejecutará tanto en un simulador local como en hardware cuántico real de IBM Quantum Platform.

---

## Tecnologías Utilizadas

- Python 3.10+
- Flask 3.x
- Google Cloud Platform (Compute Engine, Cloud SQL)
- IBM Quantum Experience
- Qiskit

---

## Estructura del Proyecto



---

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/VaniaArgueta/TesisGrover.git
cd TesisGrover
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

O en CMD:

```bash
venv\Scripts\activate.bat
```

Linux o Mac:

```bash
source venv/bin/activate
```

### 4. Instalación de dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución de la API

Levantar el servidor de desarrollo:

```bash
python app.py
```

La API REST estará disponible en:

```
http://127.0.0.1:5000/
```

---

## Endpoints

| Método | URL | Descripción |
|:-------|:----|:------------|
| POST | /etl/ejecutar | Ejecuta el proceso ETL para transformar los datos. |
| POST | /busqueda/simulacion | Ejecuta búsqueda usando simulación cuántica local. |
| POST | /busqueda/hardware-ibm | Ejecuta búsqueda usando hardware cuántico real de IBM. |

---

## Formato del Body para endpoints de búsqueda

El body de la solicitud debe ser en formato JSON (raw):

```json
{
  "nombre_planeta": "Kepler-22b",
  "radio_minimo": 1.0,
  "radio_maximo": 3.0,
  "masa_minima": 0.5,
  "masa_maxima": 5.0
}
```

Todos los parámetros son opcionales. Si no se envía ningún valor, es decir, el JSON vacío, se realizará una búsqueda sobre todo el conjunto de datos.

---

## Documentación API REST

La documentación completa de la API está publicada en Postman, disponible en el siguiente link:

[Documentación endpoints](https://documenter.getpostman.com/view/23237083/2sB2j1hCbr)

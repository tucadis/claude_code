# Módulo 3: Inicio de un Proyecto con Claude Code

## 📖 Introducción

En este módulo aprenderás a crear y configurar proyectos para trabajar con Claude Code. Explorarás la interfaz, comandos básicos y cómo Claude Code puede ayudarte en tu flujo de trabajo diario.

### Objetivos del módulo

- Crear la estructura básica de un proyecto
- Inicializar control de versiones con Git
- Iniciar sesiones de Claude Code
- Explorar comandos y funcionalidades
- Entender el contexto de trabajo de Claude

---

## 📁 Paso 1: Creación de un Proyecto Nuevo

### 1.1 Crear directorio del proyecto

```bash
# Ir al directorio home
cd ~

# Crear directorio para proyectos
mkdir -p ~/proyectos

# Navegar al directorio
cd ~/proyectos

# Crear directorio del proyecto
mkdir mi-primer-proyecto-claude

# Entrar al proyecto
cd mi-primer-proyecto-claude
```

**Verificar ubicación:**
```bash
# Ver ruta actual
pwd
```

**Salida esperada:**
```
/home/tucadis/proyectos/mi-primer-proyecto-claude
```

### 1.2 Crear estructura básica de archivos

```bash
# Crear directorios del proyecto
mkdir -p src tests docs

# Crear archivos básicos
touch README.md
touch src/main.py
touch tests/test_main.py
touch .gitignore
```

**Verificar estructura:**
```bash
# Listar estructura con tree (instalar si no está disponible)
tree
```

**O manualmente:**
```bash
# Listar estructura
ls -la
```

**Salida esperada:**
```
.
├── .gitignore
├── README.md
├── docs/
├── src/
│   └── main.py
└── tests/
    └── test_main.py
```

### 1.3 Crear contenido inicial

```bash
# Crear README básico
cat > README.md << 'EOF'
# Mi Primer Proyecto con Claude Code

Este es mi primer proyecto utilizando Claude Code como asistente de desarrollo.

## Descripción

Proyecto de aprendizaje para explorar las capacidades de Claude Code.

## Estructura del Proyecto

```
mi-primer-proyecto-claude/
├── README.md           # Este archivo
├── src/                # Código fuente
│   └── main.py        # Archivo principal
├── tests/              # Tests
│   └── test_main.py   # Tests del código principal
└── docs/               # Documentación
```

## Tecnologías

- Python 3.x
- Claude Code para asistencia en desarrollo

## Autor

Tu Nombre
EOF
```

```bash
# Crear archivo .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Environment variables
.env
.env.local

# Logs
*.log
EOF
```

```bash
# Crear archivo Python básico
cat > src/main.py << 'EOF'
#!/usr/bin/env python3
"""
Archivo principal del proyecto.
"""

def main():
    """Función principal del programa."""
    print("¡Hola desde mi primer proyecto con Claude Code!")

if __name__ == "__main__":
    main()
EOF
```

**Verificar contenido:**
```bash
# Ver contenido del README
cat README.md

# Ver contenido del archivo Python
cat src/main.py
```

---

## 🔧 Paso 2: Inicializar Git (Control de Versiones)

### 2.1 Configurar Git (si no está configurado)

```bash
# Verificar si git está instalado
git --version
```

**Si no está instalado:**
```bash
# Instalar git
sudo apt update
sudo apt install git -y
```

### 2.2 Configuración inicial de Git

```bash
# Configurar nombre de usuario
git config --global user.name "Tu Nombre"

# Configurar email
git config --global user.email "tu.email@ejemplo.com"

# Configurar editor predeterminado
git config --global core.editor nano

# Verificar configuración
git config --list
```

**Salida esperada:**
```
user.name=Tu Nombre
user.email=tu.email@ejemplo.com
core.editor=nano
```

### 2.3 Inicializar repositorio Git

```bash
# Inicializar repositorio
git init
```

**Salida esperada:**
```
Initialized empty Git repository in /home/tucadis/proyectos/mi-primer-proyecto-claude/.git/
```

### 2.4 Primer commit

```bash
# Ver estado del repositorio
git status
```

**Salida esperada:**
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        README.md
        src/
        tests/

nothing added to commit but untracked files present (use "git add" to track)
```

```bash
# Añadir todos los archivos al staging
git add .

# Verificar qué se va a commitear
git status
```

**Salida esperada:**
```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   README.md
        new file:   src/main.py
        new file:   tests/test_main.py
```

```bash
# Crear primer commit
git commit -m "Initial commit: estructura básica del proyecto"
```

**Salida esperada:**
```
[main (root-commit) a1b2c3d] Initial commit: estructura básica del proyecto
 4 files changed, 78 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 src/main.py
 create mode 100644 tests/test_main.py
```

```bash
# Ver historial de commits
git log --oneline
```

**Salida esperada:**
```
a1b2c3d (HEAD -> main) Initial commit: estructura básica del proyecto
```

---

## 🚀 Paso 3: Iniciar Claude Code

### 3.1 Iniciar sesión interactiva

```bash
# Asegurarse de estar en el directorio del proyecto
cd ~/proyectos/mi-primer-proyecto-claude

# Iniciar Claude Code
claude
```

**Salida esperada:**
```
Starting Claude Code...
Connected to Claude 3.5 Sonnet

Working directory: /home/tucadis/proyectos/mi-primer-proyecto-claude
Type 'help' for available commands or start chatting!

You:
```

### 3.2 Primer contacto con Claude

**Escribe en la sesión de Claude:**
```
Hola Claude, estoy en un nuevo proyecto. ¿Puedes ver qué archivos hay aquí?
```

**Claude responderá algo como:**
```
Claude: ¡Hola! Veo que tienes un proyecto Python con la siguiente estructura:

- README.md: Archivo de documentación del proyecto
- src/main.py: Archivo principal con una función básica
- tests/test_main.py: Archivo para tests (actualmente vacío)
- .gitignore: Configuración de Git para ignorar archivos

¿En qué te gustaría que te ayude con este proyecto?
```

---

## 🎯 Paso 4: Explorar Funcionalidades Básicas

### 4.1 Comandos básicos de Claude Code

**Dentro de una sesión de Claude, prueba estos comandos:**

#### Ver ayuda
```
help
```

**O:**
```
¿Qué comandos puedo usar?
```

#### Leer archivos
```
Lee el archivo README.md
```

**O:**
```
Muéstrame el contenido de src/main.py
```

#### Buscar en archivos
```
Busca la palabra "main" en todos los archivos
```

#### Listar archivos del proyecto
```
¿Qué archivos hay en el proyecto?
```

**O:**
```
Lista todos los archivos .py del proyecto
```

### 4.2 Trabajar con archivos

**Pedir a Claude que modifique código:**

```
Mejora el archivo src/main.py añadiendo:
1. Una función para saludar con un nombre personalizado
2. Documentación completa
3. Type hints
4. Un ejemplo de uso
```

**Claude leerá el archivo y propondrá cambios. Ejemplo de lo que podría sugerir:**

```python
#!/usr/bin/env python3
"""
Archivo principal del proyecto.

Este módulo contiene funciones básicas de saludo.
"""

def saludar(nombre: str) -> str:
    """
    Genera un saludo personalizado.

    Args:
        nombre: El nombre de la persona a saludar.

    Returns:
        Un mensaje de saludo personalizado.

    Examples:
        >>> saludar("Juan")
        '¡Hola, Juan! Bienvenido a mi proyecto con Claude Code.'
    """
    return f"¡Hola, {nombre}! Bienvenido a mi proyecto con Claude Code."

def main() -> None:
    """Función principal del programa."""
    print("¡Hola desde mi primer proyecto con Claude Code!")

    # Ejemplo de uso de la función saludar
    mensaje = saludar("Desarrollador")
    print(mensaje)

if __name__ == "__main__":
    main()
```

**Para aceptar los cambios, Claude escribirá el archivo automáticamente.**

### 4.3 Crear nuevos archivos

```
Crea un archivo src/utils.py con funciones auxiliares para:
1. Validar si una cadena es un email válido
2. Formatear fechas
3. Incluye documentación y tests
```

### 4.4 Ejecutar código

Después de que Claude modifique archivos, puedes probarlos:

```bash
# Ejecutar el script principal
python3 src/main.py
```

**Salida esperada:**
```
¡Hola desde mi primer proyecto con Claude Code!
¡Hola, Desarrollador! Bienvenido a mi proyecto con Claude Code.
```

---

## 💡 Paso 5: Entender el Contexto de Claude

### 5.1 ¿Qué "ve" Claude?

Claude Code tiene acceso a:

1. **Archivos del proyecto**: Puede leer cualquier archivo que le pidas
2. **Estructura de directorios**: Conoce la organización del proyecto
3. **Historial de conversación**: Recuerda lo que has hablado en la sesión actual
4. **Conocimiento general**: Patrones de código, mejores prácticas, sintaxis de lenguajes

### 5.2 Limitaciones importantes

Claude Code **NO** puede:

1. **Ejecutar código directamente**: No puede ejecutar `python script.py` (pero tú sí puedes desde otra terminal)
2. **Acceder a Internet**: No puede descargar librerías o buscar en línea
3. **Recordar sesiones anteriores**: Cada sesión empieza "limpia"
4. **Modificar archivos fuera del proyecto**: Solo trabaja en el directorio actual

### 5.3 Mejores prácticas para comunicarte

**✅ Buenas peticiones:**

```
Lee el archivo main.py y añade manejo de errores a la función principal
```

```
Crea un archivo config.py con constantes para el proyecto
```

```
Refactoriza la función saludar para que soporte múltiples idiomas
```

**❌ Peticiones problemáticas:**

```
Instala la librería requests
```
*Claude puede decirte cómo hacerlo, pero tú debes ejecutar `pip install requests`*

```
Ejecuta los tests
```
*Claude puede crear los tests, pero tú debes ejecutarlos con `pytest`*

---

## 🔍 Paso 6: Comandos Útiles Durante la Sesión

### 6.1 Comandos de navegación

```bash
# Ver directorio actual (desde Claude)
¿En qué directorio estamos?

# Ver estructura del proyecto
Muéstrame la estructura completa del proyecto

# Buscar archivos específicos
¿Hay algún archivo de configuración en el proyecto?
```

### 6.2 Comandos de desarrollo

```bash
# Revisar código
Revisa el archivo main.py y sugiere mejoras

# Generar documentación
Genera documentación para la función saludar

# Crear tests
Crea tests unitarios para las funciones en main.py

# Refactorizar
Refactoriza main.py separando las funciones en módulos
```

### 6.3 Comandos de Git (a través de Claude)

```bash
# Revisar cambios antes de commit
¿Qué archivos he modificado desde el último commit?

# Generar mensaje de commit
Genera un mensaje de commit descriptivo para los cambios actuales

# Revisar historial
Muéstrame el historial de commits
```

**Nota:** Claude puede ayudarte a entender Git y generar comandos, pero los comandos de Git debes ejecutarlos tú en la terminal.

---

## 🎨 Paso 7: Flujo de Trabajo Típico

### 7.1 Flujo de desarrollo con Claude

**1. Iniciar sesión en el proyecto:**
```bash
cd ~/proyectos/mi-primer-proyecto-claude
claude
```

**2. Describir la tarea:**
```
Quiero añadir una función que calcule el factorial de un número
```

**3. Claude crea/modifica el código:**
Claude añadirá la función a `src/main.py` o creará un nuevo archivo.

**4. Revisar y probar:**
```bash
# En otra terminal (sin cerrar Claude)
python3 src/main.py
```

**5. Iterar:**
```
La función funciona, pero necesito que maneje números negativos
```

**6. Commit de cambios:**
```bash
# En otra terminal
git add .
git commit -m "Añadida función factorial con manejo de errores"
```

### 7.2 Trabajar con múltiples terminales

**Terminal 1: Claude Code**
```bash
# Terminal dedicada a Claude
cd ~/proyectos/mi-primer-proyecto-claude
claude
```

**Terminal 2: Ejecución y Git**
```bash
# Terminal para ejecutar código y git
cd ~/proyectos/mi-primer-proyecto-claude

# Ejecutar código
python3 src/main.py

# Comandos git
git status
git add .
git commit -m "mensaje"
```

**Consejo:** En Windows Terminal o VSCode puedes tener múltiples paneles.

---

## 🔄 Paso 8: Gestión de Sesiones

### 8.1 Salir de Claude Code

```
exit
```

**O:**
```
quit
```

**O presiona:** `Ctrl + C` dos veces

### 8.2 Guardar contexto de sesión

**Antes de salir, puedes pedir a Claude:**

```
Resume todo lo que hemos hecho en esta sesión y guárdalo en docs/sesion-log.md
```

Claude creará un archivo con el resumen que podrás consultar después.

### 8.3 Retomar trabajo

**En la próxima sesión:**

```bash
# Iniciar Claude
claude
```

```
Lee el archivo docs/sesion-log.md y continuemos desde donde lo dejamos
```

---

## 📝 Ejercicios Prácticos

### Ejercicio 1: Exploración básica

1. Inicia Claude Code en tu proyecto
2. Pide a Claude que liste todos los archivos
3. Haz que Claude lea el README.md
4. Pide sugerencias de mejora para el README

### Ejercicio 2: Crear nueva funcionalidad

1. Pide a Claude que cree un archivo `src/calculadora.py`
2. Debe incluir funciones para: sumar, restar, multiplicar, dividir
3. Debe tener documentación completa
4. Debe tener type hints
5. Ejecuta el archivo y verifica que funcione

### Ejercicio 3: Testing

1. Pide a Claude que cree tests para `src/calculadora.py`
2. Los tests deben estar en `tests/test_calculadora.py`
3. Deben cubrir casos normales y casos edge (división por cero, etc.)

### Ejercicio 4: Refactorización

1. Pide a Claude que refactorice `src/main.py`
2. Debe separar las funciones en módulos lógicos
3. Debe mejorar la estructura del código
4. Debe mantener la funcionalidad existente

---

## ✅ Checklist de Verificación

Antes de pasar al siguiente módulo, asegúrate de que:

- [ ] Has creado un proyecto con estructura básica
- [ ] Has inicializado Git en el proyecto
- [ ] Has hecho tu primer commit
- [ ] Puedes iniciar Claude Code en el directorio del proyecto
- [ ] Claude puede leer archivos del proyecto
- [ ] Claude puede modificar archivos existentes
- [ ] Claude puede crear nuevos archivos
- [ ] Entiendes qué puede y qué no puede hacer Claude
- [ ] Sabes cómo salir de una sesión de Claude
- [ ] Has probado ejecutar código modificado por Claude

---

## 📋 Comandos de Referencia Rápida

### Proyecto:
```bash
# Crear y navegar a proyecto
mkdir -p ~/proyectos/nombre-proyecto
cd ~/proyectos/nombre-proyecto

# Inicializar git
git init
git add .
git commit -m "Initial commit"

# Iniciar Claude
claude
```

### Dentro de Claude:
```
# Ayuda
help

# Leer archivos
Lee el archivo <nombre>
Muéstrame <archivo>

# Modificar código
Mejora el archivo <nombre> añadiendo <características>
Refactoriza <archivo>

# Crear archivos
Crea un archivo <nombre> con <descripción>

# Información
¿Qué archivos hay en el proyecto?
Lista todos los archivos .py

# Salir
exit
quit
```

### Git (fuera de Claude):
```bash
# Ver estado
git status

# Añadir cambios
git add .

# Commit
git commit -m "mensaje"

# Ver historial
git log --oneline
```

---

## 🎓 Conceptos Clave Aprendidos

- ✅ Cómo estructurar un proyecto para trabajar con Claude Code
- ✅ Inicializar control de versiones con Git
- ✅ Iniciar y gestionar sesiones de Claude Code
- ✅ Comandos básicos para interactuar con Claude
- ✅ Cómo Claude lee, modifica y crea archivos
- ✅ Limitaciones y capacidades de Claude Code
- ✅ Flujo de trabajo típico de desarrollo con Claude
- ✅ Mejores prácticas de comunicación con Claude

---

## ➡️ Próximo Paso

¡Perfecto! Ahora sabes cómo iniciar y trabajar con proyectos en Claude Code. Es momento de aplicar todo esto en un proyecto práctico real.

**[Continuar al Módulo 4: Proyecto Práctico - Todo List →](./modulo-4-proyecto-practico.md)**

---

## 📚 Recursos Adicionales

- [Git Documentation](https://git-scm.com/doc)
- [Python Project Structure Best Practices](https://docs.python-guide.org/writing/structure/)
- [Claude Code Advanced Features](https://docs.claude.com/en/docs/claude-code)

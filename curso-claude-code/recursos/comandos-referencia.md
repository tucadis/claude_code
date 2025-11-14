# Referencia Rápida de Comandos

Esta es una guía de referencia rápida de todos los comandos importantes del curso.

## WSL - Windows Subsystem for Linux

### Instalación y Gestión

```powershell
# Instalar WSL con Ubuntu
wsl --install

# Ver versión de WSL
wsl --version

# Listar distribuciones instaladas
wsl --list --verbose

# Iniciar WSL
wsl

# Iniciar distribución específica
wsl -d Ubuntu

# Detener WSL
wsl --shutdown

# Actualizar WSL
wsl --update

# Establecer distribución predeterminada
wsl --set-default Ubuntu

# Convertir a WSL 2
wsl --set-version Ubuntu 2
```

### Navegación de Archivos WSL ↔ Windows

```bash
# Desde WSL: Acceder a archivos de Windows
cd /mnt/c/Users/TuUsuario/

# Desde Windows: Acceder a archivos de WSL
\\wsl$\Ubuntu\home\tucadis\
```

---

## Linux/Ubuntu - Comandos Básicos

### Sistema

```bash
# Actualizar lista de paquetes
sudo apt update

# Actualizar paquetes instalados
sudo apt upgrade -y

# Instalar paquete
sudo apt install nombre-paquete -y

# Ver versión de Ubuntu
lsb_release -a

# Ver información del sistema
uname -a

# Ver directorio actual
pwd

# Listar archivos
ls -la

# Salir de terminal
exit
```

### Navegación

```bash
# Ir al directorio home
cd ~
cd $HOME

# Ir al directorio anterior
cd -

# Ir a un directorio específico
cd /ruta/al/directorio

# Crear directorio
mkdir nombre-directorio

# Crear directorios anidados
mkdir -p ruta/completa/al/directorio

# Eliminar directorio vacío
rmdir nombre-directorio

# Eliminar directorio con contenido
rm -rf nombre-directorio
```

### Archivos

```bash
# Crear archivo vacío
touch archivo.txt

# Ver contenido de archivo
cat archivo.txt

# Editar archivo con nano
nano archivo.txt

# Copiar archivo
cp origen.txt destino.txt

# Mover/renombrar archivo
mv origen.txt destino.txt

# Eliminar archivo
rm archivo.txt
```

---

## Node.js y npm

### Instalación con NVM

```bash
# Instalar NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Cargar NVM
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Verificar NVM
nvm --version

# Instalar Node.js LTS
nvm install --lts

# Usar versión LTS
nvm use --lts

# Listar versiones instaladas
nvm list

# Ver versión actual de Node
node --version

# Ver versión de npm
npm --version
```

### npm - Gestión de Paquetes

```bash
# Instalar paquete globalmente
npm install -g nombre-paquete

# Instalar paquete localmente
npm install nombre-paquete

# Instalar dependencias de desarrollo
npm install --save-dev nombre-paquete

# Instalar desde package.json
npm install

# Actualizar paquete
npm update nombre-paquete

# Desinstalar paquete
npm uninstall nombre-paquete

# Listar paquetes instalados
npm list

# Listar paquetes globales
npm list -g --depth=0

# Limpiar caché
npm cache clean --force
```

---

## Claude Code

### Instalación

```bash
# Instalar Claude Code
npm install -g @anthropic-ai/claude-code

# Verificar instalación
claude --version

# Ver ayuda
claude --help
```

### Configuración

```bash
# Configurar API Key (variable de entorno)
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-..."' >> ~/.bashrc
source ~/.bashrc

# Verificar API Key
echo $ANTHROPIC_API_KEY

# Configurar con comando
claude config set apiKey tu-api-key

# Ver configuración
claude config list

# Configurar modelo
claude config set model claude-3-5-sonnet-20241022
```

### Uso

```bash
# Iniciar Claude Code (directorio actual)
claude

# Chat de una línea
claude chat --message "tu pregunta"

# Usar modelo específico
claude --model claude-3-opus-20240229

# Modo verbose
claude --verbose
```

### Dentro de Claude Code

```
# Ver ayuda
help

# Leer archivo
Lee el archivo nombre.txt
Muéstrame src/main.py

# Crear archivo
Crea un archivo main.py con...

# Modificar código
Mejora la función X en archivo.py

# Buscar
Busca "función" en todos los archivos

# Listar archivos
¿Qué archivos hay en src/?

# Salir
exit
quit
Ctrl+C (dos veces)
```

---

## Git - Control de Versiones

### Configuración Inicial

```bash
# Instalar Git
sudo apt install git -y

# Configurar nombre
git config --global user.name "Tu Nombre"

# Configurar email
git config --global user.email "tu@email.com"

# Configurar editor
git config --global core.editor nano

# Ver configuración
git config --list
```

### Comandos Básicos

```bash
# Inicializar repositorio
git init

# Ver estado
git status

# Añadir archivos al staging
git add archivo.txt
git add .                    # Todos los archivos

# Hacer commit
git commit -m "mensaje del commit"

# Ver historial
git log
git log --oneline
git log --graph --all

# Ver diferencias
git diff
git diff archivo.txt

# Ver archivos en staging
git diff --staged
```

### Ramas (Branches)

```bash
# Ver ramas
git branch

# Crear rama
git branch nombre-rama

# Cambiar a rama
git checkout nombre-rama

# Crear y cambiar a rama
git checkout -b nombre-rama

# Fusionar rama
git merge nombre-rama

# Eliminar rama
git branch -d nombre-rama
```

### Repositorios Remotos

```bash
# Ver remotos
git remote -v

# Añadir remoto
git remote add origin https://github.com/usuario/repo.git

# Clonar repositorio
git clone https://github.com/usuario/repo.git

# Push
git push origin main
git push -u origin main      # Primera vez

# Pull
git pull origin main

# Fetch
git fetch origin
```

---

## Python - Desarrollo

### Entornos Virtuales

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Desactivar entorno virtual
deactivate

# Verificar Python en uso
which python
python --version
```

### pip - Gestión de Paquetes

```bash
# Instalar paquete
pip install nombre-paquete

# Instalar versión específica
pip install paquete==1.2.3

# Instalar desde requirements.txt
pip install -r requirements.txt

# Actualizar paquete
pip install --upgrade paquete

# Desinstalar paquete
pip uninstall paquete

# Listar paquetes instalados
pip list

# Crear requirements.txt
pip freeze > requirements.txt

# Ver información de paquete
pip show paquete
```

### Ejecución

```bash
# Ejecutar script
python script.py
python3 script.py

# Ejecutar módulo
python -m modulo

# Modo interactivo
python
python3

# Ejecutar con argumentos
python script.py arg1 arg2
```

---

## pytest - Testing

### Instalación

```bash
# Instalar pytest
pip install pytest pytest-cov
```

### Ejecución

```bash
# Ejecutar todos los tests
pytest

# Ejecutar con verbose
pytest -v

# Ejecutar archivo específico
pytest tests/test_file.py

# Ejecutar test específico
pytest tests/test_file.py::test_function

# Ejecutar con cobertura
pytest --cov=src

# Generar reporte HTML de cobertura
pytest --cov=src --cov-report=html

# Ver solo tests fallidos
pytest --lf

# Detener en primer fallo
pytest -x

# Modo verbose con salida
pytest -v -s
```

---

## Proyecto Todo List - Comandos Específicos

### Setup

```bash
# Ir al proyecto
cd ~/proyectos/todo-list-app

# Crear entorno virtual
python3 -m venv venv

# Activar entorno
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Uso de la Aplicación

```bash
# Añadir tarea
python -m src.cli add "Título de la tarea"
python -m src.cli add "Título" -d "Descripción"

# Listar todas las tareas
python -m src.cli list

# Listar pendientes
python -m src.cli list -f pending

# Listar completadas
python -m src.cli list -f completed

# Completar tarea
python -m src.cli complete 1

# Eliminar tarea (con confirmación)
python -m src.cli delete 1

# Eliminar sin confirmación
python -m src.cli delete 1 -y
```

### Testing

```bash
# Ejecutar todos los tests
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=src --cov-report=html
```

---

## Atajos y Aliases Útiles

### Añadir a ~/.bashrc

```bash
# Editar bashrc
nano ~/.bashrc

# Añadir al final:
alias ll='ls -la'
alias cdp='cd ~/proyectos'
alias py='python3'
alias pyt='pytest -v'
alias venv='source venv/bin/activate'
alias gs='git status'
alias ga='git add .'
alias gc='git commit -m'
alias gp='git push'
alias gl='git log --oneline'

# Recargar bashrc
source ~/.bashrc
```

---

## Solución de Problemas Comunes

### WSL

```bash
# Reiniciar WSL
wsl --shutdown
wsl

# Verificar versión
wsl --list --verbose

# Reparar red
sudo rm /etc/resolv.conf
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
```

### Claude Code

```bash
# Verificar API Key
echo $ANTHROPIC_API_KEY

# Reinstalar
npm uninstall -g @anthropic-ai/claude-code
npm install -g @anthropic-ai/claude-code

# Limpiar caché npm
npm cache clean --force
```

### Python

```bash
# Verificar versión
python3 --version

# Reinstalar pip
python3 -m pip install --upgrade pip

# Limpiar __pycache__
find . -type d -name "__pycache__" -exec rm -rf {} +
```

### Git

```bash
# Deshacer último commit (mantener cambios)
git reset --soft HEAD~1

# Descartar cambios locales
git checkout -- archivo.txt

# Limpiar archivos no tracked
git clean -fd
```

---

## Variables de Entorno Importantes

```bash
# Ver variable
echo $VARIABLE_NAME

# Establecer temporalmente
export VARIABLE_NAME="valor"

# Establecer permanentemente
echo 'export VARIABLE_NAME="valor"' >> ~/.bashrc
source ~/.bashrc

# Variables comunes
echo $HOME              # Directorio home
echo $USER              # Usuario actual
echo $PATH              # Rutas de búsqueda
echo $PWD               # Directorio actual
echo $SHELL             # Shell en uso
```

---

## Teclado - Atajos Útiles

### Terminal

- `Ctrl + C`: Interrumpir comando
- `Ctrl + D`: Salir / EOF
- `Ctrl + L`: Limpiar pantalla
- `Ctrl + A`: Ir al inicio de línea
- `Ctrl + E`: Ir al final de línea
- `Ctrl + U`: Borrar línea
- `Ctrl + K`: Borrar desde cursor al final
- `Ctrl + R`: Buscar en historial
- `↑` / `↓`: Navegar historial

### Nano

- `Ctrl + O`: Guardar
- `Ctrl + X`: Salir
- `Ctrl + K`: Cortar línea
- `Ctrl + U`: Pegar
- `Ctrl + W`: Buscar

---

Esta guía de referencia rápida cubre los comandos más importantes del curso.
Guárdala para consulta rápida durante tu desarrollo.

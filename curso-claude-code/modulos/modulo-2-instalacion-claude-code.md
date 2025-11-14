# Módulo 2: Instalación de Claude Code

## 📖 Introducción

Claude Code es una herramienta de línea de comandos (CLI) que te permite interactuar con Claude, el asistente de IA de Anthropic, directamente desde tu terminal. Esta herramienta es especialmente útil para desarrolladores, ya que puede leer, escribir y modificar archivos de código con el contexto completo de tu proyecto.

### ¿Qué puedes hacer con Claude Code?

- **Desarrollo asistido por IA**: Obtén ayuda para escribir código
- **Refactorización**: Mejora código existente
- **Debugging**: Encuentra y corrige errores
- **Documentación**: Genera documentación automáticamente
- **Aprendizaje**: Entiende código complejo con explicaciones
- **Operaciones Git**: Commits, pull requests y más

---

## 🔍 Paso 1: Verificación de Requisitos Previos

### 1.1 Verificar que estás en WSL

Asegúrate de estar en tu terminal de Ubuntu (WSL):

```bash
# Verificar que estás en Linux
uname -s
```

**Salida esperada:**
```
Linux
```

Si ves `Linux`, estás en el lugar correcto. Si no, abre Ubuntu desde el menú de Windows.

### 1.2 Verificar conexión a Internet

```bash
# Probar conexión
ping -c 4 google.com
```

**Salida esperada:**
```
PING google.com (142.250.185.46) 56(84) bytes of data.
64 bytes from lga34s34-in-f14.1e100.net (142.250.185.46): icmp_seq=1 ttl=117 time=12.4 ms
64 bytes from lga34s34-in-f14.1e100.net (142.250.185.46): icmp_seq=2 ttl=117 time=11.8 ms
...
--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
```

---

## 📦 Paso 2: Instalación de Node.js y npm

Claude Code requiere Node.js para funcionar. Vamos a instalarlo usando `nvm` (Node Version Manager), que es la forma recomendada.

### 2.1 Instalar NVM (Node Version Manager)

```bash
# Descargar e instalar NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

**Salida esperada:**
```
=> Downloading nvm from git to '/home/tucadis/.nvm'
=> Cloning into '/home/tucadis/.nvm'...
remote: Enumerating objects: 365, done.
remote: Counting objects: 100% (365/365), done.
...
=> Close and reopen your terminal to start using nvm or run the following to use it now:

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

### 2.2 Cargar NVM en la sesión actual

```bash
# Cargar NVM sin reiniciar la terminal
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

**Verificar instalación de NVM:**

```bash
# Verificar que NVM está instalado
nvm --version
```

**Salida esperada:**
```
0.39.7
```

### 2.3 Instalar Node.js

```bash
# Instalar la última versión LTS (Long Term Support) de Node.js
nvm install --lts
```

**Salida esperada:**
```
Installing latest LTS version.
Downloading and installing node v20.11.0...
Downloading https://nodejs.org/dist/v20.11.0/node-v20.11.0-linux-x64.tar.xz...
############################################################################ 100.0%
Computing checksum with sha256sum
Checksums matched!
Now using node v20.11.0 (npm v10.2.4)
Creating default alias: default -> lts/* (-> v20.11.0)
```

### 2.4 Verificar instalación de Node.js y npm

```bash
# Verificar versión de Node.js
node --version
```

**Salida esperada:**
```
v20.11.0
```

```bash
# Verificar versión de npm
npm --version
```

**Salida esperada:**
```
10.2.4
```

### 2.5 Configurar npm (opcional pero recomendado)

```bash
# Configurar directorio global de npm para evitar problemas de permisos
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'

# Añadir al PATH
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

**¿Por qué hacer esto?**
Evita tener que usar `sudo` para instalar paquetes globales de npm.

---

## 🎯 Paso 3: Obtener API Key de Anthropic

Para usar Claude Code, necesitas una API Key de Anthropic.

### 3.1 Crear una cuenta en Anthropic

1. **Visita**: https://console.anthropic.com/
2. **Haz clic** en "Sign Up" o "Get Started"
3. **Completa el registro** con tu email
4. **Verifica tu email**

### 3.2 Obtener tu API Key

1. **Inicia sesión** en https://console.anthropic.com/
2. **Ve a Settings** (Configuración) o busca "API Keys"
3. **Haz clic** en "Create Key" o "Get API Key"
4. **Copia la API Key** (se ve algo como: `sk-ant-api03-...`)

**⚠️ IMPORTANTE:**
- Guarda tu API Key en un lugar seguro
- No la compartas públicamente
- No la subas a repositorios de Git
- Esta clave solo se muestra una vez

### 3.3 Entender los límites del plan gratuito

Anthropic ofrece créditos gratuitos para probar:

- **Créditos iniciales**: $5 USD en créditos
- **Caducidad**: Los créditos pueden tener fecha de expiración
- **Uso**: Suficiente para aprender y proyectos pequeños
- **Upgrade**: Puedes añadir tarjeta de crédito para uso continuo

**Ver tu uso actual:**
1. Ve a https://console.anthropic.com/
2. Busca "Usage" o "Billing"
3. Revisa tus créditos restantes

---

## 💻 Paso 4: Instalación de Claude Code

### 4.1 Instalar Claude Code globalmente

```bash
# Instalar Claude Code desde npm
npm install -g @anthropic-ai/claude-code
```

**Salida esperada:**
```
added 180 packages in 15s

24 packages are looking for funding
  run `npm fund` for details
```

**Explicación del comando:**
- `npm install`: Comando para instalar paquetes
- `-g`: Flag para instalar globalmente (disponible en todo el sistema)
- `@anthropic-ai/claude-code`: Nombre del paquete

### 4.2 Verificar instalación

```bash
# Verificar que Claude Code está instalado
claude --version
```

**Salida esperada:**
```
@anthropic-ai/claude-code/1.x.x
```

```bash
# Ver ayuda de Claude Code
claude --help
```

**Salida esperada:**
```
Claude Code - AI-powered coding assistant

Usage: claude [options] [command]

Options:
  -V, --version              output the version number
  -h, --help                 display help for command

Commands:
  chat                       Start an interactive chat session
  config                     Manage configuration
  help [command]             display help for command
```

---

## 🔐 Paso 5: Configurar la API Key

### 5.1 Configurar la API Key de forma segura

**Método 1: Variable de entorno (Recomendado)**

```bash
# Añadir API Key al archivo .bashrc
echo 'export ANTHROPIC_API_KEY="tu-api-key-aqui"' >> ~/.bashrc
source ~/.bashrc
```

**Reemplaza `tu-api-key-aqui` con tu API Key real.**

**Ejemplo:**
```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-abc123..."' >> ~/.bashrc
source ~/.bashrc
```

**Verificar que se configuró correctamente:**

```bash
# Verificar variable de entorno (muestra solo parte de la clave por seguridad)
echo ${ANTHROPIC_API_KEY:0:20}...
```

**Salida esperada:**
```
sk-ant-api03-abc123...
```

**Método 2: Archivo .env en el proyecto (Alternativa)**

Para proyectos específicos:

```bash
# Crear archivo .env en tu directorio de proyecto
echo 'ANTHROPIC_API_KEY=tu-api-key-aqui' > .env

# Asegurarse de que .env está en .gitignore
echo '.env' >> .gitignore
```

**Método 3: Configuración de Claude Code (Alternativa)**

```bash
# Configurar mediante el comando de Claude Code
claude config set apiKey tu-api-key-aqui
```

### 5.2 Verificar configuración

```bash
# Probar que Claude Code puede conectarse
claude chat --message "Hola, ¿funciona la conexión?"
```

**Si funciona, verás una respuesta de Claude:**
```
Claude: Sí, la conexión funciona perfectamente. ¿En qué puedo ayudarte hoy?
```

---

## ✅ Paso 6: Verificación Completa de la Instalación

### 6.1 Test de funcionalidad básica

```bash
# Crear directorio de prueba
mkdir -p ~/claude-test
cd ~/claude-test

# Crear archivo de prueba
echo "console.log('Hello, Claude!');" > test.js

# Iniciar Claude Code
claude
```

**Dentro de Claude Code, escribe:**
```
Lee el archivo test.js y explícame qué hace
```

**Respuesta esperada:**
Claude debería leer el archivo y explicarte que es un script simple de JavaScript que imprime "Hello, Claude!" en la consola.

### 6.2 Verificar herramientas instaladas - Checklist

```bash
# Verificar todas las herramientas
echo "=== Verificación de instalación ==="
echo "1. Node.js: $(node --version)"
echo "2. npm: $(npm --version)"
echo "3. Claude Code: $(claude --version)"
echo "4. API Key configurada: ${ANTHROPIC_API_KEY:+Sí}"
echo "=== Verificación completa ==="
```

**Salida esperada:**
```
=== Verificación de instalación ===
1. Node.js: v20.11.0
2. npm: 10.2.4
3. Claude Code: @anthropic-ai/claude-code/1.x.x
4. API Key configurada: Sí
=== Verificación completa ===
```

---

## 🎨 Paso 7: Personalización Inicial (Opcional)

### 7.1 Configurar el modelo de Claude

Claude Code puede usar diferentes modelos. El predeterminado es bueno, pero puedes cambiarlo:

```bash
# Ver configuración actual
claude config list
```

```bash
# Configurar modelo específico (opcional)
claude config set model claude-3-5-sonnet-20241022
```

**Modelos disponibles:**
- `claude-3-5-sonnet-20241022`: Balance entre velocidad y capacidad (recomendado)
- `claude-3-opus-20240229`: Más potente pero más lento y costoso
- `claude-3-haiku-20240307`: Más rápido y económico

### 7.2 Configurar preferencias de color y tema

```bash
# Habilitar colores en la terminal
claude config set colorize true

# Configurar estilo de salida
claude config set format pretty
```

### 7.3 Ver toda la configuración

```bash
# Ver archivo de configuración
cat ~/.config/claude-code/config.json
```

**Salida esperada:**
```json
{
  "apiKey": "sk-ant-api03-...",
  "model": "claude-3-5-sonnet-20241022",
  "colorize": true,
  "format": "pretty"
}
```

---

## 🚀 Paso 8: Primeros Comandos

### 8.1 Comando básico de chat

```bash
# Chat simple de una línea
claude chat --message "Hola Claude, preséntate"
```

### 8.2 Iniciar sesión interactiva

```bash
# Iniciar sesión interactiva
claude
```

**Comandos dentro de la sesión:**
- `help`: Ver comandos disponibles
- `exit` o `quit`: Salir
- `clear`: Limpiar pantalla
- `/read <archivo>`: Leer un archivo
- `/write <archivo>`: Escribir un archivo

### 8.3 Trabajar con archivos

```bash
# Crear un archivo de ejemplo
echo "def saludar(nombre):
    return f'Hola, {nombre}!'" > saludar.py

# Iniciar Claude Code
claude
```

**Dentro de Claude, prueba:**
```
Lee el archivo saludar.py y mejóralo añadiendo documentación y type hints
```

---

## 🐛 Solución de Problemas Comunes

### Problema 1: "claude: command not found"

**Causa:** El PATH no incluye el directorio de instalación global de npm.

**Solución:**
```bash
# Verificar dónde está instalado
npm list -g @anthropic-ai/claude-code

# Añadir al PATH
echo 'export PATH="$PATH:$(npm config get prefix)/bin"' >> ~/.bashrc
source ~/.bashrc
```

### Problema 2: "API key not found"

**Causa:** La API Key no está configurada o no se carga correctamente.

**Solución:**
```bash
# Verificar variable de entorno
echo $ANTHROPIC_API_KEY

# Si está vacía, configurar de nuevo
echo 'export ANTHROPIC_API_KEY="tu-api-key-aqui"' >> ~/.bashrc
source ~/.bashrc

# O configurar con el comando
claude config set apiKey tu-api-key-aqui
```

### Problema 3: "Permission denied" al instalar

**Causa:** Problemas de permisos con npm.

**Solución:**
```bash
# Configurar directorio global de npm
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

# Reinstalar Claude Code
npm install -g @anthropic-ai/claude-code
```

### Problema 4: "Error: connect ECONNREFUSED"

**Causa:** Problema de conexión a Internet o proxy.

**Solución:**
```bash
# Verificar conexión
ping -c 4 api.anthropic.com

# Si usas proxy, configurarlo
export HTTP_PROXY=http://tu-proxy:puerto
export HTTPS_PROXY=http://tu-proxy:puerto
```

### Problema 5: Versión antigua de Node.js

**Causa:** Node.js muy antiguo.

**Solución:**
```bash
# Actualizar a la última LTS
nvm install --lts
nvm use --lts

# Verificar
node --version
```

### Problema 6: "Rate limit exceeded"

**Causa:** Has alcanzado el límite de solicitudes de la API.

**Solución:**
- Espera unos minutos antes de hacer más solicitudes
- Revisa tu uso en https://console.anthropic.com/
- Considera añadir créditos o una tarjeta de crédito

---

## 📊 Entender el uso de la API

### Monitorear créditos

```bash
# Crear script para verificar uso (opcional)
cat > ~/check-usage.sh << 'EOF'
#!/bin/bash
echo "Para ver tu uso de API, visita:"
echo "https://console.anthropic.com/settings/usage"
echo ""
echo "Tu API Key actual: ${ANTHROPIC_API_KEY:0:20}..."
EOF

chmod +x ~/check-usage.sh

# Ejecutar
~/check-usage.sh
```

### Costos aproximados

- **Claude 3.5 Sonnet**: ~$3 por millón de tokens de entrada
- **Conversación típica**: 0.01 - 0.05 USD
- **Créditos iniciales**: Suficiente para ~100-500 interacciones

---

## ✅ Checklist de Verificación Final

Antes de pasar al siguiente módulo, asegúrate de que:

- [ ] Node.js está instalado (v18 o superior)
- [ ] npm está instalado y funciona
- [ ] Claude Code está instalado globalmente
- [ ] Puedes ejecutar `claude --version`
- [ ] Tienes una cuenta de Anthropic
- [ ] Has obtenido tu API Key
- [ ] La API Key está configurada (variable de entorno)
- [ ] Puedes ejecutar `claude chat --message "test"` y recibir respuesta
- [ ] Has probado leer un archivo con Claude Code

---

## 📝 Comandos de Referencia Rápida

### Instalación:
```bash
# Instalar NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Instalar Node.js
nvm install --lts

# Instalar Claude Code
npm install -g @anthropic-ai/claude-code

# Configurar API Key
echo 'export ANTHROPIC_API_KEY="tu-api-key"' >> ~/.bashrc
source ~/.bashrc
```

### Uso básico:
```bash
# Verificar instalación
claude --version

# Chat simple
claude chat --message "tu mensaje"

# Sesión interactiva
claude

# Ver configuración
claude config list

# Configurar opciones
claude config set <opcion> <valor>
```

### Verificación:
```bash
# Verificar todo
node --version && npm --version && claude --version
echo "API Key: ${ANTHROPIC_API_KEY:0:20}..."
```

---

## 🎓 Conceptos Clave Aprendidos

- ✅ Cómo instalar Node.js usando NVM
- ✅ Cómo instalar paquetes npm globalmente
- ✅ Cómo obtener una API Key de Anthropic
- ✅ Cómo instalar Claude Code
- ✅ Cómo configurar variables de entorno de forma segura
- ✅ Comandos básicos de Claude Code
- ✅ Resolución de problemas comunes de instalación

---

## ➡️ Próximo Paso

¡Excelente! Ahora tienes Claude Code instalado y configurado. Es hora de crear tu primer proyecto.

**[Continuar al Módulo 3: Inicio de un Proyecto →](./modulo-3-inicio-proyecto.md)**

---

## 📚 Recursos Adicionales

- [Documentación de Claude Code](https://docs.claude.com/en/docs/claude-code)
- [Documentación de la API de Anthropic](https://docs.anthropic.com/)
- [Node.js Documentation](https://nodejs.org/docs/)
- [npm Documentation](https://docs.npmjs.com/)
- [NVM GitHub Repository](https://github.com/nvm-sh/nvm)

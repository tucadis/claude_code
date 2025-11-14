# Módulo 1: Instalación de WSL en Windows

## 📖 Introducción

WSL (Windows Subsystem for Linux) permite ejecutar un entorno Linux directamente en Windows sin necesidad de una máquina virtual tradicional. Esto es esencial para trabajar con Claude Code, ya que proporciona un entorno de desarrollo más potente y compatible con herramientas de desarrollo modernas.

### ¿Por qué necesitamos WSL?

- **Compatibilidad**: Muchas herramientas de desarrollo están optimizadas para Linux
- **Rendimiento**: WSL 2 ofrece excelente rendimiento con virtualización ligera
- **Integración**: Acceso completo al sistema de archivos de Windows
- **Desarrollo moderno**: Acceso a herramientas CLI estándar de la industria

### Diferencias entre WSL 1 y WSL 2

| Característica | WSL 1 | WSL 2 |
|----------------|-------|-------|
| Kernel | Traducción de llamadas | Kernel Linux real |
| Rendimiento I/O | Más rápido en archivos Windows | Más rápido en archivos Linux |
| Compatibilidad | Limitada | Completa |
| Recomendado para | Casos legacy | Desarrollo moderno |

**Para este curso usaremos WSL 2.**

---

## 🔍 Paso 1: Verificación de Requisitos Previos

### Requisitos del Sistema

- Windows 10 versión 2004 o superior (Build 19041 o superior)
- Windows 11 (cualquier versión)
- Arquitectura: x64 o ARM64

### Verificar la versión de Windows

1. Presiona `Win + R` para abrir el cuadro de diálogo "Ejecutar"
2. Escribe `winver` y presiona Enter
3. Verifica que tu versión cumple con los requisitos

**Desde PowerShell (alternativa):**

```powershell
# Verificar versión de Windows
[System.Environment]::OSVersion.Version
```

**Salida esperada:**
```
Major  Minor  Build  Revision
-----  -----  -----  --------
10     0      19045  0         # Build debe ser >= 19041
```

### Verificar si tu sistema es de 64 bits

```powershell
# Verificar arquitectura del sistema
(Get-WmiObject Win32_OperatingSystem).OSArchitecture
```

**Salida esperada:**
```
64-bit
```

---

## 🚀 Paso 2: Instalación de WSL (Método Simplificado - Recomendado)

Microsoft ha simplificado la instalación de WSL. Este es el método más fácil y recomendado.

### 2.1 Abrir PowerShell como Administrador

1. Presiona la tecla `Win`
2. Escribe "PowerShell"
3. Haz clic derecho en "Windows PowerShell"
4. Selecciona "Ejecutar como administrador"
5. Acepta el control de cuentas de usuario (UAC)

### 2.2 Ejecutar el comando de instalación

```powershell
# Instalar WSL con Ubuntu (distribución predeterminada)
wsl --install
```

**Este comando hace lo siguiente:**
- Habilita las características necesarias de Windows
- Descarga e instala el kernel de Linux más reciente
- Instala WSL 2 como predeterminado
- Descarga e instala Ubuntu (distribución predeterminada)

**Salida esperada:**
```
Instalando: Plataforma de máquina virtual
Instalando: Plataforma del Subsistema de Windows para Linux
Descargando: WSL Kernel
Instalando: WSL Kernel
Descargando: Ubuntu
La operación solicitada se realizó correctamente. Los cambios se aplicarán después de reiniciar el sistema.
```

### 2.3 Reiniciar el sistema

```powershell
# Reiniciar Windows (guarda tu trabajo primero)
Restart-Computer
```

O reinicia manualmente: `Inicio > Apagar > Reiniciar`

---

## 🔧 Paso 3: Configuración Inicial de Ubuntu

Después del reinicio, Ubuntu se iniciará automáticamente.

### 3.1 Configurar Usuario y Contraseña

Cuando Ubuntu se inicie por primera vez, verás:

```
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username:
```

**Pasos:**

1. **Introduce un nombre de usuario** (solo minúsculas, sin espacios)
   ```
   Enter new UNIX username: tucadis
   ```

2. **Introduce una contraseña** (no se mostrará mientras escribes)
   ```
   New password: ********
   Retype new password: ********
   ```

3. **Confirmación exitosa:**
   ```
   passwd: password updated successfully
   Installation successful!
   ```

### 3.2 Actualizar el Sistema

Una vez dentro de Ubuntu, ejecuta:

```bash
# Actualizar lista de paquetes
sudo apt update
```

**Salida esperada:**
```
[sudo] password for tucadis:
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
...
Reading package lists... Done
Building dependency tree... Done
All packages are up to date.
```

```bash
# Actualizar paquetes instalados
sudo apt upgrade -y
```

**Parámetros:**
- `sudo`: Ejecuta el comando con privilegios de administrador
- `apt`: Gestor de paquetes de Ubuntu
- `update`: Actualiza la lista de paquetes disponibles
- `upgrade`: Actualiza los paquetes instalados
- `-y`: Confirma automáticamente (sin preguntar)

**Proceso esperado:**
```
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
...
Do you want to continue? [Y/n]
(se salta porque usamos -y)
```

---

## 🎯 Paso 4: Verificación de la Instalación

### 4.1 Verificar versión de WSL

Desde PowerShell (como administrador):

```powershell
# Ver versión de WSL
wsl --version
```

**Salida esperada:**
```
WSL version: 2.0.9.0
Kernel version: 5.15.133.1-1
WSLg version: 1.0.59
MSRDC version: 1.2.4677
Direct3D version: 1.611.1-81528511
DXCore version: 10.0.25131.1002-220531-1700.rs-onecore-base2-hyp
Windows version: 10.0.19045.3693
```

### 4.2 Listar distribuciones instaladas

```powershell
# Ver distribuciones instaladas y sus versiones de WSL
wsl --list --verbose
```

**Salida esperada:**
```
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

**Explicación:**
- `*`: Distribución predeterminada
- `NAME`: Nombre de la distribución
- `STATE`: Running (en ejecución) o Stopped (detenida)
- `VERSION`: 2 significa WSL 2 (lo que queremos)

### 4.3 Verificar desde dentro de Ubuntu

```bash
# Ver información del sistema
uname -a
```

**Salida esperada:**
```
Linux DESKTOP-XXXXX 5.15.133.1-microsoft-standard-WSL2 #1 SMP Thu Oct 5 21:02:42 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
```

```bash
# Ver versión de Ubuntu
lsb_release -a
```

**Salida esperada:**
```
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.3 LTS
Release:        22.04
Codename:       jammy
```

---

## 🛠️ Paso 5: Instalación Manual (Alternativa)

Si el método simplificado no funciona, usa este método:

### 5.1 Habilitar WSL y Virtual Machine Platform

Desde PowerShell como administrador:

```powershell
# Habilitar característica WSL
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

```powershell
# Habilitar característica de Plataforma de Máquina Virtual
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

**Salida esperada para cada comando:**
```
Deployment Image Servicing and Management tool
Version: 10.0.19041.844

Image Version: 10.0.19045.3693

Enabling feature(s)
[==========================100.0%==========================]
The operation completed successfully.
```

### 5.2 Reiniciar Windows

```powershell
Restart-Computer
```

### 5.3 Descargar e instalar el kernel de WSL 2

**Opción A: Con PowerShell**

```powershell
# Descargar kernel de WSL 2
Invoke-WebRequest -Uri https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi -OutFile wsl_update_x64.msi

# Instalar kernel
msiexec /i wsl_update_x64.msi /quiet
```

**Opción B: Manual**
1. Descarga desde: https://aka.ms/wsl2kernel
2. Ejecuta el archivo `.msi` descargado
3. Sigue el asistente de instalación

### 5.4 Establecer WSL 2 como versión predeterminada

```powershell
# Configurar WSL 2 como predeterminado
wsl --set-default-version 2
```

**Salida esperada:**
```
For information on key differences with WSL 2 please visit https://aka.ms/wsl2
The operation completed successfully.
```

### 5.5 Instalar Ubuntu desde Microsoft Store

**Opción A: Con PowerShell**

```powershell
# Instalar Ubuntu
wsl --install -d Ubuntu
```

**Opción B: Microsoft Store**
1. Abre Microsoft Store
2. Busca "Ubuntu"
3. Selecciona "Ubuntu" (sin número de versión)
4. Haz clic en "Obtener" o "Instalar"
5. Espera a que se descargue e instale
6. Haz clic en "Abrir"

---

## ⚙️ Paso 6: Configuración Avanzada (Opcional)

### 6.1 Configurar WSL 2 para una distribución específica

Si tienes múltiples distribuciones y una usa WSL 1:

```powershell
# Convertir una distribución a WSL 2
wsl --set-version Ubuntu 2
```

### 6.2 Cambiar la distribución predeterminada

```powershell
# Ver distribuciones disponibles
wsl --list

# Establecer distribución predeterminada
wsl --set-default Ubuntu
```

### 6.3 Configurar recursos de WSL 2

Crea un archivo `.wslconfig` en tu carpeta de usuario de Windows:

**Ruta:** `C:\Users\TuUsuario\.wslconfig`

```powershell
# Crear archivo de configuración
@"
[wsl2]
memory=4GB
processors=2
swap=2GB
localhostForwarding=true
"@ | Out-File -FilePath $env:USERPROFILE\.wslconfig -Encoding ASCII
```

**Explicación de parámetros:**
- `memory`: RAM máxima para WSL (4GB en este ejemplo)
- `processors`: Número de procesadores virtuales (2 en este ejemplo)
- `swap`: Espacio de intercambio (2GB)
- `localhostForwarding`: Permite acceso a localhost desde Windows

**Aplicar cambios:**

```powershell
# Detener WSL
wsl --shutdown

# Iniciar de nuevo
wsl
```

### 6.4 Acceder a archivos de Windows desde WSL

Desde Ubuntu, los archivos de Windows están en `/mnt/`:

```bash
# Ir a tu carpeta de usuario de Windows
cd /mnt/c/Users/TuUsuario/

# Listar archivos
ls -la

# Ir al escritorio
cd /mnt/c/Users/TuUsuario/Desktop/
```

### 6.5 Acceder a archivos de WSL desde Windows

En el Explorador de Windows:

```
\\wsl$\Ubuntu\home\tucadis\
```

O desde línea de comandos de Windows:

```powershell
# Abrir explorador en el home de WSL
explorer.exe \\wsl$\Ubuntu\home\tucadis\
```

---

## 🐛 Solución de Problemas Comunes

### Problema 1: "WSL 2 requires an update to its kernel component"

**Solución:**
```powershell
# Actualizar el kernel de WSL
wsl --update
```

### Problema 2: La virtualización no está habilitada en BIOS

**Síntomas:**
```
Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS.
```

**Solución:**
1. Reinicia tu computadora
2. Entra a la BIOS (generalmente F2, F10, F12 o Del durante el inicio)
3. Busca opciones de virtualización:
   - Intel: "Intel VT-x" o "Intel Virtualization Technology"
   - AMD: "AMD-V" o "SVM Mode"
4. Habilita la opción
5. Guarda y sal de la BIOS

### Problema 3: Error 0x80070003

**Solución:**
Asegúrate de que WSL instale en la unidad C:

```powershell
# Ver dónde está instalado WSL
wsl --list --verbose
```

### Problema 4: "The requested operation requires elevation"

**Solución:**
Ejecuta PowerShell como administrador (haz clic derecho > Ejecutar como administrador)

### Problema 5: Ubuntu no inicia después de la instalación

**Solución:**
```powershell
# Reiniciar WSL
wsl --shutdown

# Iniciar Ubuntu específicamente
wsl -d Ubuntu
```

### Problema 6: Conexión de red no funciona en WSL

**Solución:**
```bash
# Desde Ubuntu, generar nuevo archivo resolv.conf
sudo rm /etc/resolv.conf
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
sudo bash -c 'echo "nameserver 8.8.4.4" >> /etc/resolv.conf'

# Probar conexión
ping -c 4 google.com
```

---

## ✅ Checklist de Verificación Final

Antes de pasar al siguiente módulo, asegúrate de que:

- [ ] WSL 2 está instalado correctamente
- [ ] Ubuntu está instalado y funciona
- [ ] Puedes ejecutar `wsl --version` y ver WSL 2
- [ ] Puedes ejecutar `wsl --list --verbose` y Ubuntu aparece con VERSION 2
- [ ] Has creado un usuario y contraseña en Ubuntu
- [ ] Has ejecutado `sudo apt update && sudo apt upgrade -y`
- [ ] Puedes acceder a archivos de Windows desde Ubuntu (`/mnt/c/`)
- [ ] El comando `uname -a` muestra que estás en Linux

---

## 📝 Comandos de Referencia Rápida

### Desde Windows PowerShell:

```powershell
# Ver versión de WSL
wsl --version

# Listar distribuciones
wsl --list --verbose

# Iniciar WSL (distribución predeterminada)
wsl

# Iniciar distribución específica
wsl -d Ubuntu

# Detener WSL
wsl --shutdown

# Actualizar WSL
wsl --update

# Establecer distribución predeterminada
wsl --set-default Ubuntu

# Convertir distribución a WSL 2
wsl --set-version Ubuntu 2
```

### Desde Ubuntu (WSL):

```bash
# Actualizar paquetes
sudo apt update && sudo apt upgrade -y

# Ver versión de Ubuntu
lsb_release -a

# Ver información del sistema
uname -a

# Acceder a archivos de Windows
cd /mnt/c/Users/TuUsuario/

# Salir de WSL
exit
```

---

## 🎓 Conceptos Clave Aprendidos

- ✅ Qué es WSL y por qué es útil para desarrollo
- ✅ Diferencia entre WSL 1 y WSL 2
- ✅ Cómo instalar WSL 2 en Windows
- ✅ Cómo configurar Ubuntu en WSL
- ✅ Cómo actualizar el sistema Linux
- ✅ Cómo acceder a archivos entre Windows y Linux
- ✅ Resolución de problemas comunes

---

## ➡️ Próximo Paso

¡Felicidades! Has completado la instalación de WSL. Ahora estás listo para instalar Claude Code.

**[Continuar al Módulo 2: Instalación de Claude Code →](./modulo-2-instalacion-claude-code.md)**

---

## 📚 Recursos Adicionales

- [Documentación oficial de WSL](https://docs.microsoft.com/en-us/windows/wsl/)
- [Comparación WSL 1 vs WSL 2](https://docs.microsoft.com/en-us/windows/wsl/compare-versions)
- [Mejores prácticas de WSL](https://docs.microsoft.com/en-us/windows/wsl/setup/environment)

# Módulo 5: Mejores Prácticas y Recursos

## 📖 Introducción

En este módulo final aprenderás cómo maximizar tu productividad con Claude Code, siguiendo mejores prácticas y conociendo recursos útiles para continuar tu aprendizaje.

---

## 💡 Mejores Prácticas para Interactuar con Claude

### 1. Sé Específico y Claro

**❌ Evita peticiones vagas:**
```
Mejora este código
```

**✅ Sé específico:**
```
Refactoriza la función calculate_total en src/utils.py para:
1. Añadir type hints
2. Manejar el caso de lista vacía
3. Añadir documentación
4. Usar list comprehension en lugar de bucle for
```

### 2. Proporciona Contexto

**❌ Sin contexto:**
```
Crea una función para validar emails
```

**✅ Con contexto:**
```
Estoy desarrollando un sistema de registro de usuarios.
Crea una función validate_email en src/validators.py que:
- Valide formato de email según RFC 5322
- Retorne True/False
- Incluya tests en tests/test_validators.py
- Use regex para la validación
```

### 3. Divide Tareas Grandes

**❌ Tarea muy amplia:**
```
Crea una aplicación web completa de e-commerce
```

**✅ Dividido en pasos:**
```
Paso 1: Crea el modelo de datos para Product con campos id, name, price, stock
Paso 2: Implementa CRUD básico para productos
Paso 3: Añade validación de datos
Paso 4: Crea tests unitarios
```

### 4. Especifica el Lenguaje y Estilo

```
Crea un servidor REST API en Python usando Flask con:
- Rutas para GET /api/users y POST /api/users
- Validación con Marshmallow
- Documentación con docstrings estilo Google
- Type hints
- Manejo de errores HTTP
```

### 5. Pide Explicaciones Cuando Sea Necesario

```
Explica cómo funciona la función recursive_search en src/utils.py
línea por línea, especialmente la parte de la recursión
```

---

## 🔄 Flujo de Trabajo Óptimo

### Flujo Recomendado

```
1. Planificación
   ↓
2. Desarrollo con Claude
   ↓
3. Revisión y Testing
   ↓
4. Iteración y Mejoras
   ↓
5. Documentación
   ↓
6. Commit
```

### 1. Planificación (Antes de Claude)

```bash
# Crear estructura básica
mkdir -p proyecto/{src,tests,docs}
cd proyecto

# Inicializar git
git init

# Crear archivo de planificación
cat > PLAN.md << 'EOF'
# Plan del Proyecto

## Objetivo
Crear una API REST para gestión de biblioteca

## Módulos
- [ ] Modelo de datos (Book, Author)
- [ ] CRUD operations
- [ ] API endpoints
- [ ] Tests
- [ ] Documentación

## Tecnologías
- FastAPI
- SQLAlchemy
- pytest
EOF

# Iniciar Claude
claude
```

### 2. Desarrollo con Claude

```
Lee PLAN.md y comencemos con el primer módulo:
crear el modelo de datos en src/models.py
```

### 3. Revisión y Testing

```bash
# Salir de Claude (Ctrl+C)
# Ejecutar el código
python src/models.py

# Ejecutar tests
pytest tests/ -v

# Si hay errores, volver a Claude
claude
```

```
Los tests fallan con el error: "AttributeError: 'Book' object has no attribute 'isbn'"
Lee tests/test_models.py y src/models.py y corrige el error
```

### 4. Iteración y Mejoras

```
El código funciona pero es lento con muchos registros.
Optimiza la función search_books para mejor rendimiento
```

### 5. Documentación

```
Genera documentación completa en docs/api.md para todos
los endpoints implementados en src/api.py
```

### 6. Commit

```bash
git add .
git commit -m "feat: implementar API REST con endpoints de libros"
```

---

## 🎯 Gestión de Contexto

### Entender las Limitaciones de Contexto

Claude tiene un límite de contexto. Para proyectos grandes:

**1. Trabaja por módulos:**
```
# Sesión 1: Modelos
claude
> Trabajemos solo en los modelos de datos...

# Sesión 2: API
claude
> Lee src/models.py para entender los modelos,
  ahora creemos la API en src/api.py...
```

**2. Usa archivos de referencia:**
```bash
# Crear archivo de referencia
cat > CONTEXT.md << 'EOF'
# Contexto del Proyecto

## Estructura
- src/models.py: Modelos Book, Author con SQLAlchemy
- src/api.py: Endpoints REST con FastAPI
- src/database.py: Configuración de BD

## Convenciones
- Usar async/await para endpoints
- Type hints obligatorios
- Docstrings estilo Google
EOF
```

```
Lee CONTEXT.md antes de continuar
```

**3. Resume sesiones largas:**
```
Resume todo lo que hemos hecho en esta sesión y
guárdalo en docs/session-2024-01-15.md
```

---

## 🚀 Comandos y Atajos Útiles

### Comandos para Claude Code

```bash
# Iniciar en directorio específico
cd /ruta/al/proyecto && claude

# Usar modelo específico
claude --model claude-3-opus-20240229

# Modo verbose para debugging
claude --verbose

# Especificar archivo de configuración
claude --config ~/.config/claude-code/custom-config.json
```

### Atajos de Terminal en WSL

```bash
# Navegar rápidamente
alias cdp='cd ~/proyectos'
alias cdc='cd ~/proyectos && claude'

# Git rápido
alias gs='git status'
alias ga='git add .'
alias gc='git commit -m'
alias gp='git push'

# Python
alias py='python3'
alias pyt='pytest -v'
alias pyc='pytest --cov=src'

# Activar entorno virtual
alias venv='source venv/bin/activate'

# Añadir a ~/.bashrc
echo "alias cdp='cd ~/proyectos'" >> ~/.bashrc
source ~/.bashrc
```

### Script de Inicio de Proyecto

```bash
# Crear script ~/bin/new-project.sh
mkdir -p ~/bin
cat > ~/bin/new-project.sh << 'EOF'
#!/bin/bash

if [ -z "$1" ]; then
    echo "Uso: new-project.sh nombre-proyecto"
    exit 1
fi

PROJECT_NAME=$1
PROJECT_DIR=~/proyectos/$PROJECT_NAME

echo "Creando proyecto: $PROJECT_NAME"

# Crear estructura
mkdir -p $PROJECT_DIR/{src,tests,docs,data}
cd $PROJECT_DIR

# Archivos base
touch README.md
touch src/__init__.py
touch tests/__init__.py
touch requirements.txt
touch .gitignore

# Git
git init

# .gitignore
cat > .gitignore << 'GITIGNORE'
__pycache__/
*.pyc
.env
venv/
*.log
GITIGNORE

# README
cat > README.md << README
# $PROJECT_NAME

Descripción del proyecto

## Instalación

\`\`\`bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

## Uso

TODO

## Tests

\`\`\`bash
pytest tests/ -v
\`\`\`
README

# Entorno virtual
python3 -m venv venv
source venv/bin/activate

echo "✓ Proyecto $PROJECT_NAME creado en $PROJECT_DIR"
echo "Ejecuta: cd $PROJECT_DIR && claude"
EOF

chmod +x ~/bin/new-project.sh

# Añadir al PATH
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Uso:**
```bash
new-project.sh mi-nuevo-proyecto
cd ~/proyectos/mi-nuevo-proyecto
claude
```

---

## 📊 Optimización de Costos y Uso de API

### Monitorear Uso

```bash
# Crear script para ver uso
cat > ~/bin/claude-usage.sh << 'EOF'
#!/bin/bash
echo "Para ver tu uso de API de Claude:"
echo "https://console.anthropic.com/settings/usage"
echo ""
echo "Tu API Key: ${ANTHROPIC_API_KEY:0:20}..."
echo ""
echo "Tips para reducir costos:"
echo "1. Sé específico en tus peticiones"
echo "2. Usa el modelo Haiku para tareas simples"
echo "3. Revisa código antes de pedir cambios grandes"
echo "4. Trabaja por módulos pequeños"
EOF

chmod +x ~/bin/claude-usage.sh
```

### Elegir el Modelo Correcto

**Claude 3 Haiku** (Más barato, más rápido)
```bash
claude --model claude-3-haiku-20240307
```
- ✅ Tareas simples
- ✅ Documentación
- ✅ Explicaciones de código
- ✅ Búsquedas y listados

**Claude 3.5 Sonnet** (Balance - Recomendado)
```bash
claude --model claude-3-5-sonnet-20241022
```
- ✅ Desarrollo general
- ✅ Refactorización
- ✅ Debugging
- ✅ Uso diario

**Claude 3 Opus** (Más potente, más caro)
```bash
claude --model claude-3-opus-20240229
```
- ✅ Código muy complejo
- ✅ Arquitectura de sistema
- ✅ Problemas difíciles
- ✅ Análisis profundo

---

## 🛡️ Seguridad y Buenas Prácticas

### 1. Nunca Compartas tu API Key

```bash
# ❌ NUNCA hagas esto
git add .env
git commit -m "añadir configuración"
git push

# ✅ Siempre añade .env a .gitignore
echo ".env" >> .gitignore
echo ".env.local" >> .gitignore
```

### 2. Usa Variables de Entorno

```bash
# Método correcto
export ANTHROPIC_API_KEY="sk-ant-api03-..."
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-..."' >> ~/.bashrc
```

### 3. Revisa el Código Generado

**Siempre revisa:**
- Consultas SQL (inyección SQL)
- Inputs de usuario (XSS, injection)
- Manejo de archivos (path traversal)
- Credenciales hardcodeadas
- Algoritmos de seguridad

```
Revisa el código en src/auth.py y asegúrate de que:
1. Las contraseñas se hashean correctamente
2. No hay SQL injection
3. Se usan prepared statements
4. Se validan todos los inputs
```

### 4. No Compartas Código Sensible

```
# Al pedir ayuda en foros
❌ "Aquí está mi código con las credenciales de AWS"
✅ "Aquí está mi código con las credenciales reemplazadas por placeholders"
```

---

## 📚 Recursos para Continuar Aprendiendo

### Documentación Oficial

1. **Claude Code**
   - https://docs.claude.com/en/docs/claude-code
   - Guías, ejemplos y mejores prácticas

2. **Anthropic API**
   - https://docs.anthropic.com/
   - Referencia completa de la API

3. **Python**
   - https://docs.python.org/3/
   - Documentación oficial

### Comunidades

1. **GitHub**
   - Issues de Claude Code: https://github.com/anthropics/claude-code/issues
   - Busca ejemplos y soluciones

2. **Discord / Forums**
   - Comunidad de Anthropic
   - Comparte proyectos y aprende

### Cursos y Tutoriales

1. **Python**
   - Real Python (realpython.com)
   - Python.org tutorials

2. **Git**
   - Pro Git Book (git-scm.com/book)
   - GitHub Learning Lab

3. **Desarrollo Web**
   - FastAPI documentation
   - Django documentation
   - Flask documentation

### Libros Recomendados

1. **Python:**
   - "Python Crash Course" - Eric Matthes
   - "Fluent Python" - Luciano Ramalho

2. **Clean Code:**
   - "Clean Code" - Robert C. Martin
   - "The Pragmatic Programmer" - Hunt & Thomas

3. **AI/ML:**
   - "Hands-On Machine Learning" - Aurélien Géron
   - "Deep Learning with Python" - François Chollet

---

## 🎯 Proyectos de Práctica Sugeridos

### Nivel Principiante

1. **Calculadora Avanzada**
   - Operaciones básicas y avanzadas
   - Historial de operaciones
   - Guardar en archivo

2. **Gestor de Contraseñas**
   - Generar contraseñas seguras
   - Almacenar encriptado
   - CLI interactiva

3. **Conversor de Unidades**
   - Temperatura, distancia, peso
   - Múltiples unidades
   - Validación de entrada

### Nivel Intermedio

1. **API REST de Blog**
   - CRUD de posts
   - Usuarios y autenticación
   - Comentarios
   - FastAPI + SQLAlchemy

2. **Scraper de Noticias**
   - Extraer noticias de sitios web
   - Almacenar en base de datos
   - Generar resúmenes

3. **Bot de Discord/Telegram**
   - Comandos personalizados
   - Integración con APIs
   - Base de datos

### Nivel Avanzado

1. **Sistema de Gestión de Inventario**
   - Múltiples almacenes
   - Reportes y estadísticas
   - API REST + Frontend

2. **Pipeline de ML**
   - Carga y limpieza de datos
   - Entrenamiento de modelos
   - API de predicción

3. **Microservicios**
   - Múltiples servicios
   - Docker
   - API Gateway
   - Message queue

---

## 🔧 Herramientas Complementarias

### IDEs y Editores

1. **VS Code** (Recomendado)
   ```bash
   # Instalar en WSL
   code .
   ```
   - Extensiones: Python, GitLens, Prettier

2. **PyCharm**
   - IDE completo para Python
   - Debugging avanzado

3. **Vim/Neovim**
   - Editor de terminal
   - Altamente personalizable

### Control de Versiones

1. **Git**
   ```bash
   # Configuración avanzada
   git config --global core.editor "code --wait"
   git config --global merge.tool vscode
   git config --global diff.tool vscode
   ```

2. **GitHub CLI**
   ```bash
   # Instalar gh
   sudo apt install gh

   # Autenticar
   gh auth login

   # Crear repo
   gh repo create mi-proyecto --public
   ```

### Gestión de Dependencias

1. **Poetry** (Alternativa a pip)
   ```bash
   # Instalar
   curl -sSL https://install.python-poetry.org | python3 -

   # Crear proyecto
   poetry new mi-proyecto
   poetry add fastapi
   ```

2. **pipenv**
   ```bash
   pip install pipenv
   pipenv install requests
   ```

---

## ✅ Checklist de Mejores Prácticas

Usa esta lista en cada proyecto:

**Antes de empezar:**
- [ ] Planificar estructura del proyecto
- [ ] Crear directorio con estructura base
- [ ] Inicializar Git
- [ ] Crear .gitignore apropiado
- [ ] Configurar entorno virtual

**Durante el desarrollo:**
- [ ] Peticiones específicas a Claude
- [ ] Revisar código generado
- [ ] Ejecutar tests frecuentemente
- [ ] Commits pequeños y descriptivos
- [ ] Documentar mientras desarrollas

**Antes de finalizar:**
- [ ] Todos los tests pasan
- [ ] Código documentado
- [ ] README actualizado
- [ ] Sin credenciales en código
- [ ] Dependencias en requirements.txt
- [ ] Código formateado consistentemente

---

## 🎓 Conceptos Clave Aprendidos

- ✅ Cómo formular peticiones efectivas
- ✅ Gestión de contexto en sesiones largas
- ✅ Flujo de trabajo óptimo con Claude Code
- ✅ Optimización de costos
- ✅ Mejores prácticas de seguridad
- ✅ Recursos para continuar aprendiendo
- ✅ Herramientas complementarias
- ✅ Proyectos de práctica

---

## 🎉 ¡Felicidades!

Has completado el Curso Básico de Claude Code. Ahora tienes las herramientas y conocimientos para:

✅ Configurar tu entorno de desarrollo con WSL
✅ Instalar y usar Claude Code
✅ Desarrollar proyectos completos con asistencia de IA
✅ Aplicar mejores prácticas de desarrollo
✅ Continuar aprendiendo de forma autónoma

---

## 🚀 Próximos Pasos Recomendados

1. **Práctica diaria**
   - Usa Claude Code en tus proyectos personales
   - Experimenta con diferentes tipos de proyectos

2. **Explora características avanzadas**
   - MCP (Model Context Protocol) servers
   - Hooks personalizados
   - Comandos slash customizados

3. **Contribuye a la comunidad**
   - Comparte tus proyectos
   - Ayuda a otros en foros
   - Reporta bugs y sugerencias

4. **Mantente actualizado**
   - Sigue las actualizaciones de Claude Code
   - Lee release notes
   - Prueba nuevas características

---

## 📝 Feedback y Contacto

Si tienes preguntas, sugerencias o quieres compartir tus proyectos:

- **GitHub Issues**: Para reportar problemas o sugerencias
- **Documentación**: https://docs.claude.com/
- **Comunidad**: Únete a las discusiones en GitHub

---

## 📚 Referencias Finales

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Anthropic API Docs](https://docs.anthropic.com/)
- [Python Documentation](https://docs.python.org/3/)
- [Git Documentation](https://git-scm.com/doc)
- [WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)

---

**¡Gracias por completar este curso! Mucho éxito en tus proyectos con Claude Code. 🚀**

[← Volver al Módulo 4](./modulo-4-proyecto-practico.md) | [Volver al Inicio](../README.md)

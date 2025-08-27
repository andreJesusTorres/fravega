# 🏪 Fravega - Business Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.2.0-purple.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![SQLite](https://img.shields.io/badge/SQLite-3.0+-green.svg)](https://www.sqlite.org/)
[![PIL](https://img.shields.io/badge/Pillow-9.0+-orange.svg)](https://pillow.readthedocs.io/)
[![ReportLab](https://img.shields.io/badge/ReportLab-3.6+-red.svg)](https://www.reportlab.com/)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)

> Complete business management system for Fravega with administration, human resources, warehouse, deliveries, and cash register modules. **This project is part of my professional portfolio to demonstrate my development skills and practices.**

## 📋 Table of Contents

- [✨ Features](#-features)
- [🛠️ Technologies](#️-technologies)
- [📦 Installation](#-installation)
- [🎮 Usage](#-usage)
- [🏗️ Project Structure](#️-project-structure)
- [🔧 Database Schema](#-database-schema)
- [🧪 Testing](#-testing)
- [📄 License](#-license)

## ✨ Features

### 🎯 Core Functionality
- **🔐 Sistema de Autenticación**: Login con roles diferenciados (Gerente, Administración, RR.HH, Depósito, Caja)
- **📊 Dashboard Administrativo**: Gestión de compras y ventas con TreeView integrado
- **👥 Gestión de RR.HH**: Administración completa de empleados con datos de asistencia y salarios
- **📦 Control de Depósito**: Gestión de stock con productos, cantidades y precios
- **🚚 Sistema de Entregas**: Seguimiento de entregas pendientes de compras online
- **💳 Módulo de Caja**: Carrito de compras, ventas y generación de tickets PDF

### 🎨 User Experience
- **🌙 Tema Personalizado**: Interfaz moderna con tema Fravega personalizado
- **📱 Diseño Responsivo**: Interfaz adaptativa con CustomTkinter
- **🎨 Navegación Intuitiva**: Menú lateral con iconos y navegación fluida
- **📄 Generación de Reportes**: Tickets de venta en PDF con diseño profesional
- **🔍 Búsqueda y Filtros**: Funcionalidades de búsqueda en todos los módulos

## 🛠️ Technologies

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) | 5.2.0 | Modern UI framework for Python |
| [PIL/Pillow](https://pillow.readthedocs.io/) | 9.0+ | Image processing and manipulation |
| [Tkinter](https://docs.python.org/3/library/tkinter.html) | Built-in | GUI framework foundation |

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| [Python](https://www.python.org/) | 3.8+ | Core programming language |
| [SQLite](https://www.sqlite.org/) | 3.0+ | Local database management |
| [ReportLab](https://www.reportlab.com/) | 3.6+ | PDF generation for receipts |

### Development Tools
- **SQLite Browser**: Database management and inspection
- **Custom Theme System**: JSON-based theme configuration
- **Modular Architecture**: Clean separation of concerns

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone [url-del-repositorio]
   cd fravega
   ```

2. **Install dependencies**
   ```bash
   pip install customtkinter pillow reportlab
   ```

3. **Set up the database**
   ```bash
   # The database file (fravega_data.db) is included in the project
   # No additional setup required
   ```

4. **Start the application**
   ```bash
   python main.py
   ```

5. **Access the application**
   - The application will open as a desktop GUI
   - Default window size: 700x450 pixels

## 🎮 Usage

### Getting Started
1. **Launch the application** by running `python main.py`
2. **Login** with your credentials (see database for default users)
3. **Navigate** through different modules using the sidebar menu
4. **Switch themes** using the appearance mode selector

### Key Features Usage

#### 🔐 Authentication System
```python
# Login with role-based access
# Available roles: Gerente, Administración, RR.HH, Depósito, Caja
# Each role has access to specific modules
```

#### 📦 Inventory Management
```python
# Add products to inventory
# Products with same name are added as quantity, not new entries
# Real-time stock tracking and price management
```

#### 💳 Sales System
```python
# Add products to cart
# Calculate totals with tax
# Generate PDF receipts automatically
# Complete transaction processing
```

#### 👥 Employee Management
```python
# Add, modify, and delete employees
# Track attendance and salary information
# Role-based employee data management
```

## 🏗️ Project Structure

```
fravega/
├── 📁 images/                    # Application assets
│   ├── 🖼️ logo.png              # Main application logo
│   ├── 🖼️ banner.png            # Home page banner
│   ├── 🖼️ banner_*.png          # Module-specific banners
│   ├── 🖼️ *.png                 # UI icons and images
│   └── 📁 empleados/            # Employee photos
├── 📁 theme/                     # Custom theme configuration
│   └── 🎨 fravega.json          # CustomTkinter theme file
├── 🐍 main.py                   # Main application file
├── 🗄️ fravega_data.db          # SQLite database
├── 📄 funcionalidad.txt         # Feature documentation
└── 📄 README.md                 # Project documentation
```

## 🔧 Database Schema

### Core Tables
- **user**: Authentication and user management
- **adm_c**: Administrative purchases
- **adm_v**: Administrative sales
- **empleados**: Employee information and HR data
- **stock**: Inventory and product management
- **entregas**: Delivery tracking system

### Key Relationships
- Purchases connect to **Depósito** module
- Sales connect to **Entregas** and **Caja** modules
- Role-based access control across all modules

## 🧪 Testing

### Running Tests
```bash
# Manual testing through GUI
# Test all modules and user roles
# Verify database operations
# Check PDF generation functionality
```

### Test Coverage
- ✅ User authentication and role management
- ✅ Database CRUD operations
- ✅ PDF receipt generation
- ✅ Theme switching functionality
- ✅ Navigation between modules
- ✅ Data validation and error handling

## 📄 License

This project is proprietary software. All rights reserved. This code is made publicly available solely for portfolio demonstration purposes. See the [LICENSE](LICENSE) file for full terms and restrictions.

---

<div align="center">
  <p>
    <a href="#-fravega---sistema-de-gestión-empresarial">Back to top</a>
  </p>
</div>

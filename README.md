# GOIT-PYTHONWEB-HW-01

1. **Library Management System** (`library_management.py`) - A console application for library management system, built following the **SOLID principles**.
2. **Vehicle Factory System** (`vehicle_factory.py`) - An implementation of a vehicle factory following the abstract factory pattern.

The project is managed using **Poetry** for dependency management and includes unit tests using **pytest**.

---

## 🚀 **Getting Started**

Follow the steps below to set up and run the project on your local machine.

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/Gloomcat/goit-pythonweb-hw-01.git
cd GOIT-PYTHONWEB-HW-01
```

### 2️⃣ **Install Poetry**

Make sure you have **Poetry** installed. If not, install it by running:

```bash
pip install poetry
```

### 3️⃣ **Install Dependencies**

Run the following command to install all the project dependencies:

```bash
poetry install
```

### 4️⃣ **Run the Library Management System**

To start the **Library Management System**, run the following command:

```bash
poetry run library_management
```

The console application will prompt you to add, remove, or display books in the library.

---

## 🧪 **Running Tests**

Unit tests are written using **pytest**. To run the tests, use the following command:

```bash
poetry run pytest
```

This will execute all tests in the `tests/` directory and display the results.

---

## 📚 **Using the Library Management System**

When you run the application, you'll see the following prompt:

```
Enter command (add, remove, show, exit):
```

### Commands:
- **add** - Add a new book to the library.
- **remove** - Remove an existing book from the library.
- **show** - Display all books in the library.
- **exit** - Exit the application.

---

## 🔧 **Example Usage**

```bash
Enter command (add, remove, show, exit): add
Enter book title: 1984
Enter book author: George Orwell
Enter book year: 1949
Enter command (add, remove, show, exit): show
Title: 1984, Author: George Orwell, Year: 1949
Enter command (add, remove, show, exit): exit
```

---

## 📝 **Project Details**

- **Language**: Python
- **Dependency Management**: Poetry
- **Testing Framework**: pytest

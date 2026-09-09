cat > README.md <<'EOF'
# Fruit Sales Analysis

A simple Python data project that demonstrates how to create, organize, and export fruit sales data using **pandas**.

## Project Overview

This project creates a pandas DataFrame containing Apple and Banana sales for 2017 and 2018 and exports the results to a CSV file.

The project demonstrates basic data manipulation and CSV generation with Python.

## Technologies Used

- Python
- pandas
- CSV
- Git
- GitHub

## Sales Data

| Year | Apples | Bananas |
|---|---:|---:|
| 2017 | 35 | 21 |
| 2018 | 41 | 34 |

## How It Works

The Python script defines the fruit sales data:

```python
data = {
    "Apples": [35, 41],
    "Bananas": [21, 34]
}
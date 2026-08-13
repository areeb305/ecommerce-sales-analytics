# E-Commerce Sales Analytics

## Project Overview

This project analyzes e-commerce sales data to understand business performance, customer behavior, product performance, and sales trends.

The project follows an end-to-end data analytics workflow covering data preparation, exploratory data analysis, business KPI analysis, SQL analysis, and data visualization.

## Business Problem

An online retail company wants to understand how its sales are performing and identify the main factors contributing to revenue and profitability.

The analysis will answer questions such as:

- How much sales revenue does the company generate?
- Which products generate the most sales revenue?
- Which countries generate the most sales revenue?
- How do sales change over time?
- Which customers contribute the most revenue?
- What sales patterns and customer behaviors reveal potential business opportunities?

## Objectives

1. Clean and prepare the sales dataset.
2. Perform exploratory data analysis.
3. Calculate important business KPIs.
4. Analyze customer and product performance.
5. Investigate sales and profitability trends.
6. Perform analytical queries using SQL.
7. Create visualizations that communicate business insights.
8. Provide actionable business recommendations.

## Key Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQL
- Jupyter Notebook
- Git
- GitHub

## Project Structure

```text
ecommerce-sales-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── reports/
│
├── sql/
│
├── src/
│   ├── __init__.py
│   └── data_cleaning.py
│
├── visualizations/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Dataset

This project uses the Online Retail dataset from the UCI Machine Learning Repository.

The raw dataset contains transaction-level sales records, including invoice numbers, product codes, product descriptions, quantities, invoice dates, unit prices, customer IDs, and countries.

The raw data is excluded from version control. A reusable Python cleaning pipeline processes the raw Excel file and creates an analysis-ready CSV dataset.

### Data Cleaning Summary

The raw dataset contained **541,909 rows and 8 columns**.

After cleaning, the dataset contains **524,878 rows and 13 columns**.

A total of **17,031 rows (3.14%)** were removed during data cleaning.

The cleaning process included:

- Removing duplicate transactions
- Removing cancelled invoices
- Removing non-positive quantities
- Removing zero or negative unit prices
- Removing records with missing product descriptions
- Preserving transactions with missing Customer IDs for non-customer-specific analysis
- Creating a `sales` variable from quantity × unit price
- Creating year, month, month name, and day-of-week features

## Project Progress

- [x] Project setup
- [x] Business problem definition
- [x] Data collection
- [x] Data cleaning
- [ ] Exploratory data analysis
- [ ] KPI analysis
- [ ] Customer analysis
- [ ] Product analysis
- [ ] Country analysis
- [ ] SQL analysis
- [ ] Data visualization
- [ ] Business recommendations
- [ ] Final documentation

## Author

Muhammad Areeb
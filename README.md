# Financial Calculators

This Python program allows the user to access two different financial calculators: either for investment or home loan repayment.

## Table of Contents

1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Setup](#setup)
4. [Usage](#usage)

## General Info

This project aims to provide a simple interface for users who want to calculate the potential returns on their investments, or understand the financial implications of taking a home loan. The program supports calculations for both simple and compound interest for investments, and monthly repayment amount for home loans.

## Technologies

Project is created with:
* Python version: 3.X
* math module for mathematical operations

## Setup

To run this project, you just need to have Python (version 3.X) installed on your machine.

1. Clone the repository:

```
$ git clone https://github.com/{YourUsername}/financial-calculator.git
```

2. Change into the project directory:

```
$ cd financial-calculator
```

3. Run the program with Python:

```
$ python main.py
```

## Usage

When you run the program, a menu will be displayed asking you to choose between two options: 'investment' and 'bond'. 

If you choose 'investment', you will be prompted to enter:

1. The amount you want to invest
2. The interest rate
3. The duration of your investment
4. The type of interest: 'simple' or 'compound'

The program will then calculate and display the total amount at the end of the investment period.

If you choose 'bond', you will be prompted to enter:

1. The current value of your house
2. The annual interest rate of the loan
3. The number of months you plan to repay the loan

The program will then calculate and display your monthly repayment amount.

In case of invalid inputs, the program will indicate the error and prompt you to try again.

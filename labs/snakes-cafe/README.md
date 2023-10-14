# Snakes Cafe

## Overview

A command-line utility that mimics a Point of Sale (POS) system for a restaurant. The program prints out the menu for the restaurant, takes user orders, and acknowledges the orders entered.

## Feature Tasks and Requirements

- When run, the program prints an intro message and the menu for the restaurant.
- The restaurant’s menu includes appetizers, entrees, desserts, and beverages.
- The program prompts the user for an order.
- When a user enters an item, the program prints an acknowledgment of their input.
- The program tells the user how to exit.
  
## Usage

To run the program, open a terminal and navigate to the project folder. Then, execute the following command:

```
$ python snakes_cafe.py
```

### Sample Interaction

```
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

...

***********************************
** What would you like to order? **
***********************************
> Cake

** 1 order of Cake has been added to your meal **

> Cake

** 2 orders of Cake have been added to your meal **

> quit
```

## Stretch Goals

- Print out a summary of the complete order.
- Only allow ordering items on the menu.
- Allow ordering items not on the menu but give a custom reply.

## Installation

- Clone this repository to your local machine.
- Navigate to the project directory.
- Run `python snakes_cafe.py` to start the program.

## Author

Jesse Pena
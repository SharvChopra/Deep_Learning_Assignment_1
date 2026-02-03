# Perceptron from Scratch – Logic Gates

This project demonstrates the implementation of a **single-layer Perceptron from scratch** using pure Python (no machine learning libraries).  


## Objective

- Implement a perceptron without using ML libraries
- Train the same algorithm on multiple logic gates
- Observe convergence behavior
- Understand why **XOR cannot be learned** by a single perceptron

## Project Structure

.
├── main.py
├── output/
│ ├── And_output.png
│ ├── Or_output.png
│ ├── Nand_output.png
│ ├── Nor_output.png
│ └── XOR_output.png
├── venv/
└── README.md

## Results

![AND Gate-Output][output/And_output.png]
![OR Gate-Output][output/Or_output.png]
![NAND Gate-Output][output/Nand_output.png]
![NOR Gate-Output][output/Nor_output.png]
![XOR Gate-Output][output/XOR_output.png]

## Conclusion
It shows how single layer Perceptron is implemented from scratch
It shows the limitation of single perceptron 
 - Learning Non-linear function is a problem shown using XOR Gate

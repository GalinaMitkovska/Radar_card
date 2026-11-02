# 2D Radar Range-Doppler Detection

## Description

This project implements a target detection algorithm for a 2D radar Range-Doppler map using Python and NumPy.

The input is a 2D matrix of complex values. The algorithm calculates the power of each cell and detects potential target peaks by comparing the power of each cell with the average noise power in its surrounding area.

## Algorithm

1. Convert complex values into power.
2. Select a rectangular window around each cell under test.
3. Exclude the central guard area from noise estimation.
4. Calculate the average noise power using the surrounding training cells.
5. Calculate an adaptive detection threshold.
6. Mark cells whose power exceeds the threshold as detected targets.

## Parameters

- Range guard cells: 2
- Doppler guard cells: 1
- Range training cells: 3
- Doppler training cells: 2
- Probability of false alarm (Pfa): 0.001

## Technologies

- Python
- NumPy
- Matplotlib
- uv

## Run the project

Install dependencies:

```bash
uv sync
```

Run the program:

```bash
uv run main.py
```

## Visualization

Matplotlib is used to display the Range-Doppler power map and the detected target positions.
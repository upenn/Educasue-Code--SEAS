# Educause-Code--SEAS


# Canvas-Late-and-Grade-Reduction

This repository contains Python scripts and related files for automating grade adjustments within Canvas LMS.

## Table of Contents

- [Files](#files)
  - [grade_adjustments.py](#grade_adjustmentspy)
  - [run_grade_adjustments.sh](#run_grade_adjustmentssh)
  - [crontab](#crontab)
  - [canvas/canvas.py](#canvascanvaspy)
  - [config/config_vars.py](#configconfig_varspy)

## Files

### grade_adjustments.py

- **Description**: This Python script automates the process of adjusting grades in Canvas based on specific criteria. It communicates with the Canvas API to perform grade adjustments waiving late submissions, and reducing grades that are over the maximum point value.

- **Usage**: To use this script, follow these steps:
  1. Configure the script settings, including Canvas LMS instance details and file paths.
  2. Run the script by executing it with Python.

### run_grade_adjustments.sh

- **Description**: This Bash script simplifies the execution of `grade_adjustments.py`. It handles the virtual environment activation and script execution process. This can be used to set a crontab that runs regularly.

- **Usage**: To run the grade adjustment script using this Bash script, open your terminal, navigate to the repository's root directory, and execute the Bash script:
   ```shell
   ./run_grade_adjustments.sh

### crontab

**Description**: This file contains a crontab configuration that schedules the automated execution of the grade adjustment script at specific intervals or times. Crontab is used for task automation on Unix-like systems.

**Usage**: To set up automated grade adjustments, add the contents of this crontab file to your system's crontab configuration, specifying when and how often you want the grade adjustments to run.

---

### canvas/canvas.py

**Description**: This Python module, located in the canvas directory, provides functionality for interacting with the Canvas API. It is utilized by grade_adjustments.py for communicating with Canvas LMS.

**Usage**: This module is imported and used by grade_adjustments.py. You do not need to run it directly.

---

### config/config_vars.py

**Description**: This Python file contains configuration variables used by the grade adjustment script and other components. It may include settings like API keys, Canvas LMS endpoints, or file paths. Dotenv can be used to create a .env file to store your access token.

**Usage**: Customize the variables in this file to match your specific Canvas LMS setup and preferences. Ensure that the script references these variables correctly for proper execution.

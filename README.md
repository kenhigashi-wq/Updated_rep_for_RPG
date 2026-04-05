# Enhanced RPG Character Manager

This project is an upgraded version of an existing Python-based RPG Character Manager.  
The original program allowed users to create and manage RPG characters using a text-based menu system.  
This version enhances the project by adding **data analysis, visualization, CSV data management, and procedural generation**, as required by the assignment.

---

## Features

### Core RPG Functionality
- Create RPG characters (manual or randomized)
- Store character stats internally
- Manage character data during runtime

### Data & Analysis Enhancements
- Uses **Pandas** to convert character statistics into DataFrames
- Calculates statistical summaries across characters:
  - Mean
  - Minimum
  - Maximum
- Exports character data to CSV files
- Imports character data from CSV files to restore game state

### Visualization
- Uses **Matplotlib** to visualize character statistics
- Displays individual character stat charts
- Visualizations are generated from real gameplay data


---

## How to use
If in codespaces pip install faker, pandas
Run the program in main.
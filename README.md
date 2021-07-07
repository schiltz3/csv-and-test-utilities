# csv-and-test-utilities
### Utilities to convert data files to CSV format, and utilities to create file structures en masse.

 * **MakeTestFolder.py** - Creates folders, Blank files, and Metadata files based on the Tests spreadsheet.
     * **Tests.xlsx** - Used to configure MakeTestFolder.py.
 * **txttocsv.sh** - Converts text files created by Unico-GUI to the standard CSV file format. Can be used as a base to create other converters.
    ```BASH
    ./txttocsv.sh <file_to_convert.txt>
    ```
 * **PlotCSV.plt** - Uses GNUPlot to plot standard CSV files. 
    ```BASH
    gnuplot -c PlotCSV.plt <path\to\file> <index of first column> <index of last column>
    ```
---
### CSV Format:
CSVs are created in the folowing format, and must be in this format to use with PlotCSV
|Column Name|Column Name|...|
|---|---|---|
|data|data|...|
|...|...|...|...|
---
## **A better CSV plotter can be found [here](https://github.com/schiltz3/csv-plotter)**

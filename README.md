# csv-and-test-utilities
#### Utilities to convert data files to CSV format, and utilities to create file structures en masse.

 * MakeTestFolder.py - Creates folders, Blank files, and Metadata files based on the Tests spreadsheet.
     * Tests.xlsx - Used to configure MakeTestFolder.py.
 * txttocsv.sh - Converts text files created Unico-GUI to the standard CSV file format. Can be used as a base to create other converters.
 * PlotCSV.plt - Uses GNUPlot to plot CSV files created by txttocsv.sh. Currently broken as it tries to start from the 3rd line in a file rather than the 1st.

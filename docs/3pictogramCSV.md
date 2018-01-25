# 3. Prepare Pictogram CSV File

An important tool that will be reference in the beginning is the spreadsheet and comma separated values (CSV) file that will hold the Unicode value, the old name, and new name of the pictogram. Currently this file also contains images of the pictograms, and while the images do not need to be placed in the cells, those columns need to remain. Otherwise the scripts will pull information from the wrong columns.

### Convert Spreadsheet to CSV
1. Remove any blank columns before the Unicode column, which must be the first column.
2. Remove any blank columns after the last Pictogram Image column, which must be the last column.
3. It is okay to have empty rows at the bottom or throughout the document.
4. Export the Pictograms sheet to a Comma Separated Values file and place it in the SpreadsheetExport folder.

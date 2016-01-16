## Introduction ##
SequenceDatabaseViewer is a design for a web application that will allow user to view the data stored in a MySQL database. This database was created by processing the raw XML file, which was downloaded from the "expasy.org".  The processing was carried out by a python script (python_processor.py)

## Description ##
SequenceDatabaseViewer has four components. Each of which links the information stored inside the different tables in a "mysql" database. The components are:

1. UNIPROTID.php - script to generate an XML file of all protein IDs(strings).

2. Viewer.html - Creates user interface by displaying all protein IDs in the form of a list.

3. getUNIPROTID.php - Selection of protein IDs(strings) used to generate a query to extract a protein sequence represented as a string, and PubemedIDs(strings)

4. getpubs.php - Selection of PubmedIDs(strings) used to generate a query to extract citation information(strings)




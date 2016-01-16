## Introduction ##
SequenceDatabaseViewer is a design for a web application that will allow user to view the data stored in a MySQL database. This database was created by processing the raw XML file, which was downloaded from the "expasy.org".  The processing was carried out by a python script (name-of-script)

## Description ##
SequenceDatabaseViewer has four components. Each of which links the information stored inside the different tables in a "mysql" database. The components are:

1. UNIPROTID.php - script to generate an XML file of all protein IDs().

2. Viewer.html - Creates user interface by displaying all protein IDs in the form of a list.

3.

4.


For example, the UNIPROTID.php is the script to generate an XML file of all the protein id of  ubiquitin conjugating enzyme E2.Then Viewer.html will create a user interface by showing all the protein id in the form of scrolling list.When any protein id is slected it will bring up the information about the sequence and article related to that id.The later step is done with the help of getUNIPROTID.php and getpubs.php.

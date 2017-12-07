Culture Grid
============

Converting culture grid web service data on institutions for use in other projects.

The culture grid was an aggregation platform run by the Collections Trust, and hosted web services that provided details of cultural instititions, collections and more.

There is [a very interesting blog post](https://museumscomputergroup.org.uk/culture-grid/) by Nick Poole, previously CEO of the Collections Trust, that gives some background to this, the wider work of aggregating museum data, and the People's Network.

While the culture grid's API is still running, this repository is a simple converter to convert the data held on institutions into CSV format for repurposing (and correcting as it's out of date).

See [culture_data.csv](https://github.com/LibrariesHacked/culture-grid/blob/master/culture_data.csv) for an extract.

Original data extracted from this XML web service:

http://www.culturegrid.org.uk/index/select/?q=dcterms.isPartOf:MLAInstitutions&version=2.2&start=0&rows=100000&indent=on

Licence
--------

The data was provided by the Culture Grid as Open Government Licence.
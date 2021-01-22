This script relies on that you have the description standard on the ports that LibreNMS has, the link to their page https://docs.librenms.org/Extensions/Interface-Description-Parsing/
You must edit the script before you use so that you have a functioning API token and also the correct url and uri for your LibreNMS installation. This script only relies on LibreNMS API.

The are 3 different choices one have to create different things, either it's a new bill, update a bill or export ports to a csv file.
 
To create a new bill just enter your customers name. This will prompt you for settings for the bill and create the bill but it will also give you the bills ID. This script will only created a CDR bill
To update a bill you will enter your customers name for the collection of their ports and also the bill ID that you want update.
The CSV export is still under development but for now it will export all the ports that are related to a customer to a predefined file of your choosing. 

If you have any improvements on the script feel free to make an pull request or make an issue and I will try to fix it. 

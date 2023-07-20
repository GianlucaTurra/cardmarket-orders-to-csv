# cardmarket-orders-to-csv

Before running the script it's needed to get the cookies and the headers to fill the 'sensitive_data.py' file.
Login into the cardmarket website, open the inspector of your browser, got to the 'Network' tab and refresh the page.
Now it is possible to copy the cURL and convert it to python code (two dictionaries) to set up the 'sensitive_data.py' file.
This operation has to be done at every new login into the website.

The script asks for an input once run: yes (orders are already paid) or no (orders are not paid yet).
Whether the provided input is in lower or upper case makes no difference.

Once run the script provides as output a .csv file named 'Order.csv' into the project's folder.

This script should work with every TCG on cardmarket.com

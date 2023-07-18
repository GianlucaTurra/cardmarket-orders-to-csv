from bs4 import BeautifulSoup
import requests
from sensitive_data import cookies, headers


def choose_order_status():
    """
    Ask as input if the orders to scrap are already paid or not
    :return: the URL of the page to scrap the data from
    """
    answer = input('Are the orders already paid or no? (yes/no) ').lower()
    if answer == 'yes':
        order_status = 'Paid'
    elif answer == 'no':
        order_status = 'Unpaid'
    else:
        print('Please enter a valid input')
    page_url = f'https://www.cardmarket.com/it/YuGiOh/Orders/Purchases/{order_status}'
    return page_url


def get_order_links(page_link):
    """
    Finds the links of all the orders in the page
    :param page_link: (str) the url of the page
    :return: (list) the orders' link list
    """
    response = requests.get(url=page_link, cookies=cookies, headers=headers)
    # cookies and headers have to be manually taken from the webpage's network tab
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all(name="div", class_="col-longNumber")
    order_list = []
    for div in divs:
        a = div.find('a')
        try:
            if 'href' in a.attrs:
                link = a.get('href')
                order_list.append(link)
        except AttributeError:
            pass
    return order_list


def get_order_library():
    """
    Scraps the single order pages to build a list of dictionaries with cards data
    :return: (list) list of dictionaries
    """
    orders = get_order_links(choose_order_status())
    orders_library = []
    for order in orders:
        order_response = requests.get(f'https://www.cardmarket.com{order}', cookies=cookies, headers=headers)
        # cookies and headers have to be manually taken from the webpage's network tab
        order_soup = BeautifulSoup(order_response.text, 'html.parser')
        seller = order_soup.find(name='span', class_='seller-name').text
        # seller's name is found outside the loop being the same for every card in the order
        table = order_soup.find_all(name='tr')
        # cards' data is stored inside 'tr'. all 'tr' are stored in the list table to be iterated through
        for row in table:
            order_data = {}
            # a new dictionary is created for every card to be appended at the list 'orders_library'
            card_name = row.find(name='div', class_='text-muted').text
            card_amount = int(row.find(name='td', class_='amount').text.replace('x', ''))
            card_price = row.find(name='td', class_='price').text.replace(' €', '')
            order_data['Card'] = card_name
            order_data['Amount'] = card_amount
            order_data['Unit Prize'] = card_price
            order_data['Seller'] = seller
            orders_library.append(order_data)
    return orders_library

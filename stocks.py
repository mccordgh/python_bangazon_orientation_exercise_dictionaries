stockDict = { 'GM': 'General Motors', 'CAT':'Caterpillar', 'EK':"Eastman Kodak", "GE": 'General Electric' }
purchases = [ ( 'GE', 100, '10-sep-2001', 48 ), ( 'CAT', 100, '1-apr-1999', 24 ), ( 'GE', 200, '1-jul-1998', 56 ) ]

print('\n')

for stock in purchases:
	ticker = stock[0]
	shares = stock[1]
	share_price = stock[3]
	price = shares * share_price
	full_company_name = stockDict[ticker]
	# print(ticker + ' : ' + full_company_name + ' : $' + price)
	print("Purchased [{0}] {1}\n  {2} shares at ${3} for a total of ${4}".format(ticker, full_company_name, shares, share_price, price))

print "Enter temperature change of solution"
temp = float(raw_input(">>> "))
print "Enter price per 500g of solid"
price = float(raw_input(">>> "))
print "Enter mass of solid, leave blank for 5.00 g"
mass = float(raw_input(">>> "))

tpredic = temp * 1.25 * (10/(mass+50))
print tpredic
tcpd = (price/500) * 10
print tcpd
answer = tpredic / tcpd

print "The answer is %d degrees per $ " % answer

def isValidCoupon(couponCode, totalAmount):
    if (couponCode == "SALE" or couponCode == "BIGSALE") and totalAmount >= 50:
        return True
    elif couponCode == "LILSALE":
        return True
    else:
        return False

print(isValidCoupon("SALE", 50))
print(isValidCoupon("BIGSALE", 60))
print(isValidCoupon("LILSALE", 10))
print(isValidCoupon("SALE", 40))
print(isValidCoupon("BIGSALE", 49))
print(isValidCoupon("NOSALE", 100))

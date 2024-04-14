#Task 1
#tag products based on keywords
#tags: electronics, apparel, home & kitchen
import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

def product_tagger(descript):
    electronic_tag = r"\b(smartphone|television|computer|laptop)"
    apparel_tag = r"\b(t-shirt|pants|jacket|socks)"
    home_tag = r"\b(kitchen|room|candle|utensil)"

    try:
        if re.search(electronic_tag, descript, re.IGNORECASE):
            return "Electronics"
        elif re.search(apparel_tag, descript, re.IGNORECASE):
            return "Apparel"
        elif re.search(home_tag, descript, re.IGNORECASE):
            return "Home & Kitchen"
    except:
        print("An error occured, please try again.")

for d in descriptions:
    print(product_tagger(d), ":" , d)

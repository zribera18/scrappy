import requests, re, sqlite3, json

print("hi")

# r = requests.get('https://www.tactics.com/burton/cartel-snowboard-bindings/black', 0)
#
# title = re.findall(r'<meta name="description" content="(.*?)">', r.text)
#
# price = re.findall(r'\'price\':(.*?)\}', r.text)
#
# brand = re.findall(r'\'brand\':(.*?),', r.text)
# print("title:" + str(title))
# print("price:" + str(price))
# print("brand:" + str(brand))


def scrappy(type, url):

    r = requests.get(url, 0)

    with open('config.json') as f:
        config = json.load(f)
    print(config[type]["title"])

    for x in config[type]:
        # print(config["ecommerce"][x])
        for regex in config[type][x]:
            capture = re.findall(regex, r.text)
            print("\"" + str(x) + "\": " + str(capture))
        # for regex in x:
        #     print(regex)

    # if url.startswith("http"):
    #     page_data = requests.get(url, 0)
        # scrape_page(page_data, config)
    # else:
    #     Try prepending http
        # tmp_url = "http://" + url
        # page_data = requests.get(tmp_url, 0)
        # scrape_page(page_data, config)


    # output_to_tsv =>
    # output_to_sql =>

if __name__ == "__main__":
    url = 'https://www.tactics.com/burton/malavita-snowboard-bindings'
    print("tactics:")
    scrappy("ecommerce", url)
    url = 'https://www.backcountry.com/burton-malavita-est-snowboard-binding-09-10'
    print("backcountry:")
    scrappy("ecommerce", url)
    # https: // www.amazon.com / dp / B07TW9888V
    url = 'https://www.amazon.com/dp/B07TW9888V'
    print("amazon:")
    scrappy("ecommerce", url)


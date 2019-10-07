from driver_load import driver_load
from time import sleep


def main():
    url = "https://mobile.lebara.com/dk/en/checkout/select-number"
    driver = driver_load()

    driver.get(url)
    buttonCustomer = driver.find_element_by_xpath("""/html/body/main/header/div/div/div/div/div[1]/ul/li[4]/a""")
    buttonCustomer.click()
    sleep(2)

    number_labels = driver.find_element_by_xpath("""/html/body/main/div[6]/div/div[3]/div/div/div/div[2]""").find_elements_by_tag_name("input")##div Sa Label Tagovima U Kojima Se Nalaze Brojevi niz u pitanju
    numbers = set()##Skup(nema duplikata)
    for number in number_labels:
        numberText = number.get_attribute("value")
        numbers.add(numberText)
        print(numberText)


if __name__ == "__main__":
    main()
    input()
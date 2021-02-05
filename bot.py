from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WebBot:
    def __init__(self):
        #Link of Product
        self.link = "https://www.walmart.com/ip/Apple-AirPods-with-Charging-Case-Latest-Model/604342441"

        #Personal and Financial Information To Input
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.phone_number = ""
        self.credit_card_number = ""
        self.credit_card_exp_mon = ""
        self.credit_card_exp_year = ""
        self.credit_card_exp_year_end = ""
        self.credit_card_sec = ""
        self.address = ""
        self.city = ""
        self.state = ""
        self.state_full_name = ""
        self.zip_code = ""
        

        #Run the program
        self.run()

    def run(self):
        #Initializes web browser to Safari
        self.driver = webdriver.Safari()
        self.driver.maximize_window()

        #Gets webpage from link to product
        self.driver.get(self.link)

        #Runs the following functions to purchase item.
        run:bool = True
        while run:
            try:
                run = False
                self.add_to_cart() #Adds item to cart
            except:
                self.driver.refresh()
                print("refreshed")
        self.checkout() #Goes to checkout
        self.fill_out_info() #Fills out personal info
        self.fill_out_payment_info() #Fills out payment info
        self.fill_out_shipping_info() #Fills out shipping info
        self.submit() #Submits Order
        self.quit() #Ends Program
    
    def add_to_cart(self):
        #Adds item to cart
        self.wait = WebDriverWait(self.driver, 10)
        self.add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[7]/div[1]/div/div/div/button"))).click()
        print("Added To Cart")
        #Navigates To cart
        self.wait = WebDriverWait(self.driver, 10)
        self.go_to_cart = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div[1]/div/div/div/div/div[1]/div[3]/a"))).click()
        print("In Cart")

    def checkout(self):
        #Goes to checkout
        self.wait = WebDriverWait(self.driver, 10)
        self.checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button"))).click()
        print("Checkout Selected")
        #Selects Guest Checkout
        self.wait = WebDriverWait(self.driver, 10)
        self.guest_checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/main/div[4]/div/div[2]/button"))).click()
        print("Guest Checkout Selected")
    
    def fill_out_info(self):
        #Clicks button to allow user to fillout information
        self.wait = WebDriverWait(self.driver, 10)
        self.fill_out_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='checkoutApp']/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/section/div/a")))
        self.fill_out_button.click()
        
        self.wait = WebDriverWait(self.driver, 10)

        #User information filled out
        self.first_name_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/section/div[1]/div[1]/label/div/input")))
        self.first_name_button.send_keys(self.first_name)

        self.last_name_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/section/div[1]/div[2]/label/div/input")))
        self.last_name_button.send_keys(self.last_name)

        self.email_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/section/div[1]/div[3]/label/div/input")))
        self.email_button.send_keys(self.email)

        self.phone_number_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/section/div[1]/div[4]/label/div/input")))
        self.phone_number_button.send_keys(self.phone_number)

        self.email_contact_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[2]/label/div/input")))
        self.email_contact_button.send_keys(self.email)

        self.phone_number_contact_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[3]/label/div/input")))
        self.phone_number_contact_button.send_keys(self.phone_number)

        #Goes to payment information to be filled out
        self.continue_to_payment_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button"))).click()

        print("Personal Info Filled Out")


    def fill_out_payment_info(self):
        #Fills out credit card number
        self.credit_card_number_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[1]/div/input")))
        self.credit_card_number_button.send_keys(self.credit_card_number)

        #Selects expiration month of credit card
        self.credit_card_exp_mon_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[2]/div[1]/div/div[1]/label/div/div/select")))
        for option in self.credit_card_exp_mon_button.find_elements_by_tag_name('option'):
            if option.text == self.credit_card_exp_mon:
                option.click()
                break


        #Selects expiration year of credit card
        self.credit_card_exp_year_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[2]/div[1]/div/div[2]/label/div/div/select")))
        for option in self.credit_card_exp_year_button.find_elements_by_tag_name('option'):
            if option.text == self.credit_card_exp_year:
                option.click()
                break

        #Fills out credit card security code
        self.credit_card_number_sec_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[2]/div[2]/div/div[2]/div/input")))
        self.credit_card_number_sec_button.send_keys(self.credit_card_sec)

        print("Credit Card Info Filled Out")



    def fill_out_shipping_info(self):
        #Fills out shipping information
        self.first_name_shipping_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[2]/label/div/input")))
        self.first_name_shipping_button.send_keys(self.first_name)

        self.last_name_shipping_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[3]/label/div/input")))
        self.last_name_shipping_button.send_keys(self.last_name)

        self.address_shipping_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[4]/label/div[2]/div/div/input")))
        self.address_shipping_button.send_keys(self.address)

        self.city_shipping_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[6]/div/div[1]/label/div/input")))
        self.city_shipping_button.send_keys(self.city)

        self.zip_code_shipping_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[7]/div/div[1]/label/div/input")))
        self.zip_code_shipping_button.send_keys(self.zip_code)

        self.state_shipping_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[6]/div/div[2]/label/div/div/select")))
        for option in self.state_shipping_button.find_elements_by_tag_name('option'):
            if option.text == self.state:
                option.click()
                break

        print("Shipping Info Filled Out")

        time.sleep(10)


    def submit(self):
        #Clicks submit button to complete order
        self.wait = WebDriverWait(self.driver, 10)
        self.submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[3]/button"))).click()

        print("ORDER SUBMITTED!")

    def quit(self):
        #Closes webpage
        self.driver.close()


class Walmart(WebBot):
    def add_to_cart(self):
        #Adds item to cart
        self.wait = WebDriverWait(self.driver, 10)
        self.add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div[2]/section/div[1]/div[3]/button"))).click()
        print("Added To Cart")

    def checkout(self):
        #Goes to checkout
        time.sleep(5)
        self.wait = WebDriverWait(self.driver, 10)
        self.checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/div/div[3]/div/div/div[2]/div[1]/div[2]/div/button[1]"))).click()
        print("Checkout Selected")
        #Selects Guest Checkout
        self.wait = WebDriverWait(self.driver, 10)
        self.guest_checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[1]/div/section/section/div/button"))).click()
        print("Guest Checkout Selected")
        #Selects Delivery Option
        self.wait = WebDriverWait(self.driver, 10)
        self.delivery_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button"))).click()

    def fill_out_info(self):
        self.wait = WebDriverWait(self.driver, 10)

        #User information filled out
        self.first_name_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[1]/div[2]/input")))
        self.first_name_button.send_keys(self.first_name)

        self.last_name_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[1]/div[3]/input")))
        self.last_name_button.send_keys(self.last_name)

        self.email_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[1]/div[5]/div/input")))
        self.email_button.send_keys(self.email)

        self.phone_number_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[1]/div[4]/input")))
        self.phone_number_button.send_keys(self.phone_number)

        print("Personal Info Filled Out")

        #Fill Out Shipping Info
        self.address_shipping_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[2]/div[1]/input")))
        self.address_shipping_button.send_keys(self.address)

        self.city_shipping_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[2]/div[3]/input")))
        self.city_shipping_button.clear()
        self.city_shipping_button.send_keys(self.city)

        self.zip_code_shipping_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[2]/div[4]/div[2]/div/input")))
        self.zip_code_shipping_button.clear()
        self.zip_code_shipping_button.send_keys(self.zip_code)

        self.state_shipping_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[2]/div[4]/div[1]/div/select")))
        for option in self.state_shipping_button.find_elements_by_tag_name('option'):
            if option.text == self.state_full_name:
                option.click()
                break

        self.continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[2]/div[2]/button"))).click()

        print("Shipping Info Filled Out")

    def fill_out_payment_info(self):
        self.wait = WebDriverWait(self.driver, 10)

        #Fills out credit card number
        self.credit_card_number_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[1]/div/div[3]/input")))
        self.credit_card_number_button.send_keys(self.credit_card_number)

        #Selects expiration month of credit card
        self.credit_card_exp_mon_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[1]/div/div[4]/div[1]/div/div/div/div[1]/span/div/select")))
        for option in self.credit_card_exp_mon_button.find_elements_by_tag_name('option'):
            if option.text == self.credit_card_exp_mon:
                
                option.click()
                break


        #Selects expiration year of credit card
        self.credit_card_exp_year_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[1]/div/div[4]/div[1]/div/div/div/div[2]/span/div/select")))
        for option in self.credit_card_exp_year_button.find_elements_by_tag_name('option'):
            if option.text == self.credit_card_exp_year_end:
                option.click()
                break

        #Fills out credit card security code
        self.credit_card_number_sec_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[1]/div/div[4]/div[2]/div/div/div/input")))
        self.credit_card_number_sec_button.send_keys(self.credit_card_sec)

        print("Credit Card Info Filled Out")

        self.review_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[3]/div/button"))).click()

        print("Order Review")

    def fill_out_shipping_info(self):
        #Not Needed due to the way walmart checkout functions. Left empty so that run function works fine.
        return

    def submit(self):
        self.wait = WebDriverWait(self.driver, 10)

        #Submits Order
        self.submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[1]/div/button"))).click()
        print("ORDER SUBMITTED!")
        time.sleep(10)
        return


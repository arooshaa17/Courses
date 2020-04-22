# Login Page Locators #
login_link = "//a[@class='btn' and contains(text(), 'Sign In')]"
email_field = "email"
password_field = "password"
login_button = "//button[@type='submit']"
my_profile = "//section[@id='my-courses']"
login_error = "//li[contains(text(), 'Email or password is incorrect')]"

# Home Page Locators #
course_link = "(//div[@class='mobile-nav-item hidden-mobile nav-item nav-tab'])[1]"
product_link = "(//div[@class='mobile-nav-item hidden-mobile nav-item nav-tab'])[2]"
discover_link = "(//div[@class='mobile-nav-item hidden-mobile nav-item nav-tab'])[3]"
page_selectors_list = [course_link, product_link, discover_link]

# Course Page Locators #
explore_course = "//a[@class='btn-neutral']"
search_box = "//input[@name='search_query']"
search_button = "//*[@class='icon fa fa-search']"
course = "//h3[contains(text(),'{0}')]"
enroll_button = "//button[@class='btn enroll-btn legacy w-100']"
free_trial = "//button[@id='free_trial_start_button_button']"
amount = "//div[@class='total-subscriptions-container price-line horizontal-box']"
my_course = "//a[contains(text(),'{0}')]"
upgrade_link = "//a[@class='btn-brand btn-upgrade']"

# Payments Page Locators
first_name = "//input[@id='firstName']"
last_name = "//input[@id='lastName']"
address = "//input[@id='address']"
unit = "//input[@id='unit']"
city = "//input[@id='city']"
country = "//select[@id='country']"
state = "//select[@id='state']"
postal_code = "//input[@id='postalCode']"
card_number = "//input[@id='cardNumber']"
security_code = "//input[@id='securityCode']"
card_expiration_month = "//select[@id='cardExpirationMonth']"
card_expiration_year = "//select[@id='cardExpirationYear']"
place_order_button = "//button[@id='placeOrderButton']"
card_error = "//span[@class='text-danger']"


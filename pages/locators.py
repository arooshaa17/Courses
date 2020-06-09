
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
view_course_link = "//a[contains(text(),'View Course')]"
start_course_link = "//a[@class='btn btn-primary action-resume-course']"




# Course Page Locators #
explore_course = "//a[@class='btn-neutral']"
search_box = "//input[@name='search_query']"
search_button = "//*[@class='icon fa fa-search']"
course = "//h3[contains(text(),'{0}')]"
enroll_button = "//a[@class='enroll-btn legacy btn w-100']"
free_trial = "//button[@id='free_trial_start_button_button']"
amount = "//div[@class='total-subscriptions-container price-line horizontal-box']"
my_course = "//a[contains(text(),'{0}')]"
upgrade_link = "//a[@class='btn-brand btn-upgrade']"
course_tab = "//a[contains(text(),'Course')]"
progress_tab = "//a[contains(text(),'Progress')]"
wiki_tab = "//a[contains(text(),'Wiki')]"
discussion_tab = "//a[contains(text(),'Discussion')]"
enter_course = "//a[@class='course-target-link enter-course ']"
course_title = "//span[@class='course-name']"
course_module_tab = "//button[@id='tab_1']"
logo = "//img[@class='logo']"
next_button = "//div[@class='sequence-nav']//button[@class='sequence-nav-button button-next']"
all_courses = "//a[@class='course-link']"
audit_course = "//input[@name='audit_mode']"
upgrade_price = "//a[@class='btn-brand btn-upgrade']//span[@class='price']"
cart_price = "//span[@class='text-right']//span"
course_card_href_list = '//div[@id="displayed-results"]//a'

# Filters
any_filter = "//button[contains(text(),'{0}')]"
verified_filter = "//button[@data-value='verified']"
partner_dropdown = "//select[@class='facet-select select-organizations']"
partner_submit_button = "//button[@class='btn-edged-blue select-facet-button']"
filter_buttons_list = "//button[@class='facet-option js-clear']"
result_message = "//h2[@class='js-result-msg hide-phone']"
course_list = "//a[@class='course-link']"
course_name = "//h3[contains(text(),'CS50's Web Programming with Python and JavaScript')]"
python_filter = "//button[@data-display-name='python']"
filter_element = "//button[@data-display-name='{0}']"

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

# Page footer
footer_logo = "//div[@class='edx-footer-logo']//a//img"
about_link = "//a[contains(text(),'About')]"
for_business = "//a[contains(text(),'edX for Business')]"
terms = "//a[contains(text(),'Terms of Service & Honor Code')]"
privacy = "//a[contains(text(),'Privacy Policy')]"
accessibility = "//a[contains(text(),'Accessibility Policy')]"
blog = "//a[contains(text(),'Blog')]"
contact_us = "//a[contains(text(),'Contact Us')]"
help_c = "//a[contains(text(),'Help Center')]"
footer_elements_list = [footer_logo, about_link, for_business, terms, privacy, accessibility, blog, contact_us, help_c]

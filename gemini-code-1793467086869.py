import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# বিভিন্ন ইউজার-এজেন্ট তালিকা (বট বিভিন্ন ডিভাইস হিসেবে ঢুকবে)
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
]

def visit_website(url):
    options = Options()
    # র‍্যান্ডম ইউজার এজেন্ট সেট করা
    random_user_agent = random.choice(user_agents)
    options.add_argument(f'user-agent={random_user_agent}')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        print(f"Visiting with User-Agent: {random_user_agent}")
        driver.get(url)
        
        # ৫ থেকে ১০ মিনিটের মধ্যে র‍্যান্ডম সময় অপেক্ষা (৩০০ থেকে ৬০০ সেকেন্ড)
        wait_time = random.randint(300, 600)
        print(f"Waiting for {wait_time // 60} minutes on page...")
        
        # পেজে স্ক্রোল ডাউন সিমুলেট করা
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
        time.sleep(wait_time / 2)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(wait_time / 2)
        
    finally:
        driver.quit()

# ব্যবহার করার নিয়ম
target_url = "https://your-website-link.com"
# visit_website(target_url)
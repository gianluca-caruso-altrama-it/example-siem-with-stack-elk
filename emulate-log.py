import random
import time


def generate_fake_nginx_log():
    # List of fake IP addresses
    ip_list = ["123.123.123.123", "124.125.126.127", "128.129.130.131"]
    # List of user agents
    user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)", "Mozilla/5.0 (Linux; Android 10)"]
    # List of referrers
    referrers = ["-", "http://www.example.com", "https://www.anotherdomain.com"]
    # List of resources
    resources = ["/index.html", "/about", "/contact", "/products", "/store"]
    # List of response codes
    response_codes = ["200", "404", "500", "301"]
    
    # Generate a random log entry
    ip = random.choice(ip_list)
    user_agent = random.choice(user_agents)
    referrer = random.choice(referrers)
    resource = random.choice(resources)
    response_code = random.choice(response_codes)
    # Current time in nginx log format
    current_time = time.strftime("%d/%b/%Y:%H:%M:%S +0000", time.gmtime())
    
    # Format the log entry similar to the common nginx log format
    log_entry = f'{ip} - - [{current_time}] "GET {resource} HTTP/1.1" {response_code} {len(resource)+random.randint(50, 1000)} "{referrer}" "{user_agent}"'
    
    return log_entry

# Example usage:
fake_log = generate_fake_nginx_log() + "\n"
for i in range(10):
    fake_log = fake_log + generate_fake_nginx_log() + "\n"
print(fake_log)
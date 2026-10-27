Here are **detailed Hinglish answers for Questions 20–30** (I’ll include 20 again briefly for continuity, then 21–30 in detail):

---

## 20) Pagination scraping kaise karoge?

**Answer:**

“Pagination ka matlab hota hai data multiple pages mein divided hona.

Example:

```bash
example.com/products?page=1
example.com/products?page=2
```

Agar URL-based pagination hai toh simple loop:

```python
for page in range(1, 100):
    url = f"https://example.com/products?page={page}"
```

Agar **Next button** hai:

Selenium / Playwright se click karenge.

Example:

```python
next_btn.click()
```

Agar **API-based pagination** hai:

```bash
/api/products?offset=0&limit=50
```

offset increase karenge.

Stop condition:

* next button disabled
* no more results
* empty API response”

---

## 21) Infinite scrolling website scrape kaise karoge?

**Answer:**

“Infinite scroll mein page dynamically scroll hone pe naya content load hota hai.

Approach:

### 1. Scroll using JS

```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```

Ye bottom tak scroll karega.

### 2. Wait for loading

```python
time.sleep(2)
```

ya explicit wait.

### 3. Compare page height

```python
last_height = driver.execute_script("return document.body.scrollHeight")
```

Then scroll.

Phir check:

```python
new_height = driver.execute_script("return document.body.scrollHeight")
```

Agar same hai → no more content.

Best approach:
Network tab inspect karo, hidden API mil sakta hai.

API mil gaya toh direct call better hai.”

---

## 22) Login-required website scrape kaise karoge?

**Answer:**

“Login-required site scrape karne ke multiple ways hain:

### 1. Form automation

Selenium/Playwright se username-password fill:

```python
driver.find_element(...).send_keys("email")
```

Then login button click.

---

### 2. Session cookies use karo

Ek baar login manually.

Cookies export kar lo.

Phir requests mein use karo.

Example:

```python
session.cookies.set("token", "abc")
```

---

### 3. Token-based auth

Agar API JWT token use karta hai:

```python
headers = {
    "Authorization": "Bearer token"
}
```

Then direct requests.

Secure aur fast.”

---

## 23) Cookies aur session handling kaise karte ho scraping mein?

**Answer:**

“Cookies small data hota hai jo browser store karta hai.

Example:

* session id
* auth token
* preferences

Session handling ke liye Python requests ka Session object use karte hain:

```python
import requests
session = requests.Session()
```

Benefits:

* cookies persist hoti hain
* headers persist hote hain
* login maintain rehta hai

Example:

```python
session.post(login_url, data=payload)
session.get(data_url)
```

Without session:
har request new user jaisa lagega.”

---

## 24) API mil jaye toh scraping karoge ya API use karoge? Kyun?

**Answer:**

“API use karungi.

Reasons:

### Faster

HTML parse nahi karna padta.

### Cleaner data

Structured JSON milta hai.

Example:

```json
{
 "name":"phone",
 "price":10000
}
```

### Less fragile

HTML structure change ho sakta hai.

API stable hota hai.

### Lower resource usage

Browser automation nahi chahiye.

Agar API protected ho ya incomplete ho tab scraping karungi.”

---

## 25) Agar HTML structure frequently change hota ho toh scraper reliable kaise banaoge?

**Answer:**

“Robust selectors use karungi.

Bad:

```xpath
/div[2]/div[3]/span
```

Good:

```xpath
//span[contains(@class,'price')]
```

Strategies:

### 1. Multiple fallback selectors

```python
try xpath
except use css
```

### 2. Config-based selectors

Selectors code mein hardcoded nahi.

JSON/config file mein store.

### 3. Monitoring

Agar extraction fail ho toh alert.

### 4. Automated tests

Regularly run scraper tests.”

---

## 26) Python mein multithreading aur multiprocessing mein difference?

**Answer:**

“Multithreading:

Ek process ke andar multiple threads.

Shared memory.

Best for I/O-bound tasks.

Example:

* downloading pages
* API calls

---

Multiprocessing:

Multiple independent processes.

Separate memory.

Best for CPU-bound tasks.

Example:

* image processing
* heavy parsing

Example:

```python
from multiprocessing import Process
```

Thread lightweight hota hai.

Process heavier hota hai.”

---

## 27) Python GIL kya hota hai?

**Answer:**

“GIL = Global Interpreter Lock.

Python CPython mein ek mechanism hai jo ensure karta hai ek time pe sirf ek thread Python bytecode execute kare.

Isliye multithreading CPU-bound tasks mein speedup nahi deta.

Example:

2 threads heavy calculation kar rahe hain.

Dono parallel nahi chalenge truly.

But I/O-bound mein useful hai because waiting time mein thread switch hota hai.

CPU-bound → multiprocessing better.”

---

## 28) Asyncio kya hota hai? Scraping mein kaise use kar sakte ho?

**Answer:**

“Asyncio Python ka asynchronous programming framework hai.

Ek single thread mein multiple tasks efficiently handle kar sakta hai.

Keywords:

```python
async
await
```

Example:

```python
async def fetch():
    await session.get(url)
```

Scraping mein useful for:

* multiple API calls
* high concurrency

Libraries:

* aiohttp
* httpx async

Benefit:

Less memory than threads.”

---

## 29) List comprehension aur generator mein difference?

**Answer:**

List comprehension:

Immediately memory allocate karta hai.

Example:

```python
nums = [x*x for x in range(1000)]
```

Generator:

Lazy evaluation.

Example:

```python
nums = (x*x for x in range(1000))
```

Difference:

List:

* fast access
* more memory

Generator:

* less memory
* iterate one by one

Large scraping datasets mein generator better.”

---

## 30) Exception handling kaise implement karoge scraper mein?

**Answer:**

“Scraper mein errors common hain:

* timeout
* connection error
* parsing error

Use try-except:

```python
try:
    scrape()
except Exception as e:
    print(e)
```

Specific exceptions better:

```python
except TimeoutException:
```

Retry mechanism:

```python
for i in range(3):
```

Logging:

```python
logging.error(e)
```

Finally block:

```python
driver.quit()
```

Production scraper should never crash because of one page.”

---

Ye questions strong kar le.

Agar interviewer ne GIL puch liya aur tune bola “Python fast hai sir” toh wahi reject karke next candidate ko `await` karenge 💀

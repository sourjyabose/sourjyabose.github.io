Here are **very detailed yet easy-to-understand Hinglish answers** for **Questions 30–40**, from a **female perspective** so you can speak naturally in interview.

---

## 30) Exception handling kaise implement karoge scraper mein?

**Answer:**

“Ma’am/Sir, scraping mein errors bahut common hote hain because hum external websites ke saath deal karte hain.

For example:

* Network issue
* Timeout
* Website structure change
* Element not found
* IP blocked

Agar exception handling nahi hoga toh scraper ek hi error pe crash ho jayega.

Main usually `try-except-finally` use karti hoon.

Example:

```python
try:
    data = scrape_page(url)
except Exception as e:
    print(e)
```

### Try block

Yaha risky code likhte hain.

### Except block

Agar error aaye toh usko catch karte hain.

Example:

```python
except TimeoutException:
```

Ya:

```python
except NoSuchElementException:
```

Specific exception use karna better hota hai.

### Finally block

Cleanup ke liye.

Example:

```python
finally:
    driver.quit()
```

Isse browser close ho jayega chahe error aaye ya na aaye.

Main logging bhi use karti hoon:

```python
logging.error(f"Failed {url}")
```

Aur retry mechanism bhi:

```python
for i in range(3):
```

3 attempts tak try karega.

Production scraper mein mera goal hota hai ki ek page fail ho toh pura scraper fail na ho.”

---

## 31) Decorator kya hota hai?

**Answer:**

“Decorator Python ka ek feature hai jo function ko modify karta hai without changing original code.

Simple words mein:

Ek wrapper function.

Example:

```python
def log_function(func):
    def wrapper():
        print("Running function")
        func()
    return wrapper
```

Use:

```python
@log_function
def scrape():
    print("Scraping...")
```

Output:

```python
Running function
Scraping...
```

Scraping mein use cases:

### Logging decorator

Kaunsa function kab run hua.

### Retry decorator

Agar fail hua toh automatically retry.

### Timing decorator

Kitna time laga.

Example:

```python
@retry
def fetch():
```

Ye code reusable aur clean banata hai.”

---

## 32) Lambda function kya hota hai?

**Answer:**

“Lambda ek anonymous function hota hai.

Anonymous matlab bina naam ka.

Syntax:

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x*x
```

Equivalent:

```python
def square(x):
    return x*x
```

Use cases:

Sorting:

```python
items.sort(key=lambda x: x["price"])
```

Mapping:

```python
map(lambda x:x*x, nums)
```

Filtering:

```python
filter(lambda x:x>10, nums)
```

Scraping mein useful hota hai data transform karne ke liye.

Lekin complex logic ke liye normal function better hota hai.”

---

## 33) Scraped data ko store kaise karoge? SQL ya NoSQL?

**Answer:**

“Depend karta hai data type pe.

Agar structured data hai:

Example:

* product name
* price
* category

Toh SQL.

Like MySQL / PostgreSQL.

Because:

* relations support karta hai
* queries powerful hoti hain

Example table:

| id | name | price |

Agar semi-structured ya dynamic data hai:

Example:

Different websites ka alag fields.

Toh NoSQL like MongoDB.

MongoDB JSON-like documents store karta hai.

Example:

```json
{
 "name":"phone",
 "price":1000
}
```

Agar temporary ya caching chahiye toh Redis.

Agar analytics ke liye huge data hai toh data warehouse.

Mostly main:

MongoDB for raw scraped data

MySQL for processed structured data.”

---

## 34) MongoDB vs MySQL?

**Answer:**

“MongoDB NoSQL hai.

MySQL relational SQL database hai.

### MySQL

Tables, rows, columns.

Schema fixed.

Example:

users table.

Advantages:

* ACID compliance
* joins
* structured data

### MongoDB

Collections aur documents.

Schema flexible.

Example:

```json
{
 "title":"Laptop",
 "price":50000
}
```

Advantages:

* flexible schema
* easy horizontal scaling

Agar e-commerce product scrape kar rahi hoon jahan fields vary karte hain → MongoDB.

Agar invoice system hai → MySQL.”

---

## 35) Redis kya hai aur cache ke liye kaise use hota hai?

**Answer:**

“Redis ek in-memory data store hai.

Bahut fast hota hai.

Uses:

### Cache

Frequently used data memory mein store.

Example:

Agar same page repeatedly scrape ho raha hai toh cache check karungi.

```python
redis.get(url)
```

Agar data mil gaya toh request nahi bhejungi.

---

### Message broker

Celery ke saath queue.

---

### Session store

User sessions.

---

### Rate limiting counters

Track request count.

Because Redis RAM mein hota hai, speed bahut high hoti hai.”

---

## 36) Duplicate data avoid kaise karoge?

**Answer:**

“Duplicate avoid karna important hai.

Methods:

### Unique key

Example:

Product URL unique.

Database mein unique index.

```sql
UNIQUE(url)
```

---

### Hashing

Content ka hash generate.

Same hash means duplicate.

Example:

MD5 / SHA.

---

### Upsert

Insert if not exists, otherwise update.

MongoDB:

```python
update_one(..., upsert=True)
```

---

### Pre-check

Insert se pehle database check.

Main mostly URL ya product ID use karti hoon.”

---

## 37) Large-scale scraped data ko process kaise karoge?

**Answer:**

“Large-scale data ko chunks mein process karungi.

Instead of memory mein sab load karne ke.

Example:

1000 rows at a time.

Use:

Pandas chunking:

```python
pd.read_csv(chunksize=1000)
```

Ya stream processing.

ETL pipeline banaungi:

Extract → Transform → Load

Distributed processing ke liye:

Apache Spark

Ya Celery workers.

Raw data alag store karungi.

Processed data alag.

Aur indexing use karungi fast queries ke liye.”

---

## 38) Agar 1 lakh pages scrape karne ho toh architecture kaise design karoge?

**Answer:**

“1 lakh pages ke liye simple script kaafi nahi hoga.

Scalable architecture design karungi.

### Step 1: URL producer

URLs generate karega.

---

### Step 2: Queue

Redis / RabbitMQ.

---

### Step 3: Workers

Multiple Celery workers parallel scraping.

---

### Step 4: Proxy rotation

IP ban avoid.

---

### Step 5: Retry system

Failed pages requeue.

---

### Step 6: Storage

MongoDB / SQL.

---

### Step 7: Monitoring

Logs, alerts.

Flow:

Producer → Queue → Worker → Database

Isse horizontal scaling possible hai.”

---

## 39) Agar scraper suddenly fail ho jaye production mein toh debugging kaise karoge?

**Answer:**

“Sabse pehle panic nahi karungi.

Step by step check karungi.

### Logs check

Error kya hai?

Example:

Timeout?

403?

Element not found?

---

### Website inspect

HTML change hua?

Captcha aaya?

---

### Proxy issue?

IP blocked?

---

### Network/API issue?

Server down?

---

### Reproduce locally

Same URL test karungi.

---

### Screenshot/save HTML

Selenium mein screenshot le sakti hoon.

```python
driver.save_screenshot()
```

Ya page source save.

Then fix and redeploy.”

---

## 40) Agar IP ban ho gaya toh kya karoge?

**Answer:**

“IP ban usually excessive requests ki wajah se hota hai.

Solutions:

### Proxy rotation

Har request different IP.

Residential proxies better.

---

### Slow down requests

Random delays.

```python
sleep(random.uniform(1,3))
```

---

### Rotate user agents

Different browser fingerprints.

---

### Session reuse

Har request new visitor jaisa na lage.

---

### Respect rate limits

Less aggressive scraping.

Agar permanent ban hai toh new proxy use karungi.”

---




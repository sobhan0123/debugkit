# debugkit


A tiny but powerful debugging helper for Python

DebugKit is a lightweight Python library that helps developers quickly inspect variables, trace execution, and measure function performance with clean, readable terminal output.

---

دیباگ‌کیت

یک ابزار کوچک ولی قدرتمند برای دیباگ در پایتون

DebugKit یک کتابخانه سبک برای پایتون است که به برنامه‌نویس‌ها کمک می‌کند متغیرها را سریع بررسی کنند، مسیر اجرای برنامه را ببینند و زمان اجرای توابع را اندازه‌گیری کنند؛ آن هم با خروجی مرتب و خوانا در ترمینال.

---

Features | قابلیت‌ها

English:
- Clean, structured debugging output
- Automatic variable name detection from the source line
- Show all local variables instantly with debug()
- Function execution tracing with @trace
- Function runtime measurement with @timer
- Colored and boxed terminal output
- Very lightweight and easy to plug into existing code

فارسی:
- خروجی مرتب و ساختاریافته برای دیباگ
- تشخیص خودکار نام متغیرها از روی خط کد
- نمایش همه متغیرهای محلی تنها با debug()
- نمایش مسیر اجرای توابع با @trace
- اندازه‌گیری زمان اجرای تابع با @timer
- خروجی رنگی و قاب‌دار در ترمینال
- بسیار سبک و قابل استفاده سریع در کدهای موجود

---

Installation | نصب

download repository 

cd debugkit--main


Local install:
pip install -e .

---

Installation on Linux and macOS | نصب در لینوکس و مک

English:
python3 --version
pip3 --version
pip3 install debugkit

git clone https://github.com/your-username/debugkit.git
cd debugkit
pip3 install -e .

(Optional)
python3 -m venv venv
source venv/bin/activate
pip install debugkit

فارسی:
python3 --version
pip3 --version
pip3 install debugkit

git clone https://github.com/your-username/debugkit.git
cd debugkit
pip3 install -e .

(اختیاری)
python3 -m venv venv
source venv/bin/activate
pip install debugkit

---

Usage | نحوه استفاده

Debug variables:
from debugkit import debug
x = 10
y = 20
debug(x, y)

Show all variables:
def compute():
    a = 1
    b = 2
    c = a + b
    debug()

compute()

Keyword mode:
debug(total=sum_value, count=n_items)

Trace:
from debugkit import trace
@trace
def add(a, b):
    return a + b
add(2, 3)

Timer:
from debugkit import timer
@timer
def slow():
    import time; time.sleep(1)
slow()

---

License | لایسنس

MIT License

---

Author | سازنده


Made for developers who want cleaner debugging with less noise.


-Sobhan

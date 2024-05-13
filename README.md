# BRUTFORCE

To check your website on brutforce attacks you can use this.

- If you want to test attack like a real one, then use a **VPN** to change your **IP**.
- Use **PROXIES** and ideally not free ones if possible, as these could save your data. But with VPN that doesn't matter, you can also use free proxies.
- The **USER AGENT** is also added and changed here.
- **Sessions** are also used to maintain the session.

If you don't use **PROXIES** and **VPNs**, your real information will be sent along.

However, you don't need to worry because you are testing your own website. It's about protecting your website against real attacks. 

But to simulate a real attack you should also consider **VPN** and **PROXIES**, because a real attacker will not do otherwise in order not to transmit his information and also bypass your blocks.

> The script for all possible combinations of letters, numbers and special characters. Starting with a.

# IMPORTANT NOTE

Using such extensive brute force methods can be very resource intensive, especially for longer passwords, as the number of combinations increases exponentially with the length of the password. 

> Use this approach wisely and ensure that your testing is ethical and legal, especially when conducted against systems you do not own.

# INSTALL PYTHON

https://www.python.org/

# INSTALL MODULES

Check if package is installed:

```bash
$ pip3 list
```

If not installed, install the packages:

```bash
$ pip3 install requests
```

```bash
$ pip3 install "requests[socks]"
```

```bash
$ pip3 install beautifulsoup4
```

# USAGE

Set your settings first and then start the script.

## SETTINGS

```python
EMAIL = "email@localhost"  # Set the email for login
LOGIN_URL = "http://localhost:8000/login/"  # Set the login page url
ERROR_DIV_CLASS = "error-message"  # Set the error message class name
MAX_PASS_LENGTH = 10
RESPONSE_DELAY = 1
DEBUG_FORM = True  # Set this to True to print form debugging information
DEBUG_FORM_LENGTH = 1000  # Set this to True to print form debugging information
```

### USER AGENT

If you use the script with user agent only.

USER AGENTS:

```python
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    # Add more user agents as needed
]
```

### PROXY

If you use the script with proxies and user agents.

HTTP PROXY:
```python
proxy_list = [
    {'http': 'http://proxy1:port', 'https': 'http://proxy1:port'},
    {'http': 'http://proxy2:port', 'https': 'http://proxy2:port'},
    {'http': 'http://proxy3:port', 'https': 'http://proxy3:port'},
    # Add more proxies as needed
]
```

OR SOCKS PROXY:
```python
proxy_list = [
    {'http': 'socks5://proxy1:port', 'https': 'socks5://proxy1:port'},
    {'http': 'socks5://proxy2:port', 'https': 'socks5://proxy2:port'},
    {'http': 'socks5://proxy3:port', 'https': 'socks5://proxy3:port'},
    # Add more proxies as needed
]
```

## START

Start the brutforce:

```bash
$ python3 bruteforce.py
```

Output

```bash
/*-------------------------------------------------------------------------------------*/
/*                                  BRUTEFORCE ATTACK                                  */
/*-------------------------------------------------------------------------------------*/
/*                          Don't use for illegal activities                           */
/*-------------------------------------------------------------------------------------*/

Test combination: admin a
Status Code: 200, Final URL: http://localhost/user/login/

...

Test combination: adm0\
Test combination: adm0]
Test combination: adm0^
Test combination: adm0_
Test combination: adm0`
Test combination: adm0{
Test combination: adm0|
Test combination: adm0}
Test combination: adm0~
Test combination: adm1!
Test combination: adm1"
Test combination: adm1#

/*-------------------------------------------------------------------------------------*/
/*                                   PASSWORD FOUND                                    */
/*-------------------------------------------------------------------------------------*/
/*     Time (ms)      |        Tries        |        Name         |      Password      */
/*      1322.645      |       454533        |        admin        |       adm1#        */
/*-------------------------------------------------------------------------------------*/
```

If you debug the form, you will also see the form in the output

```bash
<form method="post" action="http://localhost/user/login/">
    <input type="email">
    <input type="password">
    <input type="submit">
</form>
```

# Information

## What does a VPN do?
A VPN creates a secure, encrypted connection between your device and a server operated by the VPN provider. Below are some key points about VPNs:

- **Encryption**: VPNs encrypt all of your internet traffic, meaning everything you send and receive is protected and cannot be seen or manipulated by anyone along the way.
- **IP Hide**: Similar to a proxy, a VPN replaces your IP address with that of the VPN server. Websites and online services only see the IP address of the VPN server.
- **Bypass geo-blocking**: VPNs are effective at bypassing geo-restrictions because they allow you to choose the location of the server you are connecting from.
- **Security on public networks**: VPNs are particularly useful for protecting your data on public and unsecure networks (like public Wi-Fi).

## What does a proxy do?
A proxy server acts as an intermediary between your device and the internet. When you send a request through a proxy, your request first goes to the proxy server, which then forwards the request to the destination on your behalf. Here are some key aspects of proxies:

- **IP Hide**: Your actual IP address will be replaced with the proxy server’s IP address. Websites see the proxy's IP address and not your own.
- **No encryption**: Most standard proxy servers do not encrypt your traffic. This means that information transmitted between your device and the proxy server could be viewed by third parties unless it is otherwise encrypted.
- **Different types**:
    - **HTTP Proxy**: Suitable for web browsing.
    - **SOCKS Proxy**: More flexible and compatible with all types of internet traffic, but slower.
    - **Transparent proxies**: They don't actually hide your IP address and are often used in businesses and educational institutions to monitor or filter internet traffic.

# ISSUE

Please use the issue tab to request a:

* Bug
* Feature

Choose template and report a bug or feature you want [issues](https://github.com/prod3v3loper/bruteforce/issues).

# CONTRIBUTE

Please read the [contributing](https://github.com/prod3v3loper/bruteforce/blob/master/.github/CONTRIBUTING.md) to contribute.

# VULNERABILITY

Please use the Security section for privately reporting a [vulnerability](https://github.com/prod3v3loper/bruteforce/security).

# AUTHOR

[prod3v3loper](https://www.prod3v3loper.com)

# License

[MIT](https://github.com/prod3v3loper/php-mvc-professional/blob/master/LICENSE)
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="images/logo.png" alt="Logo" width="80" height="80">

  <h3 align="center">Instagram Comments Crawler</h3>

  <p align="center">
    Collect all comments and replies on an instagram post. And pick randomly winners of an event.
    
  <a href="https://youtu.be/P7g2c4UMUHs">View Demo Video</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This is developed for collecting all comments of an instagram post and picking randomly winners of an event.

### 👀 Features

- Save comments of an instagram post to CSV file.
- Pick winners and save their account and student ID to CSV file. (_Optional_)
- Automatically download chrome driver.

<p align="right">(<a href="#top">back to top</a>)</p>

### ⚙️ Built With

- Python
- Selenium

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 🚀 Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

- Download Chrome Browser (**Not Chrome Driver**)
- Chrome Driver will be downloaded automatically.

### Installation

1. Create a virtual environment

   ```bash
   python -m venv [venv]
   ```

2. Activate virtual environment

   ```bash
   # For Windows
   source [venv]/scripts/activate
   # For Mac or Linux
   source [venv]/bin/activate
   ```

3. Install pip packages
   ```bash
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## 🔑 Usage

- `ChromeDriver` in `driver.py` is a customized version of Selenium webdriver.
  So some function of original webdriver is not available.

  ```python
  from driver import ChromeDriver
  driver = ChromeDriver()
  ```

- Details of customized setting

  - `user-agent` : randomly changed when launching script.
  - `auto download chrome driver` : automatically download chrome driver compatible with chrome browser installed.
  - Default download path
    ```bash
    # For windows
    C:/Program Files/chrome or C:/Program Files (x86)/chrome
    # For Mac
    /usr/bin/chrome
    ```

- It is necessary to login to access an instagram post. User account and password are entered on terminal. Password will be hided by `getpass` when entering input.

  ```python
  import getpass
  driver.move_to_login_page()

  username = input("Input ID : ")
  password = getpass.getpass("Input Password :")

  # For only personal usage, you can just put raw data.
  # username = "instagram_account"
  # password = "password"

  driver.login_to_instagram(username, password)
  ```

- Set an instagram post url to `target_url`

  ```python
  target_url = "https://www.instagram.com/p/..."
  driver.get(target_url)
  ```

- Load all comments and replies.

  ```python
  driver.load_all_comments()
  driver.load_all_replies()
  ```

- Save all comments and replies to CSV file. It will be saved to `comments_{yyyy_mm_dd_hh_mm_ss}.csv`

  ```python
  driver.collect_comments()
  ```

- Close chrome driver at the end of script.
  ```python
  driver.close()
  ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## 📮 Contact

Email - joonhyuk.han@kakao.com

<p align="right">(<a href="#top">back to top</a>)</p>

# Instagram comment crawler
This program is developed for the [MJU_NAEIL](https://www.instagram.com/mju_naeil/) event(2020.05). <br>

Below is what this program can do : <br>
<ul>Collect all comments in a specific instagram post</ul>
<ul>Pick up winners </ul>

## Requirements

```
Python Selenium
Google Chorme Browser
Google Chromedriver (version check is necessary with Chorme browser) 
```

## What's Inside?

### Counting the number of clicking
To collect all comments in a instagram post, we need to click plus button until it is unavailable.<br>
So this program finds plus button by using "find_element_by_css_selector".
```
클릭을 1 번 했습니다.
클릭을 2 번 했습니다.
클릭을 3 번 했습니다.
클릭을 4 번 했습니다.
...
답글 불러오기 완료
```
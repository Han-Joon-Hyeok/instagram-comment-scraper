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

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

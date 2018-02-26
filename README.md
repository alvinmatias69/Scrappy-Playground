# Scrapy Playground

A playground for web scraping using Scrapy from python package.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Before using this playground your system needs to have following software installed.

1. [Python 2.7](https://www.python.org/downloads/release/python-2713/)
2. [PIP](https://pypi.python.org/pypi/pip)
3. [Scrapy](https://docs.scrapy.org/en/latest/)

### Installing

Make sure you have [git](https://git-scm.com/download) installed on your machine.

Clone this project

```
git clone https://github.com/alvinmatias69/Scrappy-Playground.git
```

And that's it, you're ready to go.

## Spiders

Spider is a class instance used in Scrapy to scraping a page. More information at Scrapy [documentation](https://docs.scrapy.org/en/latest/topics/spiders.html)

### Running

To run a crawler simply run

```
scrapy crawl <spider name> [arguments]
```

Common argument used are `-o` for setting output file and `-a` for setting spider arguments.

example
```
scrappy crawl example -o exampleOutput.json -a date=02/27/2018
```

more on Scrapy [commmands](https://docs.scrapy.org/en/latest/topics/commands.html)

### List

List of available spider crawler on this project.

#### Detik

Crawler for [Detik News](https://news.detik.com). Get all news title from the web.

##### Params

* date [`mm/dd/yyyy`]

Date when news will be crawled, default to `02/26/2018`

##### Example

```
scrappy crawl detik -o detikOutput.json -a date=02/27/2018
```

## Authors

* **Matias Alvin** - [alvinmatias69](https://github.com/alvinmatias69)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Hat tip to Scrapy developers for it's amazing library

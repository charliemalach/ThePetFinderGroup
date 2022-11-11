# The PetFinder Group

A Command Line Tool created to help users find cats up for adoption. 

Written as part two of an interview with The PathFinder Group by Charlie Malachinski. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Installation

Make sure that you have all the [requirements](requirements.txt) installed. 

A step by step guide that will tell you how to get the development environment up and running.

```
$ Run 'server-run.bat' to connect JSON to endpoint.
$ Open Command Prompt or Terminal and navigate to install location. 
$ Use command 'python main.py --help' to see list of all commands. 
```

## Usage

A few examples of useful commands and/or tasks.

```
$ python main.py list --> shows a list of all available cats 
$ python main.py age --> shows a filter list of cats based on age argument
$ python main.py gender --save --> shows a filter list of cats based on gender argument and prompts user to save results as a CSV
```


## Additional Documentation and Acknowledgments

* Implements [ JSON-SERVER ](https://www.npmjs.com/package/json-server)to mock test rest server. 
* Implements [Click](https://click.palletsprojects.com/en/8.1.x/) for commands and options. 
* Implements [Requests](https://requests.readthedocs.io/en/latest/) for HTTP methods.
* Implements [Pandas](https://pandas.pydata.org/) for JSON, CSV, and DataFrame compatibility. 

# WhatsApp Data Extractor 

<!-- Include Github badges here (optional) -->
<!-- e.g. Github Actions workflow status -->

In collaboration with the [Human Data Science group](https://hds.sites.uu.nl) and [Eyra](https://eyra.co), we developed scripts
to make WhatsApp data packages easily accessible to researchers. 

The main goal is that respondents can voluntarily donate their data 
download packages through an online platform (PORT), and researchers can provide custom data extraction scripts, which will be run locally on the respondent’s devices. 
The [port-poc](https://github.com/eyra/port-poc) has been developed by Eyra, while WhatsApp data extraction scripts were provided by the Soda team.

This project consists of two main scripts for extracting information from WhatsApp group chats and WhatsApp account data.

##Todo how to download data download package from whatsapp?
Whatsapp data packages can be requested via the whatsapp account ...
## How it works
The extraction logic is placed in the process function within data_extractor/[whatsapp_chat or whatsapp_account_info]/__init__.py which follows the template format of PORT.

The main function in these scripts is process() which takes .txt and .zip files as input.


## Usage

<!-- We should add here -->
- Install Poetry:
```pip install poetry
```
- install the required python packages :
``` poetry install
```

The behavior of the process function can be verified by running the tests. The test are located in the tests folder.
To run the tests
```
poetry run pytest
```

To extract data from Whatsapp data packages from the browser run the following code from the project root folder (the one with .git):

```
python3 -m http.server
```

This will start a webserver on: localhost. Opening a browser with that URL will initialize the application. After it has been loaded a file can be selected. The output of the process function will be displayed after a while (depending on the amount of processing required and the speed of the machine)

Data is processed locally. 
Security is preserved.
The following is the image of the extracted data

<img src="man/resources/output.png" alt="output" width="250px"/>
In case of agreement, donator can donate the extracted information

### Built with

- [python3](https://www.python.org/download/releases/3.0/), [pyodide](https://pyodide.org/en/stable/)

## Contributing

Contributions are what make the open source community an amazing place
to learn, inspire, and create. Any contributions you make are **greatly
appreciated**.

Please refer to the
[CONTRIBUTING](https://github.com/sodascience/osmenrich/blob/main/CONTRIBUTING.md)
file for more information on issues and pull requests.


<!-- Do not forget to also include the license in a separate file(LICENSE[.txt/.md]) and link it properly. -->
### License

The code in this project is released under [MIT license](LICENSE.md).

<!-- CONTACT -->

## Contact

**WhatsApp Data Extractor** is project by [Human Data Science group](https://hds.sites.uu.nl).
The technical implementation is provided by the [ODISSEI Social Data
Science (SoDa)](https://odissei-data.nl/nl/soda/) team.

Do you have questions, suggestions, or remarks on the technical implementation? File an issue in the
issue tracker or feel free to contact [Parisa Zahedi](https://github.com/parisa-zahedi) or [Shiva Nadi](https://github.com/shNadi)

<img src="man/resources/word_colour-l.png" alt="SoDa logo" width="250px"/> 

Project Link: [https://github.com/sodascience/port-whatsapp-datadonation](https://github.com/sodascience/port-whatsapp-datadonation)



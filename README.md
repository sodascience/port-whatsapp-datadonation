# WhatsApp Data Extractor 

<!-- Include Github badges here (optional) -->
<!-- e.g. Github Actions workflow status -->

WhatsApp datadonation script is developted by SoDa team in collaboration with the [Human Data Science group](https://hds.sites.uu.nl) and [Eyra](https://eyra.co). This project is a part of [Data Donation project](https://github.com/eyra/port-poc) that makes the information extracted from the WhatsApp Data Download packages(DDPs) accessible to the researchers for further analysis while preserving the the privacy of the datadonators. 

## WhatsApp data donation process

Participants can voluntary donate their whatsapp data for research purposes. 
1. Make a request for your WhatsApp DDPs through the whatsapp application (on group/account level)
2. Download the data package on your local storage.
3. Login to Eyra environement and select your data package. Please keep in your mind that data extraction and anonymization processes run locally on your browser. It means you have not shared any data yet.
4. Review the extracted data and donate it in case of agreement.

## Data Extraction overview

This project consists of two main scripts for extracting information from WhatsApp group chats and WhatsApp account data.
The extraction logic is placed in the process function within data_extractor/[whatsapp_chat or whatsapp_account_info]/__init__.py which follows the template format of PORT. More information about collaboration with PORT can be found in this [tutorial]().

The script runs through an online platform called port:
- [Group level](https://next.dev.eyra.co/data-donation/flow/5?session[participant]=test)
<img src="img/resources/whatsapp-chat1.png" alt="output" width="600px"/>
<img src="img/resources/whatsapp-chat2.png" alt="output" width="600px"/>
<img src="img/resources/whatsapp-chat3.png" alt="output" width="600px"/>

- [Account level](https://next.dev.eyra.co/data-donation/flow/6?session[participant]=test)
<img src="img/resources/account-info.png" alt="output" width="600px"/>

## Usage

<!-- We should add here -->
- Install Poetry:
```
pip install poetry
```
- install the required python packages :
```
poetry install
```

The behavior of the process function can be verified by running the tests. The test are located in the tests folder.
To run the tests
```
poetry run pytest
```

### Built with

- [python3](https://www.python.org/download/releases/3.0/)
-  [pyodide](https://pyodide.org/en/stable/)


### License

The code in this project is released under [MIT license](LICENSE.md).

<!-- CONTACT -->

## Contact

**WhatsApp Data Extractor** is project by [Human Data Science group](https://hds.sites.uu.nl).
The technical implementation is provided by the [ODISSEI Social Data
Science (SoDa)](https://odissei-data.nl/nl/soda/) team.

Do you have questions, suggestions, or remarks on the technical implementation? File an issue in the
issue tracker or feel free to contact [Parisa Zahedi](https://github.com/parisa-zahedi) or [Shiva Nadi](https://github.com/shNadi)

<img src="img/resources/word_colour-l.png" alt="SoDa logo" width="250px"/> 

Project Link: [https://github.com/sodascience/port-whatsapp-datadonation](https://github.com/sodascience/port-whatsapp-datadonation)



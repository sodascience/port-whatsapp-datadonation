# WhatsApp Data Extractor 

<!-- Include Github badges here (optional) -->
<!-- e.g. Github Actions workflow status -->

In collaboration with the [Human Data Science group](https://hds.sites.uu.nl) and [Eyra](https://eyra.co), we developed WhatsApp data extractor scripts
to make the information extracted from the WhatsApp Data Download packages(DDPs) accessible to the researchers for further analysis while preserving the the privacy of the datadonators. 

# How WhatsApp data donation works

Participants can voluntary donate their whatsapp data for research perposes. 
- DDPs can be requested by participants through the whatsapp application (on group/account level)
- DDPs can be stored on participants local storage
- Data extraction and anonymization processes run locally on participants browser using pyodide technology
- Extracted data can be donatated after being reviewed and approved by the participants 

This project consists of two main scripts for extracting information from WhatsApp group chats and WhatsApp account data.
The extraction logic is placed in the process function within data_extractor/[whatsapp_chat or whatsapp_account_info]/__init__.py which follows the template format of PORT. More information about collaboration with PORT can be found in this [tutorial]().

The script can be tested through an online platform called port-poc.We provide two levels of data extraction:
- [Group level](https://next.dev.eyra.co/data-donation/flow/5?session[participant]=test)
- [Account level](https://next.dev.eyra.co/data-donation/flow/6?session[participant]=test)


## Usage

The behavior of the process function can be verified by running the tests. The test are located in the tests folder.
To run the tests
```
poetry run pytest
```

The following is the image of the extracted data

<img src="img/resources/output.png" alt="output" width="250px"/>
In case of agreement, donator can donate the extracted information

### Built with

- [python3](https://www.python.org/download/releases/3.0/), [pyodide](https://pyodide.org/en/stable/)


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



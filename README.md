# Product Props Roadmapper

**A lightweight, interactive product roadmap visualization tool built with Streamlit.**

Product Props Roadmapper turns roadmap data into an interactive visual roadmap that makes it easier to communicate **what is being worked on, when, and how the work is organized**.

It is designed for product managers and product teams who want a simple way to transform roadmap data into something that is easier to explore, discuss, and share — without requiring a dedicated roadmap management platform.

## What It Does

Product Props Roadmapper takes structured roadmap data from a CSV file and turns it into an interactive roadmap visualization.

The tool supports:

* 📅 **Timeline-based roadmap visualization**
* 🔎 **Interactive filtering**
* 🗂️ **Flexible grouping and organization**
* ↕️ **Sorting of roadmap items**
* 📊 **Visualization of roadmap work across time**
* 📄 **CSV-based data input**
* 🖥️ **Interactive Streamlit interface**

The goal is not to replace a product management system. Instead, Roadmapper provides a lightweight visualization layer that can help product teams **see and communicate their roadmap more effectively**.

## Why Roadmapper?

Roadmaps are often maintained as spreadsheets, project-management data, or product-planning artifacts that are useful to the people maintaining them but difficult for everyone else to understand.

Roadmapper is intended to make that information more accessible.

Instead of asking stakeholders to interpret rows and columns, you can provide an interactive visual representation of the same underlying roadmap data.

## Getting Started

### Requirements

You will need:

* Python 3.x
* Streamlit
* The Python packages listed in `requirements.txt`

### Installation

Clone the repository:

```bash
git clone https://github.com/ggelsinon/Roadmapper.git
cd Roadmapper
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### Run the Application

Launch the Streamlit application:

```bash
streamlit run PP_Roadmap.py
```

Streamlit will provide a local URL where you can open the Roadmapper interface in your browser.

## Roadmap Data

Roadmapper currently uses a CSV file as its data source.

A sample dataset is included in the repository:

```text
PP Roadmap Sample Data.csv
```

You can use this file to explore the application and understand the expected structure of the roadmap data.

The roadmap visualization uses fields in the dataset to determine things such as:

* Roadmap item
* Start timing
* End timing
* Grouping
* Categorization
* Sorting
* Other attributes used by the visualization

The exact fields and supported values are best understood by looking at the included sample dataset.

## Project Structure

```text
Roadmapper/
│
├── PP_Roadmap.py
│   Main Streamlit application
│
├── PP Roadmap Sample Data.csv
│   Sample roadmap dataset
│
└── requirements.txt
    Python dependencies
```

## Who Is This For?

Roadmapper is particularly useful for:

* Product managers
* Product operations teams
* Product leaders
* Agile teams
* Program and portfolio managers
* Anyone who needs to communicate a product roadmap visually

It can be especially useful when you have roadmap information already stored in a spreadsheet or CSV but want a more engaging way to explore and present it.

## Open Source

Roadmapper is an open-source project from **Product Props**.

The project is intended to be useful, understandable, and adaptable. If you have ideas for improvements, find a bug, or want to extend the tool, contributions and feedback are welcome.

## Contributing

Interested in improving Roadmapper?

A simple contribution workflow is:

1. Fork the repository.
2. Create a branch for your change.
3. Make your changes.
4. Test the application locally.
5. Submit a pull request.

For larger changes, opening an issue first can help discuss the proposed approach before significant development work begins.

## Ideas for Future Development

Roadmapper is an evolving project. Potential future enhancements may include:

* Additional visualization options
* More flexible roadmap configuration
* Additional filtering capabilities
* Improved data validation
* Additional export options
* More customization of roadmap appearance
* Support for additional data sources

These are possibilities rather than commitments; the project will evolve based on practical use and feedback.

## About Product Props

**Product Props** is a collection of practical tools, resources, and ideas for product management.

The goal is simple:

> **Make product management practice more useful, more accessible, and a little less complicated.**

Roadmapper is one of those tools.

---

## License

This project is currently published as an open-source project. See the repository's license information for the terms under which the software may be used, modified, and distributed.

---

**Built with Python and Streamlit.**

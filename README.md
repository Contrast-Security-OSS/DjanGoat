# DjanGoat

DjanGoat is a vulnerable Django Application based in large part off the [RailsGoat](https://github.com/OWASP/railsgoat) project. The application purports to be an internal employee portal for MetaCorp, Inc but includes vulnerabilities from the [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project) and is intended to be used as an educational tool for developers and security professionals.

## Installation

On a mac, first install python.

### Quickstart

```
    make
```
When it's running, click [here!](http://127.0.0.1:8000/) Emails sent by the app will print to the console controlling the process.

If you get an error about not having pip, do this:

```
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    sudo python get-pip.py
```

### Initial Setup

Requirements:

 - Python 2.7
 - Pip

To set it all up and activate your virtualenv:
```
    make install
    source env/bin/activate
```

### Running

To run the server:
```
    make run
```

When it's running, click [here!](http://127.0.0.1:8000/)

### Resetting

If something went wrong and you want to start fresh:
```
    make clean
    make install
    make run
```

### Email

Emails sent by the app will print to the console controlling the process, both headers and body.

### Linting

To run `pylint` using the provided `.pylintrc` configuration file:
```
    make lint
```

## Tutorial
Tutorial information on the various vulnerabilities in this application are [here](docs/home.md).

## Acknowledgements
The development [team](docs/acknowledgements.md).

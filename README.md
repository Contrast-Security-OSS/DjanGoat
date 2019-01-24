# DjanGoat

DjanGoat is a vulnerable Django Application based in large part off the [RailsGoat](https://github.com/OWASP/railsgoat) project. The application purports to be an internal employee portal for MetaCorp, Inc but includes vulnerabilities from the [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project) and is intended to be used as an educational tool for developers and security professionals.

## Installation

On a mac, first install python.

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
    make install
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

If you did something in the app that would lead you to expect it to send email, you will find the full contents of that email output to the console controlling the server process.

### Linting

To run `pylint` using the provided `.pylintrc` configuration file:
```
    make lint
```

## Tutorial
Tutorial information on the various vulnerabilities in this application are [here](docs/home.md).

## Acknowledgements
The development [team](docs/acknowledgements.md).

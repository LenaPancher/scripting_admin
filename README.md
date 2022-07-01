# Scripting Admin

This repo contains every python projects made for the scripting admin course in Coding Factory Cergy.

## Installation

You need to make sure to use at least python 3 to be able to run this project.

```bash
$ python3 -V
```

## Usage

### leap_year

Allows to know if a year is leap year or not.

```bash
$ python3 "name_of_file.py"
```

### base64

Allows you to encode and decode a character string.

You can all the available arguments with :

```bash
$ python3 "base64_cli.py" --help
```

- Encode :

Example : Encode a string, display it in a .txt file with a logging level (ex: INFO)

```bash
$ python3 "base64_cli.py" encode -s "your_string" -o "name_of_file.txt" -l "logging_level"
```

- Decode :

Example : Decode a string, display it in a .txt file with a logging level (ex: INFO)

```bash
$ python3 "base64_cli.py" decode -s "your_string" -o "name_of_file.txt" -l "logging_level"
```

### supervision

Allows you to check the proper functioning of a system or service and to automatically send alerts to administrators.

You can all the available arguments with :

```bash
$ python3 "administration.py" --help
```

```bash
$ python3 "administration.py" -i "your_interval_in_second"
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors and acknowledgment

Show your appreciation to those who have contributed to the project.

LÉNA PANCHER, MOÏSE NSINGI, LUCAS GAUVAIN

## License

[MIT](https://choosealicense.com/licenses/mit/)
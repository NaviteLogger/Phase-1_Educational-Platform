# Educational Platform

A place where everyone can learn programming and topics related to IT.

## Table of Contents

- [Educational Platform](#educational-platform)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)
  - [Acknowledgements](#acknowledgements)

## About

This project is a web application that allows users to learn programming and topics related to IT. The application is divided into two parts: the first part is the learning platform, where users can learn programming and IT topics, and the second part is the social platform, where users can share their knowledge and experience with other users.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)
- [MySQL](https://dev.mysql.com/downloads/installer/)

### Installation

1. Clone the repo

```sh
git clone https://github.com/NaviteLogger/EducationalPlatform.git
```

2. Install Python packages

```sh
pip install -r requirements.txt
```

3. Create a database

```sh
mysql -u root -p
```

```sql
CREATE DATABASE educational_platform;
```

4. Create a `.env` file in the root directory and add the following lines

```sh
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_HOST=your_host
DB_NAME=educational_platform
DB_PORT=your_port
```

5. Run the application

```sh
python run.py
```

## Usage

1. Open your browser and go to `http://localhost:5000/`

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the project

2. Create your feature branch

```sh
git checkout -b feature/AmazingFeature
```

3. Commit your changes

```sh
git commit -m 'Add some AmazingFeature'
```

4. Push to the branch

```sh
git push origin feature/AmazingFeature
```

5. Open a pull request

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Contact

- [Email](mailto:kacprzakmarek92@gmail.com)

## Acknowledgements
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
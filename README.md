<!--
HOW TO USE:
This is an example of how you may give instructions on setting up your project locally.

Modify this file to match your project and remove sections that don't apply.

REQUIRED SECTIONS:
- Table of Contents
- About the Project
  - Built With
  - Live Demo
- Getting Started
- Authors
- Future Features
- Contributing
- Show your support
- Acknowledgements
- License

After you're finished please remove all the comments and instructions!
-->

<!-- <div align="center">
  <!-- You are encouraged to replace this logo with your own! Otherwise, you can also remove it. -->
  <!-- <img src="https://user-images.githubusercontent.com/86473715/208989298-61c26953-a6ea-4543-9250-465e28dd057a.png" alt="logo" width="140"  height="auto" />
  <br/> -->

<!-- TABLE OF CONTENTS -->

<div id="readme-top"></div>

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
  - [🚀 Live Demo](#live-demo)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Install](#install)
  - [Usage](#usage)
  - [Run tests](#run-tests)
  - [Deployment](#triangular_flag_on_post-deployment)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [🤝 Contributing](#contributing)
- [⭐️ Show your support](#support)
- [🙏 Acknowledgements](#acknowledgements)
- [❓ FAQ](#faq)
- [📝 License](#license)


<!-- PROJECT DESCRIPTION -->

# 📖 HubSpot <a id="about-project"></a>
 **HubSpot** is a real-time chat application using Django and Python, inspired by Discord. This project aims to replicate some of the key features of Discord, allowing users to create and join chat rooms, send and receive messages in real time, and manage user accounts. Implemented text messaging, user authentication, roles, and permissions.

<a name="readme-top"></a>

## 🛠 Built With <a id="built-with"></a>
- Django

### Tech Stack <a id="tech-stack"></a>
- Python
- Django
- Django-rest-framework

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://djangoproject.com/">Django</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
  </ul>
</details>

<!-- Features -->
### Key Features <a id="key-features"></a>

- **Users can create a room and discuss with others**
- **Users can connect with friends**
- **Hosts can create, delete, and update their rooms and messages**
- **Users can check recent activities in the room**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LIVE DEMO -->
## 🚀 Live Demo <a id="live-demo"></a>
Not Available yet!

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- GETTING STARTED -->

## 💻 Getting Started <a id="getting-started"></a>
To get a local copy up and running, follow these steps.

### Prerequisites

To run this project you need:

- to have [Python](https://python.org/) installed on your machine
- to have [PostgreSQL](https://www.postgresql.org/) installed on your machine
### Setup

To get a local copy up and running follow these simple example steps.

1. Navigate to a folder where you want the cloned file to appear

2. Clone this repo in your terminal or git bash using the command
```sh
  cd HubSpot
  git clone https://github.com/degisew/HubSpot.git
```

3. Run the following command to install all the necessary dependencies

 ```sh
  cd HubSpot
  pip install pipenv
  pipenv install    # This will create a virtual env't and install dependencies in the virtual env't.
``` 

4. Navigate to the folder called HubSpot/ and open this project using your editor

### Usage
To run the project, first activate your virtual environment:
```sh
  pipenv shell
```

Once you have activated, execute the following command to run the server:

```sh
cd HubSpot

For Mac/Linux run:
 python3 manage.py runserver

For Windows run:
 python manage.py runserver
```
- This above command will start the Django server in your browser

It runs the app in the development mode.\
Open [http://localhost:8000](http://localhost:8000) to view it in your browser.

### Deployment

You can deploy this project using:

- pythonanywhere
- Heroku
- Renderer

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- AUTHORS -->

## 👥 Authors <a id="authors"></a>

👤 **Degisew**

- GitHub: [degisew](https://github.com/degisew)
- LinkedIn: [Degisew](https://linkedin.com/in/degisew-mengist)
- Twitter: [@Dj_etiya](https://twitter.com/DJ_etiya)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a id="future-features"></a>

- Deploy and expose to the public

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a id="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/degisew/HubSpot/issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a id="support"></a>

If you like this project give a ⭐️ to repo.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a id="acknowledgements"></a>

I want to thank all my supporters.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->

## 📝 License <a id="license"></a>

This project is [MIT](https://github.com/degisew/HubSpot/blob/dev/LICENSE) licensed.

_NOTE: we recommend using the [MIT license](https://choosealicense.com/licenses/mit/) - you can set it up quickly by [using templates available on GitHub](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository). You can also use [any other license](https://choosealicense.com/licenses/) if you wish._

<p align="right">(<a href="#readme-top">back to top</a>)</p>

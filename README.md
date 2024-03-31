<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">PERSPECTIFY</h1>
</p>
<p align="center">
    <em>A new era of book reading and sharing motivation...</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/prathampt/perspectify?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/prathampt/perspectify?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/prathampt/perspectify?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/prathampt/perspectify?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with these software and tools:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Django-092E20.svg?style=flat&logo=Django&logoColor=white" alt="Django">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running perspectify](#-running-perspectify)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

This website is made for giving people a daily boost of motivation...

---

##  Features

This is entirely made using a framework of python Django, and styled using CSS only...

---

##  Repository Structure

```sh
└── perspectify/
    ├── LICENSE
    ├── README.md
    ├── core
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_delete_userprofile.py
    │   │   ├── 0003_initial.py
    │   │   ├── 0004_remove_userprofile_place_userprofile_email_and_more.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── signals.py
    │   ├── static
    │   │   └── core
    │   │       ├── about.css
    │   │       ├── contact.css
    │   │       ├── privacy_policy.css
    │   │       ├── profile.css
    │   │       └── styles.css
    │   ├── templates
    │   │   └── core
    │   │       ├── about.html
    │   │       ├── base.html
    │   │       ├── contact.html
    │   │       ├── login.html
    │   │       ├── privacyPolicy.html
    │   │       ├── profile.html
    │   │       └── signup.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── items
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── data
    │   │   └── .trackme
    │   ├── forms.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_remove_book_category_delete_category.py
    │   │   ├── 0003_alter_book_genre.py
    │   │   ├── 0003_alter_book_genre_savebook_delete_userbook.py
    │   │   ├── 0004_merge_20240310_1927.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── randomImages
    │   │   └── .trackme
    │   ├── scripy.py
    │   ├── static
    │   │   └── items
    │   │       ├── book.css
    │   │       ├── bookList.css
    │   │       ├── bookShelf.css
    │   │       ├── card.css
    │   │       └── styles.css
    │   ├── templates
    │   │   └── items
    │   │       ├── base.html
    │   │       ├── books.html
    │   │       ├── detail.html
    │   │       └── forms.html
    │   ├── templatetags
    │   │   ├── __init__.py
    │   │   └── custom_filters.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    ├── perspectify
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── requirements.txt
```

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.10`

###  Installation

1. Clone the perspectify repository:

```sh
git clone https://github.com/prathampt/perspectify
```

2. Change to the project directory:

```sh
cd perspectify
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running perspectify

Use the following command to run perspectify:

```sh
python main.py
```

##  Contributing

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/prathampt/perspectify
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b dev_yourname
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>


##  Acknowledgments

### Contributors:

[<img src="https://github.com/prathampt.png" width="60px;"/><br /><sub>Pratham Tandale</sub><br/>](https://github.com/prathampt/)
[<img src="https://github.com/anjali04tekam.png" width="60px;"/><br /><sub>Anjali Tekam</sub><br/>](https://github.com/anjali04tekam)
[<img src="https://github.com/Mehmood-Deshmukh.png" width="60px;"/><br /><sub>Mehmood Deshmukh</sub><br/>](https://github.com/Mehmood-Deshmukh)


---

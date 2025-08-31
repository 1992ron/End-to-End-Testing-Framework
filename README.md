# Full Stack Automation Project

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()  
[![Coverage](https://img.shields.io/badge/coverage-85%25-yellowgreen)]()  
[![Allure Report](https://img.shields.io/badge/allure-report-blue)]()

**Supported Platforms:** Web • Mobile • API • Database • Desktop • Electron

End-to-end, multi-platform test automation framework covering:  
**Web UI** • **Mobile UI** • **API** • **Database** • **Desktop App** • **Electron App**

## About

This project demonstrates a smart, modular automation infrastructure in six “Flows” layers—Web, Mobile, API, DB, Desktop, Electron—wrapped in a unified POM + Actions + Verifications. Tests read as single-line, business-readable scenarios, and the XML-driven config lets you swap platforms with zero code changes. The result is a framework that’s easy to extend, maintain, and scale as your application landscape grows.  
This project was built as a full-featured practice and demonstration framework for mastering test automation and showcasing real-world skills in multi-platform QA.

## Project Overview

This repository implements a reusable, config-driven automation framework that exercises every layer of a typical enterprise application:

- **Web** (Selenium)  
- **Mobile** (Appium)  
- **API** (REST)  
- **Database** (SQL validations)  
- **Desktop** (WinAppDriver)  
- **Electron** (TodoList app)  

Each platform has its own **Flows** module that abstracts low-level interactions into business-readable steps, making tests concise and maintainable.

---

## Features

- **Page Object Model** for each UI flavor (Web, Mobile, Desktop, Electron)  
- **Flows Layer** per platform (**web_flows.py**, **mobile_flows.py**, **api_flows.py**, **db_flows.py**, **desktop_flows.py**, **electron_flows.py**)  
- **UIActions & Verifications** helpers for clicks, typing and assertions  
- **APIActions** wrapper for HTTP requests  
- **DBActions** wrapper for SQL execution and result validation  
- **Common Ops** utilities (**common_ops.py**): configuration reader, wait wrapper, logging  
- **Factory Pattern** (**manage_pages.py**): central page-object instantiation by driver type  
- **Config-Driven** via a single **XML** settings file  
- **Allure** reporting with step annotations, screenshots, logs  
- **PyTest** fixtures, markers, parametrization  

---

## Tools & Frameworks

- **PyTest** – Test runner & framework  
- **Selenium** / **Appium** – Web & Mobile automation  
- **WinAppDriver** / **ElectronDriver** – Desktop & Electron automation  
- **Requests** – API testing  
- **SQLite (DB-Browser)** – Simple local data source  
- **Allure** – Test reporting  

---

## CI/CD with Jenkins

This project includes a `Jenkinsfile` for automated CI/CD pipelines.  
The pipeline is configured to:

- Pull the latest code from GitHub  
- Install all Python dependencies from `requirements.txt`  
- Run automated tests across multiple platforms:  
  - Web (Selenium)  
  - API (Requests + JSONPlaceholder)  
  - Database (SQLite)  
  - Desktop (WinAppDriver)  
  - Electron (TodoList app)  
- Generate a unified Allure report after each run  

With this setup, every code update is automatically tested and reported through Jenkins, similar to how CI/CD pipelines are implemented in real-world projects.

---

## Configuration & Key Settings

All settings live in **XML** (`configuration/configuration.xml`). Here’s an example snippet:

```xml
<Environment>
    <!-- General -->
    <ImplicitlyWait>10</ImplicitlyWait>
    <WaitForElement>30</WaitForElement>
    <ScreenshotsPath>./allure-screen-shots/</ScreenshotsPath>

    <!-- Web -->
    <Browser>Chrome</Browser>
    <Url>https://www.saucedemo.com/</Url>
    <username>standard_user</username>
    <password>secret_sauce</password>
    <disabled_user>locked_out_user</disabled_user>
</Environment>
```
---

## Getting Started

### Quick Start

1. Clone the repo  
2. Install dependencies:  

   ```bash
   pip install -r requirements.txt
   ```

3. Configure your `configuration/configuration.xml`  
4. Run a sample test to see the Flows syntax in action:  

   ```bash
   pytest test_cases/web_tests/test_web_functionality.py
   ```

---

### Sample Test Snippet

```python
def test_add_and_remove_item():
    WebFlows.login("standard_user", "secret_sauce")
    WebFlows.add_backpack_to_cart()
    WebFlows.remove_item_from_inventory()
    WebFlows.logout()
```


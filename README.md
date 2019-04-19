# Logic circuit simulator

[![Build Status](https://travis-ci.com/Sean2525/Logic-circuit-simulator.svg?branch=master)](https://travis-ci.com/Sean2525/Logic-circuit-simulator) [![codecov](https://codecov.io/gh/Sean2525/Logic-circuit-simulator/branch/master/graph/badge.svg)](https://codecov.io/gh/Sean2525/Logic-circuit-simulator) ![GitHub](https://img.shields.io/github/license/sean2525/Logic-circuit-simulator.svg?style=popout) [![python3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release)

> This is a small exam to join a lab.

This repository use [pipenv](https://github.com/pypa/pipenv) to manage dev-packages.

### if you don't want to use it, you can **follow the without pipenv** command.

## Install

```bash
# with pipenv
pipenv install --dev
# without pipenv
pip install pytest pytest-cov pytest-mock
```

## Usage

**run tests**

```bash
# with pipenv
pipenv run python -m pytest --cov=./ --cov-report term-missing --cov-config=.coveragerc ./tests
# without pipenv
python -m pytest --cov=./ --cov-report term-missing --cov-config=.coveragerc ./tests
```

**run simulator**

```bash
# with pipenv
pipenv run python main.py
# without pipenv
python main.py
```

## Description

**lcf file**  
![](https://i.imgur.com/UZI6u7S.png)

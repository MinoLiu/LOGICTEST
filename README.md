# Logic circuit simulator

[![Build Status](https://travis-ci.com/Sean2525/Logic-circuit-simulator.svg?branch=master)](https://travis-ci.com/Sean2525/Logic-circuit-simulator) [![codecov](https://codecov.io/gh/Sean2525/Logic-circuit-simulator/branch/master/graph/badge.svg)](https://codecov.io/gh/Sean2525/Logic-circuit-simulator) ![GitHub](https://img.shields.io/github/license/sean2525/Logic-circuit-simulator.svg?style=popout)

> This is a small exam to join a lab.

## Install

```bash
pipenv install --dev
```

## Usage

run tests

```bash
pipenv run python -m pytest --cov=./ --cov-report term-missing --cov-config=.coveragerc
```

run simulator

```bash
pipenv run python main.py
```

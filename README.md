# Azure STT Python Integration

Following instructions from [HERE](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-use-codec-compressed-audio-input-streams?tabs=linux%2Cdebian%2Cjava-android%2Cterminal&pivots=programming-language-python)

## Install `python 3.12` on your system

> On Ubuntu 24.04 you should have `python 3.12`

## Create `.venv` for PyCharm 

Steps

1. Switch Python Interpreter
2. Add New Interpreter > Add Local Interpreter 

From `Add Python Interpreter` modal:

1. Virtual Env Environment
2. Environment > New
3. Location: e.g. `/home/robert/git/mi/poc/azure-py/.venv`

## Install dependencies via `requirements.txt`

Activate `.venv` environment

```bash
source .venv/scripts/activate
```

```bash
pip install -r requirements.txt
```

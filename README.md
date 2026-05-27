# Project Setup
In this file we will cover the essentials to install and run the project locally according to the challenge requirements

## Requirements
1. Have python 3.11.11 installed
2. An IDE compatible with python
3. Clone or download the project
```bash
git clone <repo-url>
```
4. Create a python virtual environment
```bash
python -m venv <environment-name>
```
5. Activate your virtual environment
```bash
source <environment-name>/bin/activate
```
6. Navigate inside the root folder of the project
```bash
cd optum-asses
```
7. Install dependencies listed in the requirements.txt file
```bash
pip install -r requirements.txt
```
8. Configure your env variables following the example env file, you need the following keys:
    - Your OpenAI API key
    - Your supabase URL
    - Your supabase KEY
    - Your DB URL from supabase (use pooler connection string)
9. Launch the project
```bash
chainlit run front/main.py
```
That will open a basic ChatGPT like UI to start interacting with the agentic solution
<p align="center">
  <img src="./logo.png" />
</p>

<p align="center">
  <!-- <a href="https://anarchy.ai/" target="_blank"><img src="https://img.shields.io/badge/View%20Documentation-Docs-yellow"></a>
  <a href="https://discord.gg/YmNvCAk6W6" target="_blank"><img src="https://img.shields.io/badge/Join%20our%20community-Discord-blue"></a> -->
  <a href="https://github.com/ingenhub/agent-email">
      <img src="https://img.shields.io/github/stars/ingenhub/agent-email" />
  </a>
</p>
<h1 align='center'> Ingenuity Agents (Email) </h1>
<p align='center'><em>the Center of Ingenuity that runs prompt-economy</em></p>

Currently, AI tools are usually constrained to a chat window or are limited in the way they can directly help your day-to-day life. Let's change the way people get value from AI, and make it more accessible for everyone.

>This project is in BETA. Expect continuous improvement and development.

<br/>

## Quickstart

<br/>

### Requirements

Python >=3.10 supported. To check what's the installed version :
```bash 
python3 --version 
``` 

<br/>

### Installation

```bash
git clone https://github.com/ingenhub/agent-email.git

cd agent-email

cp .example.env .env

python3 -m venv .venv

. .venv/bin/activate

pip install openai google-generativeai
```

<br/> 

### Environment file [.env](.example.env)

```bash
OPENAI_KEY="sk-xxx"
GEMINIAI_KEY="xxx"
SYSTEM_PROMPT="You are a helpful assistant.."
IMAP_SERVER="imap.xx.xxxx.xxx"
SMTP_SERVER="smtp.xx.xxxx.xxx"
USER_NAME="xxx@xxxx.xxx"
PASSWORD="xxxxxx"
```
<br/>

### How it Work
1. Write an email to agent's email address (same as IMAP username)

2. Run the script:

    ``` python3 main.py ``` (default ChatGPT 3.5 Turbo)

    or 

    ``` python3 main-gemini.py ``` (using Gemini Pro)

<br/>

### Demo (using Gemini AI)

```text
Hi,

What's the math equation to prove a wormhole?

Thanks!
```

Click to send email to [door@ingenhub.com](mailto:door@ingenhub.com?subject=Asking%20common%20question.&body=Hi%2C%0A%0AWhat%27s%20the%20math%20equation%20to%20prove%20a%20wormhole%3F%0A%0AThanks!)

<br/>

## License
MIT license. For more information, see the [LICENSE](LICENSE) file included in the repository.
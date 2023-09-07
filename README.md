<div align="center">
    <a href="https://openinterpreter.com">
        <img src="https://openinterpreter.com/assets/favicon/favicon-32x32.png" alt="Open Interpreter Icon" />
    </a>
    <h1>Open Interpreter</h1>
</div>

<div align="center">
    <div>
        <a href="https://discord.gg/YG7APUyJ5">
            <img alt="Discord" src="https://img.shields.io/discord/1146610656779440188?logo=discord&style=flat&logoColor=white">
        </a>
        <img src="https://img.shields.io/static/v1?label=license&message=MIT&color=white&style=flat" alt="License" />
    </div>
    <div>
        <strong>Let language models run code on your computer.</strong>
    </div>
    <div>
        An open-source, locally running implementation of OpenAI's Code Interpreter.
    </div>
    <a href="https://openinterpreter.com">Get early access to the desktop application.</a>
</div>

<br>

![poster](https://github.com/KillianLucas/open-interpreter/assets/63927363/08f0d493-956b-4d49-982e-67d4b20c4b56)

## Introduction

**Open Interpreter** lets LLMs run code (Python, Javascript, Shell, and more) locally. You can chat with Open Interpreter through a ChatGPT-like interface in your terminal by running `interpreter` after installing.

This provides a natural-language interface to your computer's general-purpose capabilities:

- Generate or modify files such as PDFs, CSVs, etc.
- Manage a Chrome browser for conducting research
- Compute, clean, and study large datasets
- ...and much more!

**⚠️ NOTE: You'll be asked to approve code before it's run.**

## Visual Demo

https://github.com/KillianLucas/open-interpreter/assets/63927363/37152071-680d-4423-9af3-64836a6f7b60

#### An interactive demo is also available on Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WKmRXZgsErej2xUriKzxrEAXdxMSgWbb?usp=sharing)

## Quick Start

```shell
pip install open-interpreter
```

## Command Line (Terminal)

To start an interactive chat in your terminal after installation, simply run `interpreter` from the command line:

```shell
interpreter
```

### Changing Models (GPT-4, GPT-3.5-Turbo, Code Llama)

**⚠️ NOTE: We're working on consolidating these into a unified command.**

If you do not have access to GPT-4 or want to use "fast mode" (`gpt-3.5-turbo`):

```shell
interpreter --fast
```

**⚠️ NOTE: This requires you to install Code Llama on your machine.**

You can run `interpreter` in "local mode" from the command line to use `Code Llama`:

```shell
interpreter --local
```

### Don't have an OpenAI key?

You can get your own OpenAI API key by following the following instructions:

1. Go to https://platform.openai.com/account/api-keys
2. Click on the `+ Create New Secret Key` button
3. Enter an identifier name (optional) and click on the `Create Secret Key` button
4. Copy & Paste!

## Programmatic (Python)

Run `interpreter.chat()` from a .py file:

```python
interpreter.chat()
```

For more precise control, you can pass messages directly to `.chat(message)`:

```python
import interpreter

interpreter.chat("Plot APPL and META's normalized stock prices") # Executes a single command
interpreter.chat() # Starts an interactive chat
```

```python
interpreter.chat("Add subtitles to all videos in /videos.")

# ... Streams output to your terminal, completes task ...

interpreter.chat("These look great but can you make the subtitles bigger?")

# ...
```

#### You would have to set the model manually in Python:

```python
interpreter.model = "gpt-3.5-turbo"
```

#### Start a New Chat

In Python, Open Interpreter remembers conversation history. If you want to start fresh, you can reset it:

```python
interpreter.reset()
```

#### Save and Restore Chats

`interpreter.chat()` returns a List of messages when return_messages=True, which can be used to resume a conversation with `interpreter.load(messages)`:

```python
messages = interpreter.chat("My name is Killian.", return_messages=True) # Save messages to 'messages'
interpreter.reset() # Reset interpreter ("Killian" will be forgotten)

interpreter.load(messages) # Resume chat from 'messages' ("Killian" will be remembered)
```

#### Customize System Message

You can inspect and configure Open Interpreter's system message to extend its functionality, modify permissions, or give it more context.

```python
interpreter.system_message += """
Run shell commands with -y so the user doesn't have to confirm them.
"""
print(interpreter.system_message)
```

## How Does it Work?

Open Interpreter equips a [function-calling language model](https://platform.openai.com/docs/guides/gpt/function-calling) with an `exec()` function, which accepts a `language` (like "python" or "javascript") and `code` to run.

We then stream the model's messages, code, and your system's outputs to the terminal as Markdown.

## Safety Notice

Since generated code is executed in your local environment, it can interact with your files and system settings, potentially leading to unexpected outcomes like data loss or security risks.

**⚠️ NOTE: Open Interpreter will ask for user confirmation before executing code.**

You can run `interpreter -y` or set `interpreter.auto_run = True` to bypass this confirmation, in which case:

- Be cautious when requesting commands that modify files or system settings.
- Watch Open Interpreter like a self-driving car, and be prepared to end the process by closing your terminal.
- Consider running Open Interpreter in a restricted environment like Google Colab or Replit. These environments are more isolated, reducing the risks associated with executing arbitrary code.

## Comparison to ChatGPT's Code Interpreter

OpenAI's release of [Code Interpreter](https://openai.com/blog/chatgpt-plugins#code-interpreter) with GPT-4 presents a fantastic opportunity to accomplish real-world tasks with ChatGPT.

However, OpenAI's service is hosted, closed-source, and heavily restricted:
- No internet access.
- [Limited set  of pre-installed packages](https://wfhbrian.com/mastering-chatgpts-code-interpreter-list-of-python-packages/).
- 100 MB maximum upload, 120.0 second runtime limit.
- State is cleared (along with any generated files or links) when the environment dies.

---

Open Interpreter overcomes these limitations by running on your local environment. It has full access to the internet, isn't restricted by time or file size, and can utilize any package or library.

This combines the power of GPT-4's Code Interpreter with the flexibility of your local development environment.

## Contributing

This is a community-made project. If it looks exciting to you, please don't hesitate to contribute!

## License

Open Interpreter is licensed under the MIT License. You are permitted to use, copy, modify, distribute, sublicense and sell copies of the software.

**⚠️ NOTE: This software is not affiliated with OpenAI.**

> Having access to a junior programmer working at the speed of your fingertips ... can make new workflows effortless and efficient, as well as open the benefits of programming to new audiences.
>
> — _OpenAI's Code Interpreter Release_

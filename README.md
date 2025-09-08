
# buzzline-02-Mahitha

Streaming data is often too big for any one machine. Apache Kafka is a popular streaming platform that uses publish-subscribe patterns:

- **Producers** publish streaming data to topics
- **Consumers** subscribe to topics to process data in real-time

We'll write Python producers and consumers to work with Kafka topics.

Kafka needs space - it's big. 

It also comes from the Linux world. We'll use WSL on Windows machines.

## Copy This Example Project & Rename

1. Copy/fork this project into your GitHub account and create your own version of this project to run and experiment with.
2. Name it `buzzline-02-yourname` where yourname is something unique to you.

## Task 1. Install and Start Kafka (using WSL if Windows)

Before starting, ensure you have completed the setup tasks in <https://github.com/denisecase/buzzline-01-case> first.
Python 3.11 is required.

In this task, we will download, install, configure, and start a local Kafka service.

1. Install Windows Subsystem for Linux (Windows machines only)
2. Install Kafka Streaming Platform
3. Start the Kafka service (leave the terminal open).

For detailed instructions, see:

- [SETUP_KAFKA](SETUP_KAFKA.md)

## Task 2. Manage Local Project Virtual Environment

Open your project in VS Code and use the commands for your operating system to:

1. Create a Python virtual environment
2. Activate the virtual environment
3. Upgrade pip
4. Install from requirements.txt

### Windows

Open **PowerShell** terminal in VS Code (Terminal / New Terminal / PowerShell).

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip wheel setuptools
py -m pip install --upgrade -r requirements.txt
```

If you get execution policy error, run this first:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Mac / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade -r requirements.txt
```

## Task 3. Start a Kafka Producer

Producers generate streaming data for our topics.

In VS Code, open a terminal.
Use the commands below to activate .venv, and start the producer.

Windows **PowerShell**:

```shell
.venv\Scripts\activate
py -m producers.kafka_producer_case
```

Mac/Linux:

```zsh
source .venv/bin/activate
python3 -m producers.kafka_producer_case
```

## Task 4. Start a Kafka Consumer

Consumers process data from topics or logs in real time.

In VS Code, open a NEW terminal in your root project folder.
Use the commands below to activate .venv, and start the consumer.

Windows **PowerShell**:

```shell
.venv\Scripts\activate
py -m consumers.kafka_consumer_case
```

Mac/Linux:

```zsh
source .venv/bin/activate
python3 -m consumers.kafka_consumer_case
```

## Later Work Sessions

When resuming work on this project:

1. Open the project folder in VS Code.
2. Start the Kafka service (in WSL if Windows).
3. Activate your local project virtual environment (.venv) in your OS-specific terminal. 

## Save Space

To save disk space, you can delete the .venv folder when not actively working on this project.
You can always recreate it, activate it, and reinstall the necessary packages later.
Managing Python virtual environments is a valuable skill.

## License

This project is licensed under the MIT License as an example project.
You are encouraged to fork, copy, explore, and modify the code as you like.
See the [LICENSE](LICENSE.txt) file for more.
=======
# buzzline-01-Mahi

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)

This project introduces streaming data. 
The Python language includes generators - we'll use this feature to generate some streaming buzzline messages. 
As the code runs, it will continuously update the log file. 
We'll use a consumer to monitor the log file and alert us when a special message is detected. 

## Task 1. Set Up Your Machine & Sign up for GitHub

We practice professional Python. In each course that uses Python, we use a standard set of popular professional tools. 
This course uses advanced tools such as Apache Kafka that requires **Python 3.11**. 
You are encouraged to install and practice with multiple versions. 
If space is an issue, we only need Python 3.11 for this course. 

Follow instructions at [pro-analytics-01](https://github.com/denisecase/pro-analytics-01), **Part 1: Set Up Machine & Sign up for GitHub**.

**Setup is critical.** Follow all steps exactly and verify success before proceeding.  
Missing or incomplete setup steps can make the course impossible to complete.

## Task 2. Initialize a Project

Once your machine is ready, you'll copy this template repository into your own GitHub account  
and create your personal version of the project to run and explore. 
Name it **buzzline-01-yourname** (replace `yourname` with something unique to you).  

Follow instructions at [pro-analytics-01](https://github.com/denisecase/pro-analytics-01), **Part 2: Initialize a Project**.
This will get your project stored safely in the cloud - and ready for work on your machine. 

## Task 3. Generate Streaming Data (Terminal 1)

Now we'll generate some streaming data. 
By the way - you've done 90% of the hard work before we even look at code. 
Congratulations!

In VS Code, open a terminal.
Use the commands below to activate .venv, and run the generator as a module. 
To learn more about why we run our Python file as a module, see [PYTHON-PKG-IMPORTS](docs/PYTHON-PKG-IMPORTS.md) 

Windows PowerShell:

```shell
.venv\Scripts\activate
py -m producers.basic_producer_case
```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m producers.basic_producer_case
```

## Task 4. Monitor an Active Log File (Terminal 2)

A common streaming task is monitoring a log file as it is being written. 
This project has a consumer that reads and processes our own log file as log messages arrive. 

In VS Code, open a NEW terminal in your root project folder. 
Use the commands below to activate .venv, and run the file as a module. 

Windows:
```shell
.venv\Scripts\activate
py -m consumers.basic_consumer_case
```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m consumers.basic_consumer_case
```

## Save Space
To save disk space, you can delete the .venv folder when not actively working on this project.
We can always recreate it, activate it, and reinstall the necessary packages later. 
Managing Python virtual environments is a necessary and valuable skill. 
We will get a good amount of practice. 

## License
This project is licensed under the MIT License as an example project. 
You are encouraged to fork, copy, explore, and modify the code as you like. 
See the [LICENSE](LICENSE.txt) file for more.


## Producer Script 
The producer script generates custom buzz messages and logs them. To run it:
1. Ensure your virtual environment is activated.
2. Run the producer script with command:py producers/basic_producer_mahi
3. The generated messages will be logged both to the console and a file located in the logs directory.

Custom Message Example:
-Breaking news! I just shared a book and it was absolutely shocking!
-Breaking news! I just loved an app and it was absolutely mind-blowing! 

## consumer script
detects the message, triggering the alert.

## producers.kafka_producer_mahi 
code generates messages, It picks a patient from the list, telling which patient just arrived, checked in or waiting at the hospital. Then prints the message like example "Patient David Lee is here at the hospital; he just arrived at the reception desk.
>>>>>>> 12c6818 (included kafka_producer_mahi)

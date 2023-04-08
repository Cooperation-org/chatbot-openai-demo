# chatbot-sttr-grant

- To run install the required libraries and replace the openai api wiht your api 
```
sudo apt install python
```

```
python -m venv env && source env/bin/activate

```

```
pip install -r requirements.txt

```

```
python uvicorn main:app --reload

```

- The accuracy is a little low for now so please be specific while asking questions

- Team members can add any text file or pdf in the textdata folder and name it related to their project and the bot will provide answers based on that info
- The format must be text or pdf but content can be any code , it can't process images or videos

# Steps for updating the EC2 instance running our chatbot FastAPI application in a virtual environment and using tmux:

 The Api Backend is accessible through
- [chatbot.linkedtrust.us](www.chatbot.linkedtrust.us/docs)
- [Public IP](http://52.53.248.142/docs)
### Instructions on how to update an EC2 instance that is running a FastAPI application in a virtual environment using tmux.

1. Prerequisites
- Before updating the EC2 instance, ensure that you have the following prerequisites:

2. Access to the EC2 instance using SSH.
- A virtual environment set up in the EC2 instance.
- A tmux session started for the FastAPI application with the name "myapp".
- Git installed in the EC2 instance.
- Your FastAPI application code hosted on a Git repository.

3. Updating the EC2 Instance
Follow these steps to update your EC2 instance:

- SSH into the EC2 instance.
```

```

4. Navigate to the directory that contains your FastAPI application code.

```
cd chatbot-sttr-bot/
```

5. Activate the virtual environment for the FastAPI application.

```
source env/bin/activate
```

6. Stop the tmux session that is running the FastAPI application.

```
tmux send-keys -t myapp C-c
```
- Pull the latest code changes from the Git repository.

```
git pull
```

7. Install any new dependencies or update existing ones by running the following command:

```
pip install -r requirements.txt
```

Start the FastAPI application in the tmux session with the name "myapp".

```
tmux send-keys -t myapp "uvicorn main:app --host 0.0.0.0 --port 80" C-m
```

8. Verify that the FastAPI application is running as expected by accessing it through a web browser or using a tool such as curl.

```
curl http://localhost:80
```

That's it! Your EC2 instance should now be updated with the latest changes to your FastAPI application.
for further complaints, enquires or contact
contact 

```
peter benjamin ani or Aaditya Bansal on slack
```




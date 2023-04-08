# chatbot-sttr-grant

To run install the required libraries and replace the openai api wiht your api
The accuracy is a little low for now so please be specific while asking questions
Team members can add any text file or pdf in the textdata folder and name it related to their project and the bot will provide answers based on that info
The format must be text or pdf but content can be any code , it can't process images or videos

<!-- 
[Unit]
Description=My FastAPI App For ChatBot sttr

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/myapp
ExecStart=/usr/bin/env bash -c 'source /home/ubuntu/chatbot-sttr-grant/env/bin/activate && uvicorn main:app --host 0.0.0.0 --port 80'
Restart=always

[Install]
WantedBy=multi-user.target
 -->

# Chat API
This is a basic chat application API in REST like format

## Steps to getting setup

1. Make sure that python3 is installed
2. Make sure that virtualenv is installed
    - Create a virtual env with: "python3 -m venv venv"
    - Go into the venv: "source venv/bin/activate"
3. install requirements:
    - "pip3 install -r requirements.txt"
    - NOTE* - Save using "pip3 freeze > requirements.txt"




### Steps to port forward WSL 2 to computer so you can see the web app
1. Once you start ubuntu/WSL2, make sure that the firewall allows the port incase it is on.
    - "ufw allow $PORT"
2. Then in windows, run "netsh interface portproxy add v4tov4 listenport=$PORT listenaddress=0.0.0.0 connectport=$PORT connectaddress=127.0.0.1" 
3. Extra step that wasn't needed when I set it up but add an Inbound Rule using the Windows Defender Firewall with Advanced Security. Add the PORTS of interests.
4. Should work now but the odd thing is that it still only works on port 8000... so make sure you change that in the web application.
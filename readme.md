
### How to run

1. Clone the repository
2. Run the following command in the terminal if you are using a virtual environment
```bash
python3.10 -m venv venv
```
3. Activate the virtual environment
```bash
source venv/bin/activate
```
4. Install the requirements
```bash
pip install -r requirements.txt
```
5. Run the following command to start the application

To download video :
```bash
python3.10 vid_dl.py https://youtu.be/dQw4w9WgXcQ
```
To download playlist :
```bash
python3.10 playlist_dl.py url
```
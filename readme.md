## Data Source
The application uses `cybersecurity_events.db`, containing 6,999 open-data security events and responses.

## Local Setup
```bash
git clone <your-repo-url>
cd <repo-dir>
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=run.py
flask db stamp head
python run.py

visit online service URL
Visit https://politicmusic-sultannumeric-5000.codio-box.uk/events/
visit https://cybersec-events.onrender.com/error500

## Render Deployment URL  
The application is live at:  
[CyberSecurity Events on Render](https://cybersec-events.onrender.com)

## Features  
- Event list with severity filtering (Low, Medium, High, Critical)  
- Event details with response actions  
- Custom 404 and 500 error pages  
- Pagination for large datasets  

## How to Access  
- Events: `/events/`  
- Event Details: `/event/<event_id>`  
- Filter by Severity: `/events/?severity=low`  
- Example URLs:  
  - Low Severity: [Events - Low](https://cybersec-events.onrender.com/events/?severity=low)  
  - High Severity: [Events - High](https://cybersec-events.onrender.com/events/?severity=high)  

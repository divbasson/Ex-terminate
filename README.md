
# Facebook Photo Cleanup Script

A Python script to help automate the cleanup of Facebook photos involving a specific person (e.g., an ex-partner). This script provides a way to filter, hide, delete, or untag photos in a user-friendly and interactive manner.

---

## Features

- Authenticate via Facebook Graph API.
- Fetch all photos where the user is tagged or the uploader.
- Filter photos by a specific friend (selected by the user).
- Perform actions (hide, delete, untag) on each photo with user approval.

---

## Prerequisites

1. **Python 3.7 or higher**  
   Make sure Python is installed on your system. [Download Python](https://www.python.org/downloads/)

2. **Facebook Developer App**  
   Set up a Facebook Developer App to get the necessary credentials (App ID and App Secret).  
   - [Create a Facebook Developer App](https://developers.facebook.com/apps/)

3. **Install Required Libraries**  
   Install the required Python libraries: `requests`.  
   Run the following command:  
   ```bash
   pip install requests
   ```

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/facebook-photo-cleanup.git
   cd facebook-photo-cleanup
   ```

2. Edit the script to add your Facebook Developer credentials:
   - Open `script.py` and replace placeholders:
     ```python
     APP_ID = 'your_app_id'
     APP_SECRET = 'your_app_secret'
     REDIRECT_URI = 'your_redirect_url'
     ACCESS_TOKEN = 'your_access_token'
     ```

3. Generate a User Access Token:
   - Use the Facebook Developer Tools to generate a long-lived access token for testing.

---

## Running the Script

1. Run the script:
   ```bash
   python script.py
   ```

2. Follow the interactive prompts:
   - Authenticate with the provided URL.
   - Select the friend whose photos you'd like to manage.
   - Approve actions (hide, delete, untag) for each photo.

---

## Limitations

- Facebook's Graph API restricts certain actions (e.g., moving photos to new albums).
- User must manually approve each action.

---

## Future Enhancements

- Add a graphical interface for easier use.
- Support batch processing with reduced manual steps.
- Expand compatibility with other social platforms.

---

## Disclaimer

This script is provided as-is and is meant for personal use. Be cautious when managing photos and ensure compliance with Facebook’s terms of service.

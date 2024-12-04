import requests

APP_ID = 'your_app_id'
APP_SECRET = 'your_app_secret'
REDIRECT_URI = 'your_redirect_url'

AUTH_URL = f"https://www.facebook.com/v16.0/dialog/oauth?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&scope=user_photos,user_friends"

print(f"Authenticate here: {AUTH_URL}")

ACCESS_TOKEN = 'user_access_token'

# Fetch photos with tags
def get_photos_with_tags():
    url = f"https://graph.facebook.com/v16.0/me/photos?fields=id,images,tags,from&access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    return response.json().get('data', [])

# Filter photos by a specific friend
def filter_photos_by_friend(photos, friend_id):
    return [
        photo for photo in photos
        if any(tag['id'] == friend_id for tag in photo.get('tags', {}).get('data', []))
    ]

# Request user approval for each photo
def process_photos(photos, friend_name):
    for photo in photos:
        photo_id = photo['id']
        photo_url = photo['images'][0]['source']
        print(f"\nPhoto ID: {photo_id}")
        print(f"Photo URL: {photo_url}")
        print(f"Tagged with {friend_name}")

        action = input("Choose action: (H)ide, (D)elete, (U)ntag, (S)kip: ").strip().lower()

        if action == 'h':
            hide_photo(photo_id)
        elif action == 'd':
            delete_photo(photo_id)
        elif action == 'u':
            untag_photo(photo_id, friend_id)
        elif action == 's':
            print("Skipped.")
        else:
            print("Invalid choice. Skipping.")

# Hide photo (set privacy to 'Only Me')
def hide_photo(photo_id):
    url = f"https://graph.facebook.com/v16.0/{photo_id}"
    payload = {"privacy": '{"value": "SELF"}', "access_token": ACCESS_TOKEN}
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f"Photo {photo_id} hidden successfully.")
    else:
        print(f"Failed to hide photo {photo_id}: {response.json()}")

# Delete photo
def delete_photo(photo_id):
    url = f"https://graph.facebook.com/v16.0/{photo_id}"
    response = requests.delete(url, params={"access_token": ACCESS_TOKEN})
    if response.status_code == 200:
        print(f"Photo {photo_id} deleted successfully.")
    else:
        print(f"Failed to delete photo {photo_id}: {response.json()}")

# Untag user from photo
def untag_photo(photo_id, friend_id):
    url = f"https://graph.facebook.com/v16.0/{photo_id}/tags/{friend_id}"
    response = requests.delete(url, params={"access_token": ACCESS_TOKEN})
    if response.status_code == 200:
        print(f"Untagged successfully from photo {photo_id}.")
    else:
        print(f"Failed to untag photo {photo_id}: {response.json()}")

# Example Workflow
print("Fetching photos...")
photos = get_photos_with_tags()

# Let user select a friend to focus on
friend_id = input("Enter the friend's Facebook ID: ")
friend_name = input("Enter the friend's name for display: ")

filtered_photos = filter_photos_by_friend(photos, friend_id)
print(f"Found {len(filtered_photos)} photos tagged with {friend_name}.")

process_photos(filtered_photos, friend_name)

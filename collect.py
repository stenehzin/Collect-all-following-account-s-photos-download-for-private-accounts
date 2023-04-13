import instaloader

def download_followees_photos():
    L = instaloader.Instaloader(dirname_pattern="{profile}")

    # Login to the profile
    try:
        L.context.login("nickname", "password")
    except Exception as e:
        print(f"Error: {e}")
        return

    # Get the profile of the logged-in user
    profile = instaloader.Profile.from_username(L.context, L.context.username)

    # Get the followees of the logged-in profile
    followees = profile.get_followees()

    # Loop through the followees and download their posts
    for followee in followees:
        for post in followee.get_posts():
            L.download_post(post, target=f"{followee.username}_photos")

if __name__ == "__main__":
    download_followees_photos()

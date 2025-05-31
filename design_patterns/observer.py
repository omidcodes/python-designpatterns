"""
Observer Pattern
🔧 Practice: Build a YouTube-style notification system

Channel is the subject.

Subscribers implement an update(message) method.

When the channel uploads a video, notify all subscribers.

🧠 Bonus: Allow subscribers to unsubscribe.
"""

# the Subject, or “Publisher”
class Channel:

    def __init__(self):
        self._subscribers = []
    

    def subscribe(self, user):
        self._subscribers.append(user)
    
    def unsubscribe(self, user):
        self._subscribers.remove(user)

    def upload_video(self, video_name:str ):
        for s in self._subscribers:
            s.update(f"New video called '{video_name}' uploaded.")

# the Observer, or “Subscriber”
class User:
    
    def __init__(self, username):
        self.username = username
    
    def update(self, message):
        print(f"Hello '{self.username}'. {message}")


u1 = User("Omid")
u2 = User("Reza")
u3 = User("Jack")

ch = Channel()
ch.subscribe(u1)
ch.subscribe(u2)
ch.subscribe(u3)


ch.unsubscribe(u2)  # optional (unsubscribe)

ch.upload_video(video_name="Interstellar")

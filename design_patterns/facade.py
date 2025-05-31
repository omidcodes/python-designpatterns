# Subsystem classes

class Amplifier:
    def on(self):
        print("Amplifier: on")

    def set_volume(self, level):
        print(f"Amplifier: setting volume to {level}")

    def off(self):
        print("Amplifier: off")


class DVDPlayer:
    def on(self):
        print("DVD Player: on")

    def play(self, movie):
        print(f"DVD Player: playing '{movie}'")

    def stop(self):
        print("DVD Player: stopped")

    def off(self):
        print("DVD Player: off")


class Lights:
    def dim(self, level):
        print(f"Lights: dimming to {level}%")

    def on(self):
        print("Lights: full brightness")

    def off(self):
        print("Lights: off")


# Facade class

class HomeTheaterFacade:
    def __init__(self, amplifier, dvd_player, lights):
        self.amp = amplifier
        self.dvd = dvd_player
        self.lights = lights

    def watch_movie(self, movie_title):
        print("Get ready to watch a movie...")
        self.lights.dim(10)             # Step 1: dim lights
        self.amp.on()                   # Step 2: turn on amplifier
        self.amp.set_volume(5)          # Step 3: set volume level
        self.dvd.on()                   # Step 4: turn on DVD player
        self.dvd.play(movie_title)      # Step 5: play the movie
        print("Enjoy your movie!\n")

    def end_movie(self):
        print("Shutting movie theater down...")
        self.dvd.stop()                 # Step 1: stop DVD
        self.dvd.off()                  # Step 2: turn off DVD player
        self.amp.off()                  # Step 3: turn off amplifier
        self.lights.on()                # Step 4: turn lights back on
        print("Movie theater is off.\n")


# Client code

if __name__ == "__main__":
    # Create instances of each subsystem
    amp = Amplifier()
    dvd = DVDPlayer()
    lights = Lights()

    # Create the Facade, passing in the subsystem instances
    home_theater = HomeTheaterFacade(amp, dvd, lights)

    # Use the Facade to watch a movie
    home_theater.watch_movie("Inception")

    # Later, when you're done:
    home_theater.end_movie()

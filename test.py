import pyttsx3 as p

engine = p.init()
engine.setProperty("rate", 140)
engine.say("welcome back sir")
engine.runAndWait()
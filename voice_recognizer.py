import speech_recognition as sr

recognizer = sr.Recognizer()
while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Listening...")
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"You: {text}")
            
            if "stop" in text:
                print("Exiting...")
                break

    except sr.UnknownValueError:
        print("Sorry, I did not understand that. Please repeat.")
        continue
    except sr.RequestError as e:
        print(f"Error with the speech service: {e}")
        break

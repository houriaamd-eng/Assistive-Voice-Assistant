import speech_recognition as sr
from gtts import gTTS
import os

print("=== PROGRAMME D'ASSISTANCE POUR LES BESOINS SPÉCIAUX ===")
print("1. Convertir un texte en voix (Pour les personnes malvoyantes)")
print("2. Convertir l'audio en texte (Pour les personnes malentendantes)")
choix = input("Choisissez 1 ou 2 : ")

if choix == '1':
    # --- Partie : Texte vers Voix ---
    texte_a_lire = input("Écrivez le texte en français : ")
    print("Création de la voix en cours...")
    tts = gTTS(text=texte_a_lire, lang='fr')
    tts.save("voix.mp3")
    os.system("start voix.mp3") # Cette commande lance l'audio sur Windows
    print("✅ Lecture terminée !")

elif choix == '2':
    # --- Partie : Voix vers Texte ---
    r = sr.Recognizer()
    fichier_audio = "test.wav"
    try:
        with sr.AudioFile(fichier_audio) as source:
            print("Écoute de l'audio en cours...")
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language="fr-FR")
            print("✅ Résultat de la transcription :")
            print("=>", text)
    except FileNotFoundError:
        print("❌ Erreur : Le fichier 'test.wav' est introuvable dans le dossier Robo.")
    except Exception as e:
        print("❌ Erreur : ", e)
else:
    print("❌ Choix invalide. Veuillez relancer le programme.")
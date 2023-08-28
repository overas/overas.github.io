from microbit import *
import time

display.show(Image.HAPPY)  # Et smilefjes vises på displayet
while True:  # Løkke som kjører til den blir avbrutt

    if button_a.is_pressed():  # Hvis knapp a trykkes, skjer følgende:

        temperatureValues = open(
            "temperatur.txt", "w"
        )  # Tekstfilen temperatur.txt knyttes til variabel temperatureValues

        break  # Løkka avbrytes
while True:  # Løkke som kjører til den blir avbrutt

    temperatureMeasure = (
        temperature()
    )  # Målt temperatur lagres som variabelen temperatureMeasure

    temperatureValues.write(
        str(temperatureMeasure) + " "
    )  # Den målte temperaturen skrives til tekstfilen temperatur.txt

    display.scroll(temperatureMeasure)  # Temperature vises på displayet

    if button_b.get_presses() > 0:  # Hvis knapp b har blitt trykket, skjer følgende:

        temperatureValues.close()  # Tekstfilen lukkes

        break  # Løkka avbrytes
    time.sleep(30)  # Løkka settes på pause i 30 sekunder
display.show(Image.HEART)  # Et hjerte vises på displayet# Write your code here :-)

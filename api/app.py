from time import sleep
import time
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():

    request.form.get('Body')
    TWILIO_ACCOUNT_SID = 'Twilio ACCOUNT TOKEN'
    TWILIO_AUTH_TOKEN = 'Twilio PASSWORD TOKEN'
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    from_whatsapp_number = 'whatsapp:+TWILIO APPLICATION NUMBER'
    to_whatsapp_number = 'whatsapp:+YOUR NUMBER'

    resp = MessagingResponse()
    # Create reply
    resp.message("Oi Siclana, tudo bem? Meu nome é Casé, sou o bot que o Fulano criou para te lembra o quão importante você para ele! :)")
    resp.message("Ele só quer que você saiba que ele te amo muito, e você é umas das coisas mais maravilhosa que aconteceu na vida dele")
    resp.message("Ele me desenvolveu especialmente para esse dia! <3")

    frases = ["Te amo infinitamente mais mor!","Que sorte eu tenho de ter você cmg!","Espero que cada dia mais eu possa ser feliz com você!", "E só espero casar com você e ter o Gustavo junior <3"]
    fotos = ['PICTURES ARRAY']
    for x in range(0, 4):
        client.messages.create(body=frases[x],
                            media_url=fotos[x],
                            from_=from_whatsapp_number,
                            to=to_whatsapp_number)
        
    resp.message("O que você gostaria de ver hoje?")

    todas_fotos = 'PICTURES'
    resp.message(f"Fotos de vocês dois: {todas_fotos}")

    musicas = 'YOUr PLAYSLIST'
    resp.message(f"Músicas que fazem ele lembrar de você: {musicas}")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
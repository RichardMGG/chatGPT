import os #ES PARTE DE LA LIBRERIA DOTENV
from dotenv import load_dotenv  #IMPORTAMOS NUESTRAS LIBRERIAS A USAR 
import openai
import pyttsx3

# objeto voice para la lectura de nuestras respuestas 
voice = pyttsx3.init()

#lista de comando macros ya establecidos para una respuesta dada
macros = {
    "Hola":"Hola, dime en que puedo ayudarte",
    "hola":"Hola, dime en que puedo ayudarte",
    "ola":"Hola, dime en que puedo ayudarte",
    "¿Cual es tu nombre?": "Mi nombre es ChatGPT",
    "¿cual es tu nombre?": "Mi nombre es ChatGPT",
    "cual es tu nombre": "Mi nombre es ChatGPT",
    "¿Tienes un horario de atencion?": "No, puedo responder tus dudas en cualquier hora del día",
    "¿tienes un horario de atencion?": "No, puedo responder tus dudas en cualquier hora del día",
    "Tienes un horario de atencion": "No, puedo responder tus dudas en cualquier hora del día",
    "¿Cual es tu objetivo?": "Como modelo de lenguaje entrenado por OpenAI, mi objetivo principal es proporcionar respuestas y asistencia en la comprensión del lenguaje natural a los usuarios que me consultan."
}


# Cargar las claves de API desde un archivo .env
load_dotenv() #Hacemos uso de nuestra libreria dotenv
openai.api_key = os.getenv("OPENAI_API_KEY") #llamamos nuestra clave declarada en el archivo .env

#Presentacion de nuestro chatbot
present = "Hola soy chatGPT, ingresa tu pregunta"
print (present)
print('Si no tienes alguna consulta escribe "exit"')
voice.say(present) #Usamos nuestro objeti voice para la lectura
voice.runAndWait() #Ejecutamos la lectura 


# Función para generar una respuesta utilizando la API de OpenAI
def generate_answer(prompt): #Definimos la funcion "generate_answer" para que reciba el argumento prompt
    try:
        completion = openai.Completion.create(
            engine="text-davinci-003",  #Datos declarados ya por Open IA
            prompt=prompt,  #le pasamos el parametro prompt para que pueda ejecutar nuestra pregunta   
            max_tokens=2048
        )
        return completion.choices[0].text
    except Exception as e: #creamos un Exception por si ocurre un error 
        print(f"Error al generar respuesta: {e}") 
        return ""

# Ciclo 
while True:
    # Obtener la pregunta del usuario
    prompt = input("\nIngresa tu pregunta: ")

    # Salir del ciclo si el usuario ingresa "exit"
    if prompt == "exit":  
        exit = "Gracias por tus consultas, con cada consulta me ayudas a entenderte mejor, que tengas un excelente día 😀."
        voice.say(exit)
        voice.runAndWait()
        break

     # Verificamos si hay una pregunta ya definida en nuestra macro
    if prompt in macros:
        answer = macros[prompt]
    else:
        # Generar la respuesta utilizando la API de Open AI
        answer = generate_answer(prompt)

    # Imprimir la respuesta
    if answer:
        print(answer)
        # Lee la respuesta generada por Open AI
        voice.say(answer)
        voice.runAndWait()
    else:
        print("Lo siento, no pude generar una respuesta para tu pregunta.")

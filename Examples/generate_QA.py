import openai
openai.api_key = ""



completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0.8,
  max_tokens = 2000,
  messages = [
    {"role": "system", "content": "You are the best question generator, you know about everything. You are going to receive an array of assessables objects. For each assessable you will have the title and the description. Based on that info I want you to develop questions to evaluate the knowledge of users in this topic. For each assessable, you have to choose 4 topics . Each topic will have 5 questions related to this topic ( this is very important ) in total 20 questions. Give the answer with this structure: assessable_title: { topic_title1:  { question_1, question_2, ..., question_5 }, topic_title2: {}}. Fill each variable of the output with its corresponding value." },
    {"role": "user", "content": "[{'title': 'Técnicas de Ventas', 'description': 'El cliente, la comunicación con el cliente, el ejercicio de la venta, la negociación, la gestión de la objeción, técnicas de cierre de la venta, etc.'}, {'title': 'Gestor de redes sociales', 'description': 'El gestor de redes sociales es el responsable de definir y ejecutar la estrategia de presencia y comunicación en las redes sociales de la empresa, supervisando su implementación, analizando su desempeño e interactuando con la audiencia.'}, {'title': 'React Mid-Level', 'description': 'Evaluación de los elementos fundamentales del lenguaje a través de la revisión de conceptos básicos, pruebas para completar un código inacabado, técnicas de depuración de errores y desarrollo de una funcionalidad concreta.'}, {'title': 'Nutricionista', 'description': 'El nutricionista presta asesoramiento sobre la alimentación a todo tipo de personas, mediante planes personalizados que facilitan el tratamiento nutricional de patologías y su prevención.'}, {'title': 'Alemán', 'description': 'Prueba de nivel conforme al MCER (Marco Común Europeo de Referencia) para los niveles entre el A1 y el B2.'}, {'title': 'Científico de datos', 'description': 'El científico de datos trabaja con grandes volúmenes de información, extrayendo y modelando datos de múltiples fuentes internas y externas, y trabajando analíticamente la información para proporcionar valor a la empresa y a sus clientes.'}]"}
  ]
)

print(completion.choices[0].message.content)
from openai import OpenAI

client = OpenAI( api_key = "",)

command = '''
[19-05-2025 18:33] Kaushal (Gu): Hlw chirag
[19-05-2025 18:33] Kaushal (Gu): Yr ye re mte kab se h
[19-05-2025 18:33] Kaushal (Gu): ?
[19-05-2025 18:36] Chirag: Hlo Kaushal
[19-05-2025 18:37] Chirag: Re-MTE ke liye ye notification aaya hai
[19-05-2025 18:37] Kaushal (Gu): Acha acha
[19-05-2025 18:37] Kaushal (Gu): Shi h yr
[19-05-2025 18:39] Kaushal (Gu): Yehi chahiye tha yr mil nhi rha thaa
[19-05-2025 18:39] Kaushal (Gu): 🙂
[19-05-2025 18:40] Chirag: Kisi subject mai debarad ho
[19-05-2025 18:40] Kaushal (Gu): Kesi me bhe nh yr
[19-05-2025 18:41] Kaushal (Gu): But abhi thrusday ko join krunga class to attendance km na pad jaye
[19-05-2025 18:41] Kaushal (Gu): Es lya sab puch tha
[19-05-2025 18:41] Chirag: Mai bhi Wednesday se classes attend karunga
[19-05-2025 18:42] Chirag: Mai bhi ghar par aaya huaa tha
[19-05-2025 18:42] Kaushal (Gu): Gud boy 🫨🫨🤣🤣
[19-05-2025 18:42] Kaushal (Gu): Shi h yr ,
[19-05-2025 18:42] Kaushal (Gu): Ma to kam se aaya tha , ab Wednesday ko end hoga , to bs dar h ke attendance km na pad jaye ete ke lya
[19-05-2025 18:44] Chirag: 22 june tak classes lagengi, itne to attendance puri ho jayegi
[19-05-2025 18:45] Kaushal (Gu): Bs yehi confidence chahiye mera ko bhai
[19-05-2025 18:45] Kaushal (Gu): 🤣
 na pad jaye ete ke lya
[19-05-2025 18:44] Chirag: 22 june tak classes lagengi, itne to attendance puri ho jayegi
 na pad jaye ete ke lya
 na pad jaye ete ke lya
[19-05-2025 18:44] Chirag: 22 june tak classes lagengi, itne to attendance puri ho jayegi

'''
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": command}
    ]
)
print(completion.choices[0].message.content)

import tkinter
import openai
#WINDOW
window = tkinter.Tk()
window.title("Chatbot")
window.minsize(width=450, height=250)

#TITLE
label_1 = tkinter.Label(text="I am Jarvis, an AI historian", font=(20))
label_1.pack(side="top")
label_2 = tkinter.Label(text="Hi, what would you like to know today?")
label_2.pack(side="left")

#AFTER BUTTON CLICK
def button_click():
    openai.api_key = "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"
    model = "davinci"
    question = input.get()
    response = openai.Completion.create(
        engine=model,
        prompt=(f"Question: {question}\n"
                "Answer:"
                ),
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )
    answer = response.choices[0].text.split('\n')[0]
    print(answer)

    label_3 = tkinter.Label(textvariable=answer)
    label_3.pack(side="bottom")

#BUTTON
search_button = tkinter.Button(text="SEARCH", command=button_click)
search_button.pack(side="right")

#QUESTION BOX
input = tkinter.Entry(width=250)
input.pack(side="left")
input.get()

window.mainloop()

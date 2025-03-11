messages=['mayday', 'panpan', 'securite']
sent_messages=[]

def show_messages(messages):
    for m in messages:
        print(f"{m}")


def sent_message(messages, sent_messages):
    while messages:
        temp = messages.pop()
        sent_messages.append(temp)

sent_message(messages[:], sent_messages)
print("\n")

show_messages(sent_messages)

print("\n")

show_messages(messages)
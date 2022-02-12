from twilio.rest import Client

from tkinter import *
root = Tk()
root.geometry('400x400+250+100')
root.configure(bg='#063f61') 
root.resizable(FALSE,FALSE)

small_font = ('Verdana',13)

input_user1 = StringVar()
input_user2 = StringVar()
input_user3 = StringVar()
input_user4 = StringVar()
input_user5 = StringVar()


def send_sms():
    account_sid = str(input_user1.get())
    print(account_sid)
    
    auth_token = str(input_user2.get())
    print(auth_token)
    
    TwilioNumber = str(input_user3.get())
    print(TwilioNumber)

    myPhone = str(input_user4.get())
    print(myPhone)
    
    subject = '\nMessage Body :\n' + str(input_user5.get())
    print(subject)
    #account_sid = 'AC4a25f05e82fad04fda0aa610ead17a1e'
    #auth_token = '16f3ebb1d43b92b28de84f0da177a159'
    #TwilioNumber = '+12242880806'
    #myPhone = '+2001229206963'
    
    client = Client(account_sid, auth_token)

    client.messages.create(
        to = myPhone,
        from_= TwilioNumber,
        body= subject
        )
    
    


main_label = Label(root,text='Send a Message',bg='#6dbefc',fg='#8c247b')
main_label.place(x=100,y=15)
main_label.config(font=("Comic Sans MS", 20))

a1_label = Label(root,text='Account sid',bg='#063f61',fg='#ddf21d')
a1_label.place(x=13,y=80)
a1_label.config(font=(20))

a2_label = Label(root,text='Auth Token',bg='#063f61',fg='#ddf21d')
a2_label.place(x=13,y=123)
a2_label.config(font=(20))

a3_label = Label(root,text='Twilio Number',bg='#063f61',fg='#ddf21d')
a3_label.place(x=13,y=163)
a3_label.config(font=(20))

a4_label = Label(root,text='To',bg='#063f61',fg='#ddf21d')
a4_label.place(x=13,y=203)
a4_label.config(font=(20))

a5_label = Label(root,text='Subject',bg='#063f61',fg='#ddf21d')
a5_label.place(x=13,y=243)
a5_label.config(font=(20))

a6_label = Label(root,text='Twilio APIs',bg='white',fg='green')
a6_label.place(x=9,y=373)
a6_label.config(font=(10))

title_programmer = Label(root,text='By Mohamed Emad, Member at IEEE. April 2020',
                         bg='green',fg='white'
                         )
title_programmer.config(font=("Comic Sans MS", 10))
title_programmer.pack(fill='x')
title_programmer.place(x=93,y=373)


b1_Entry = Entry(root, width=22,font=small_font,textvariable=input_user1)
b1_Entry.place(x=132,y=82)

b2_Entry = Entry(root,width=22,font=small_font,textvariable=input_user2)
b2_Entry.place(x=132,y=123)

b3_Entry = Entry(root,width=22,font=small_font,textvariable=input_user3)
b3_Entry.place(x=132,y=164)

b4_Entry = Entry(root,width=22,font=small_font,textvariable=input_user4)
b4_Entry.place(x=132,y=205)

b5_Entry = Entry(root,width=22,font=small_font,textvariable=input_user5)
b5_Entry.place(x=132,y=245)

s_button = Button(root,text='Send',width=12,
                  height=1,
                  bg='#99004d',
                  fg='white',
                  activebackground='#4d0026',
                  activeforeground='green',
                  command=send_sms
                  )
s_button.config(font=('Comic Sans MS',13))
s_button.place(x=235,y=300)



'''
account_sid = 'AC4a25f05e82fad04fda0aa610ead17a1e'
auth_token = '16f3ebb1d43b92b28de84f0da177a159'

myPhone = '+2001229206963'
TwilioNumber = '+12242880806'

client = Client(account_sid, auth_token)

client.messages.create(
    to = myPhone,
    from_=TwilioNumber,
    body='Hello Mohamed, I"m Python !'
    
    )

'''

root.mainloop()

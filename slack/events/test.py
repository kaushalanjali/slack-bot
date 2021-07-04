from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from slackclient import SlackClient   
import json
                            #1


SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)
SLACK_BOT_USER_TOKEN = getattr(settings,                          #2
'SLACK_BOT_USER_TOKEN', None)                                     #
Client = SlackClient(SLACK_BOT_USER_TOKEN)      
response = Client.api_call(
      "chat.update",
      channel=form_json["channel"]["id"],
      ts=form_json["message_ts"],
      text="One {}, right coming up! :coffee:".format(message_text),
      attachments=[] # empty `attachments` to clear the existing massage attachments
    )
class Events(APIView):
    def post(self, request, *args, **kwargs):
        slack_message=request.data

        #verify token
        if slack_message.get('token') !=SLACK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)

        #checking for url verification
        if slack_message.get('type')=='url_verification':
            return Response(data=slack_message, status=status.HTTP_200_OK)

        #send a greeting to the bot
        if 'event' in slack_message:
            #process message if event data is contained in it
            event_message=slack_message.get('event')
            
            #ignore bot's own message
            #if event_message.get('subtype')=='bot_message':
                #return Response(status=status.HTTP_200_OK)

            #handle the message by parsing the JSON data
            user=event_message.get('user')
            inputText=event_message.get('text')
            channel=event_message.get('channel')
            bot_text='Hi <@{}> :wave:'.format(user)
            intro_msg  = json.dumps([{"text":"Choose an action","fallback":"You are unable to choose an option","callback_id":"lunch_intro","color":"#3AA3E3","attachment_type":"default","actions":[{"name":"enroll","text":"Enroll","type":"button","value":"value"},{"name":"leave","text":"Leave","type":"button","value":"leave"}]}])

            #finally use the slack api to post the message with chat.postMessage

            responseData = {"hi":"Hi","hello":"Hello","hey":"Hey","hee":"hee"}

            staticWords = ["hi", "hello", "hey", "hee",]
            

            if 'bot_id' not in event_message:

                #if any(staticText in text.lower() for staticText in staticWords):
                for staticText in staticWords:
                    if staticText in inputText.lower():
                        bot_text=responseData[staticText]+' <@{}> :wave:'.format(user)
                        
                        Client.api_call(method='chat.postMessage',
                            channel=channel,
                            text=bot_text)
                        Client.api_call("chat.postMessage",
                             channel=channel, text="What would you like to do?", 
                             attachments=intro_msg, as_user=True)
                        return Response(status=status.HTTP_200_OK)


        return Response(status=status.HTTP_200_OK)
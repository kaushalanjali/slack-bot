from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from slackclient import SlackClient  
                             


SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)
SLACK_BOT_USER_TOKEN = getattr(settings,                          
'SLACK_BOT_USER_TOKEN', None)                                     
Client = SlackClient(SLACK_BOT_USER_TOKEN)                        


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

            #finally use the slack api to post the message with chat.postMessage

            responseData = {"hi":"Hi","hello":"Hello","hey":"Hey","hee":"hee",}
            staticWords = ["hi", "hello", "hey", "hee",]

            if 'bot_id' not in event_message:
                #if any(staticText in text.lower() for staticText in staticWords):
                for staticText in staticWords:
                    if staticText in inputText.lower():
                        bot_text=responseData[staticText]+' <@{}> :wave:'.format(user)
                        
                        Client.api_call(method='chat.postMessage',
                            channel=channel,
                            text=bot_text)
                        return Response(status=status.HTTP_200_OK)
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
            bot_newtext= 'you can use this to raise request for password reset'

            #finally use the slack api to post the message with chat.postMessage

            responseData = {"iam":"https://dis-support.thalesgroup.com/nav_to.do?uri=%2Fcom.glideapp.servicecatalog_cat_item_view.do%3Fv%3D1%26sysparm_id%3D220efceddb68a70027399334ca9619f7%26sysparm_link_parent%3Db3328925db4067005a599785ca9619c8%26sysparm_catalog%3D42226d4edbdcdf0084dd79e9bf961978%26sysparm_catalog_view%3Dcatalog_Data_Centers_Operations_Catalog"}
            staticWords = ["iam", "IAM",]

            if 'bot_id' not in event_message:
                #if any(staticText in text.lower() for staticText in staticWords):
                for staticText in staticWords:
                    if staticText in inputText.lower():
                        bot_newtext=bot_newtext+" <"+responseData[staticText]+"|IAM PASSWORD RESET>"
                        
                        Client.api_call(method='chat.postMessage',
                            channel=channel,
                            text=bot_newtext)
                        return Response(status=status.HTTP_200_OK)   
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
            bot_newtext1= 'you can use this to raise request for MFA reset'

            #finally use the slack api to post the message with chat.postMessage

            responseData = {"mfa":"https://dis-support.thalesgroup.com/nav_to.do?uri=%2Fcom.glideapp.servicecatalog_cat_item_view.do%3Fv%3D1%26sysparm_id%3D7aafbcaddb68a70027399334ca961982%26sysparm_link_parent%3Db3328925db4067005a599785ca9619c8%26sysparm_catalog%3D42226d4edbdcdf0084dd79e9bf961978%26sysparm_catalog_view%3Dcatalog_Data_Centers_Operations_Catalog"}
            staticWords = ["mfa", "MFA",]

            if 'bot_id' not in event_message:
                #if any(staticText in text.lower() for staticText in staticWords):
                for staticText in staticWords:
                    if staticText in inputText.lower():
                        bot_newtext1=bot_newtext1+" <"+responseData[staticText]+"|MFA RESET REQUEST>"
                        
                        Client.api_call(method='chat.postMessage',
                            channel=channel,
                            text=bot_newtext1)
                        return Response(status=status.HTTP_200_OK) 

        return Response(status=status.HTTP_200_OK)
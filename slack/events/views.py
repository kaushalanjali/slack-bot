from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from slackclient import SlackClient   
import json



SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)
SLACK_BOT_USER_TOKEN = getattr(settings,'SLACK_BOT_USER_TOKEN', None)                                     
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

            #handle the message by parsing the JSON data
            user=event_message.get('user')
            inputText=event_message.get('text')
            channel=event_message.get('channel')
            bot_text='Hi <@{}> :wave:'.format(user)
            bot_text_error='I dont understand what you trying to say please select option from above menu or type "hi" to move to main menu'

            intro_msg  = json.dumps([{
                                            "blocks": [
                                                {
                                                    "type": "header",
                                                    "text": {
                                                        "type": "plain_text",
                                                        "text": "These are the services we offer"
                                                    }
                                                },
                                                {
                                                    "type": "context",
                                                    "elements": [
                                                        {
                                                            "type": "image",
                                                            "image_url": "https://res.cloudinary.com/hy4kyit2a/f_auto,fl_lossy,q_70/learn/modules/aws-identity-and-access-management/get-to-know-aws-identity-and-access-management/images/a421b1d81a6b214c527699eb9f7a74d6_541-b-2-a-0-b-f-074-46-d-1-96-de-30-f-4082-fe-6-ba.png",
                                                            "alt_text": "IAM"
                                                        },
                                                        {
                                                            "type": "mrkdwn",
                                                            "text": "*IAM*"
                                                        },
                                                        {
                                                            "type": "image",
                                                            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3Jl8AWlnTNPFgO7Q9IAR8LQs6Czp06vwOTw&usqp=CAU",
                                                            "alt_text": "SNOW"
                                                        },
                                                        {
                                                            "type": "mrkdwn",
                                                            "text": "*CONFLUENCE*"
                                                        },
                                                        {
                                                            "type": "image",
                                                            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/AWS_Simple_Icons_Virtual_Private_Cloud.svg/60px-AWS_Simple_Icons_Virtual_Private_Cloud.svg.png",
                                                            "alt_text": "VPC"
                                                        },
                                                        {
                                                            "type": "mrkdwn",
                                                            "text": "*VPC*"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "type": "section",
                                                    "text": {
                                                        "type": "plain_text",
                                                        "text": "Please type service to move forword",
                                                    }
                                                }
                                            ]
                                        }])

            #finally use the slack api to post the message with chat.postMessage
            responseData = {"hi":"Hi","hello":"Hello","hey":"Hey","hee":"hee"}
            staticWords = ["hi", "hello", "hey", "hee"]   


            #Get Second Message
            #responseData1 = {"snow":"SNOW"}
            staticWords1 = ["snow"]
            intro_msg1  = json.dumps([{
                                        "blocks": [
                                            {
                                                "type": "header",
                                                "text": {
                                                    "type": "plain_text",
                                                    "text": "These are the services we offer in snow"
                                                }
                                            },
                                            {
                                                "type": "context",
                                                "elements": [
                                                    {
                                                        "type": "image",
                                                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDMs6ajGpkHhbIVhegTQXVdTlePNwKtlY_ZA&usqp=CAU",
                                                        "alt_text": "cute cat"
                                                    },
                                                    {
                                                        "type": "mrkdwn",
                                                        "text": "*Identity Access Management*"
                                                    },
                                                    {
                                                        "type": "image",
                                                        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/AWS_Simple_Icons_Virtual_Private_Cloud.svg/60px-AWS_Simple_Icons_Virtual_Private_Cloud.svg.png",
                                                        "alt_text": "SNOW"
                                                    },
                                                    {
                                                        "type": "mrkdwn",
                                                        "text": "*Virtual Private Cloud*"
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "context",
                                                "elements": [
                                                    {
                                                        "type": "plain_text",
                                                        "text": "Please trype service to move forowrd",
                                                    }
                                                ]
                                            }
                                        ]
                                    }])


            
            staticWords2 = ["confluence"]
            intro_msg2 = json.dumps([{
                                    "blocks": [
                                        {
                                            "type": "header",
                                            "text": {
                                                "type": "plain_text",
                                                "text": "These are the listed teams in confluence"
                                            }
                                        },
                                        {
                                            "type": "section",
                                            "text": {
                                                "type": "mrkdwn",
                                                "text": "Operations, Support & Governance \n \n <https://confluence.gemalto.com/pages/viewpage.action?pageId=314050718 | CONFLUENCE LINK TO OPERATION'S PAGE> "
                                            },
                                            "accessory": {
                                                "type": "image",
                                                "image_url": "https://www.acps.k12.va.us/cms/lib/VA01918616/Centricity/shared/images/Effective_Efficient_Operations_icon.png",
                                                "alt_text": "operations"
                                            }
                                        },
                                        {
                                            "type": "divider"
                                        },
                                        {
                                            "type": "section",
                                            "text": {
                                                "type": "mrkdwn",
                                                "text": "Site Reliability support \n \n <https://confluence.gemalto.com/pages/viewpage.action?spaceKey=COPS&title=%5BAWS%5D+Site+Reliability+Engineering | CONFLUENCE LINK TO SRE PAGE> "
                                            },
                                            "accessory": {
                                                "type": "image",
                                                "image_url": "https://vorozhko.net/wp-content/uploads/2020/06/DevOps_google-825x510.jpg",
                                                "alt_text": "SRE"
                                            }
                                        },
                                        {
                                            "type": "divider"
                                        },
                                        {
                                            "type": "section",
                                            "text": {
                                                "type": "mrkdwn",
                                                "text": "Network, Security, Risk & Compliance \n \n <https://confluence.gemalto.com/pages/viewpage.action?pageId=255329157 | CONFLUENCE LINK TO SECURITY PAGE> "
                                            },
                                            "accessory": {
                                                "type": "image",
                                                "image_url": "https://www.nicepng.com/png/full/189-1891872_information-security-team-icon.png",
                                                "alt_text": "SRE"
                                            }
                                        },
                                        {
                                            "type": "divider"
                                        },
                                        {
                                            "type": "section",
                                            "text": {
                                                "type": "mrkdwn",
                                                "text": "Finance & PreSales \n \n <https://confluence.gemalto.com/pages/viewpage.action?pageId=283509931 | CONFLUENCE LINK TO FINANCE & PRESALES PAGE> "
                                            },
                                            "accessory": {
                                                "type": "image",
                                                "image_url": "https://cdn3.iconfinder.com/data/icons/business-people-forex/512/investors-512.png",
                                                "alt_text": "SRE"
                                            }
                                        },
                                        {
                                            "type": "divider"
                                        }
                                    ]
                                }])


            staticWords3 = ["iam", "iam",]
            bot_text3 = 'Thanks for contacting thales bot'
            intro_msg3 = json.dumps([{
                            "blocks": [
                                {
                                    "type": "header",
                                    "text": {
                                        "type": "plain_text",
                                        "text": "These are the services we offer for IAM"
                                    }
                                },
                                {
                                    "type": "context",
                                    "elements": [
                                        {
                                            "type": "mrkdwn",
                                            "text": "*IAM USER CREATION*"
                                        }
                                    ]
                                },
                                {
                                    "type": "section",
                                    "text": {
                                        "type": "mrkdwn",
                                        "text": "Service Request to create your IAM user account on Thales-AWS infrastructure \n <https://confluence.gemalto.com/display/COPS/User+Management+-+Overview | CONFLUENCE LINK TO CREATE IAM USER>"
                                    },
                                    "accessory": {
                                        "type": "image",
                                        "image_url": "https://i.ibb.co/ky0KJLZ/f4d50165db4067005a599785ca961987.png",
                                        "alt_text": "iam user creation"
                                    }
                                },
                                {
                                    "type": "section",
                                    "text": {
                                        "type": "mrkdwn",
                                        "text": " _Click button to move to service catalog_ "
                                    },
                                    "accessory": {
                                        "type": "button",
                                        "text": {
                                            "type": "plain_text",
                                            "text": "IAM USER CREATION"
                                        },
                                        "value": "click_me_123",
                                        "action_id": "button-action",
                                        "url": "https://dis-support.thalesgroup.com/nav_to.do?uri=%2Fcom.glideapp.servicecatalog_cat_item_view.do%3Fv%3D1%26sysparm_id%3D9d438d29db4067005a599785ca961973%26sysparm_link_parent%3Db3328925db4067005a599785ca9619c8%26sysparm_catalog%3D42226d4edbdcdf0084dd79e9bf961978%26sysparm_catalog_view%3Dcatalog_Data_Centers_Operations_Catalog"
                                    }
                                },
                                {
                                    "type": "divider"
                                },
                                {
                                    "type": "context",
                                    "elements": [
                                        {
                                            "type": "mrkdwn",
                                            "text": "*IAM PASSWORD RESET *"
                                        }
                                    ]
                                },
                                {
                                    "type": "section",
                                    "text": {
                                        "type": "mrkdwn",
                                        "text": " \n Open this Service Request to manage CloudHealth access for AWS Account(s) on Thales-AWS infrastructure"
                                    },
                                    "accessory": {
                                        "type": "image",
                                        "image_url": "https://icon-library.com/images/reset-password-icon/reset-password-icon-29.jpg",
                                        "alt_text": "iam password reset"
                                    }
                                },
                                {
                                    "type": "section",
                                    "text": {
                                        "type": "mrkdwn",
                                        "text": "_Click button to move to service catalog_   "
                                    },
                                    "accessory": {
                                        "type": "button",
                                        "text": {
                                            "type": "plain_text",
                                            "text": "IAM PASSWORD RESET"
                                        },
                                        "value": "click_me_123",
                                        "action_id": "button-action",
                                        "url": "https://dis-support.thalesgroup.com/nav_to.do?uri=%2Fcom.glideapp.servicecatalog_cat_item_view.do%3Fv%3D1%26sysparm_id%3D0e840a51db710c10f68fd1274896192b%26sysparm_link_parent%3Db3328925db4067005a599785ca9619c8%26sysparm_catalog%3D42226d4edbdcdf0084dd79e9bf961978%26sysparm_catalog_view%3Dcatalog_Data_Centers_Operations_Catalog"
                                    }
                                },
                                {
                                    "type": "divider"
                                },
                                {
                                    "type": "context",
                                    "elements": [
                                        {
                                            "type": "mrkdwn",
                                            "text": "*MFA RESET*"
                                        }
                                    ]
                                },
                                {
                                    "type": "section",
                                    "text": {
                                        "type": "mrkdwn",
                                        "text": " \n Service Request to Enable/Disable Datadog user(s) account(s) on Thales-AWS infrastructure"
                                    },
                                    "accessory": {
                                        "type": "image",
                                        "image_url": "https://res.cloudinary.com/hy4kyit2a/f_auto,fl_lossy,q_70/learn/modules/aws-cloud-security/control-access-with-aws-identity-and-access-management/images/79b38ddd6c48c644b091547739d1d5ef_90-f-568-fd-d-90-d-4-ebb-a-710-4-e-9-fb-41-ba-1-c-6.png",
                                        "alt_text": "mfa reset"
                                    }
                                },
                                {
                                    "type": "section",
                                    "text": {
                                        "type": "mrkdwn",
                                        "text": "_Click button to move to service catalog_   "
                                    },
                                    "accessory": {
                                        "type": "button",
                                        "text": {
                                            "type": "plain_text",
                                            "text": "MFA RESET"
                                        },
                                        "value": "click_me_123",
                                        "action_id": "button-action",
                                        "url": "https://dis-support.thalesgroup.com/nav_to.do?uri=%2Fcom.glideapp.servicecatalog_cat_item_view.do%3Fv%3D1%26sysparm_id%3D14569155dbbdc810f68fd1274896196b%26sysparm_link_parent%3Db3328925db4067005a599785ca9619c8%26sysparm_catalog%3D42226d4edbdcdf0084dd79e9bf961978%26sysparm_catalog_view%3Dcatalog_Data_Centers_Operations_Catalog"
                                    }
                                },
                                {
                                    "type": "divider"
                                }
                            ]
                        }])

            bot_text4 = 'Thanks for contacting thales bot'
            staticWords4 = ["vpc", "VPC",]
            intro_msg5 = json.dumps([{
                                        "blocks": [
                                            {
                                                "type": "header",
                                                "text": {
                                                    "type": "plain_text",
                                                    "text": "These are the services we offer for VPC"
                                                }
                                            },
                                            {
                                                "type": "context",
                                                "elements": [
                                                    {
                                                        "type": "mrkdwn",
                                                        "text": "*NEW VPC ACCOUNT CREATION*"
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "section",
                                                "text": {
                                                    "type": "mrkdwn",
                                                    "text": "Service request to create new VPC under AWS account. \n <https://confluence.gemalto.com/dologin.action| CONFLUENCE LINK VPC CREATION>"
                                                },
                                                "accessory": {
                                                    "type": "image",
                                                    "image_url": "https://i.ibb.co/HqJS5G5/691e5b88db7650500f80d3ca4b96196f.png",
                                                    "alt_text": "vpc creation"
                                                }
                                            },
                                            {
                                                "type": "section",
                                                "text": {
                                                    "type": "mrkdwn",
                                                    "text": " _Click button to move to service catalog_  "
                                                },
                                                "accessory": {
                                                    "type": "button",
                                                    "text": {
                                                        "type": "plain_text",
                                                        "text": "VPC CREATION"
                                                    },
                                                    "value": "click_me_123",
                                                    "action_id": "button-action",
                                                    "url": "https://dis-support.thalesgroup.com/nav_to.do?uri=/com.glideapp.servicecatalog_cat_item_view.do?v=1&sysparm_id=f27899b2db7de70027399334ca961912&sysparm_link_parent=c470303adbf9e70027399334ca9619fd&sysparm_catalog=42226d4edbdcdf0084dd79e9bf961978&sysparm_catalog_view=catalog_Data_Centers_Operations_Catalog"
                                                }
                                            },
                                            {
                                                "type": "divider"
                                            }
                                        ]
                                    }])


            if 'bot_id' not in event_message:
                #if any(staticText in text.lower() for staticText in staticWords):
                ##### API for HI ##########################
                for staticText in staticWords:
                    if staticText in inputText.lower():
                        bot_text=responseData[staticText]+' <@{}> :wave:'.format(user)
                        Client.api_call(method='chat.postMessage',
                            channel=channel,
                            text=bot_text)
                        Client.api_call("chat.postMessage",
                             channel=channel, text="*How may i help you??*", 
                             attachments=intro_msg, as_user=True)
                        return Response(status=status.HTTP_200_OK)  

                ################ API for snow ############################
                for staticText in staticWords1:
                    if staticText in inputText.lower():

                        Client.api_call("chat.postMessage",
                             channel=channel, 
                             attachments=intro_msg1, as_user=True)
                        return Response(status=status.HTTP_200_OK)

                ###API for AIM ##############################
                for staticText in staticWords3:
                    if staticText in inputText.lower():                      
                        Client.api_call("chat.postMessage",
                             channel=channel,
                             attachments=intro_msg3, as_user=True)
                        Client.api_call(method='chat.postMessage',
                            channel=channel,
                            text=bot_text4)                        
                        return Response(status=status.HTTP_200_OK)
                ###API for VPC ##############################
                for staticText in staticWords4:
                    if staticText in inputText.lower():                      
                        Client.api_call("chat.postMessage",
                             channel=channel,
                             attachments=intro_msg5, as_user=True)
                        Client.api_call(method='chat.postMessage',
                            channel=channel,
                            text=bot_text3)                        
                        return Response(status=status.HTTP_200_OK)
                    ### API for conflunce###########################
                for staticText in staticWords2:
                    if staticText in inputText.lower():                      
                        Client.api_call("chat.postMessage",
                             channel=channel, text="*Type service to move forword*", 
                             attachments=intro_msg2, as_user=True)
                       
                        Client.api_call(method='chat.postMessage',
                            channel=channel,
                            text=bot_text3)                        
                        return Response(status=status.HTTP_200_OK)
        
 
                    else:

                        Client.api_call(method='chat.postMessage',
                            channel=channel,
                            text=bot_text_error)                     
                        return Response(status=status.HTTP_200_OK)          
        return Response(status=status.HTTP_200_OK)          
           



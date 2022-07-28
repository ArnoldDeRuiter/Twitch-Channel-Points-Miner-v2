

***********



[{"operationName":"UpdateCommunityPointsLastViewedContent","variables":{"input":{"channelID":"140918389","viewedContent":["AUTOMATIC_REWARD","CUSTOM_REWARD"]}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"ae490fa8c1c284f6da9e43f0e7b6418100d887de8dd62ef2a08e320b8b75c1cf"}}}]


https://gql.twitch.tv/gql#origin=twilight

*/*/*/


https://gql.twitch.tv/gql#origin=twilight


[{"operationName":"RedeemCustomReward","variables":{"input":{"channelID":"140918389","cost":151,"prompt":"A wild Snubbull appeared on the screen, try and catch it!","rewardID":"d061dd74-166d-40f1-bf68-d82244bc59be","title":"Catch the Snubbull!","transactionID":"79a47c8421f4a75e9378e8f5aa2fefe0"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"d56249a7adb4978898ea3412e196688d4ac3cea1c0c2dfd65561d229ea5dcc42"}}}]


curl 'https://gql.twitch.tv/gql#origin=twilight' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H 'Accept: */*' -H 'Accept-Language: en-US' -H 'Accept-Encoding: gzip, deflate, br' -H 'Referer: https://www.twitch.tv/' -H 'Client-Id: kimne78kx3ncx6brgo4mv6wki5h1ko' -H 'X-Device-Id: 597203908bf58592' -H 'Client-Version: 1ad44d1e-7760-485b-b2c0-4dc85ac42995' -H 'Client-Session-Id: 4418d555614d425e' -H 'Authorization: OAuth wqbf1tojzliqlnd9po7opdgpu1ju9v' -H 'Content-Type: text/plain;charset=UTF-8' -H 'Origin: https://www.twitch.tv' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'Sec-GPC: 1' --data-raw '[{"operationName":"RedeemCustomReward","variables":{"input":{"channelID":"140918389","cost":151,"prompt":"A wild Snubbull appeared on the screen, try and catch it!","rewardID":"d061dd74-166d-40f1-bf68-d82244bc59be","title":"Catch the Snubbull!","transactionID":"79a47c8421f4a75e9378e8f5aa2fefe0"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"d56249a7adb4978898ea3412e196688d4ac3cea1c0c2dfd65561d229ea5dcc42"}}}]'



==================================



https://gql.twitch.tv/gql#origin=twilight


[{"operationName":"RedeemCustomReward","variables":{"input":{"channelID":"140918389","cost":151,"prompt":"A wild Cubone appeared on the screen, try and catch it!","rewardID":"d061dd74-166d-40f1-bf68-d82244bc59be","title":"Catch the Cubone!","transactionID":"7d0bb11221a6b77cec2ddd5c0d90915a"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"d56249a7adb4978898ea3412e196688d4ac3cea1c0c2dfd65561d229ea5dcc42"}}}]


POST /gql HTTP/1.1
Host: gql.twitch.tv
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US
Accept-Encoding: gzip, deflate, br
Referer: https://www.twitch.tv/
Client-Id: kimne78kx3ncx6brgo4mv6wki5h1ko
X-Device-Id: 597203908bf58592
Client-Version: 1ad44d1e-7760-485b-b2c0-4dc85ac42995
Client-Session-Id: 4418d555614d425e
Authorization: OAuth wqbf1tojzliqlnd9po7opdgpu1ju9v
Content-Type: text/plain;charset=UTF-8
Origin: https://www.twitch.tv
Content-Length: 421
DNT: 1
Connection: keep-alive
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Sec-GPC: 1


curl 'https://gql.twitch.tv/gql#origin=twilight' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H 'Accept: */*' -H 'Accept-Language: en-US' -H 'Accept-Encoding: gzip, deflate, br' -H 'Referer: https://www.twitch.tv/' -H 'Client-Id: kimne78kx3ncx6brgo4mv6wki5h1ko' -H 'X-Device-Id: 597203908bf58592' -H 'Client-Version: 1ad44d1e-7760-485b-b2c0-4dc85ac42995' -H 'Client-Session-Id: 4418d555614d425e' -H 'Authorization: OAuth wqbf1tojzliqlnd9po7opdgpu1ju9v' -H 'Content-Type: text/plain;charset=UTF-8' -H 'Origin: https://www.twitch.tv' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'Sec-GPC: 1' --data-raw '[{"operationName":"RedeemCustomReward","variables":{"input":{"channelID":"140918389","cost":151,"prompt":"A wild Cubone appeared on the screen, try and catch it!","rewardID":"d061dd74-166d-40f1-bf68-d82244bc59be","title":"Catch the Cubone!","transactionID":"7d0bb11221a6b77cec2ddd5c0d90915a"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"d56249a7adb4978898ea3412e196688d4ac3cea1c0c2dfd65561d229ea5dcc42"}}}]'


HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 239
Content-Type: application/json
Access-Control-Allow-Origin: *
Date: Thu, 28 Jul 2022 20:24:53 GMT
Timing-Allow-Origin: *


await fetch("https://gql.twitch.tv/gql#origin=twilight", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Accept": "*/*",
        "Accept-Language": "en-US",
        "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
        "X-Device-Id": "597203908bf58592",
        "Client-Version": "1ad44d1e-7760-485b-b2c0-4dc85ac42995",
        "Client-Session-Id": "4418d555614d425e",
        "Authorization": "OAuth wqbf1tojzliqlnd9po7opdgpu1ju9v",
        "Content-Type": "text/plain;charset=UTF-8",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1"
    },
    "referrer": "https://www.twitch.tv/",
    "body": "[{\"operationName\":\"RedeemCustomReward\",\"variables\":{\"input\":{\"channelID\":\"140918389\",\"cost\":151,\"prompt\":\"A wild Cubone appeared on the screen, try and catch it!\",\"rewardID\":\"d061dd74-166d-40f1-bf68-d82244bc59be\",\"title\":\"Catch the Cubone!\",\"transactionID\":\"7d0bb11221a6b77cec2ddd5c0d90915a\"}},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"d56249a7adb4978898ea3412e196688d4ac3cea1c0c2dfd65561d229ea5dcc42\"}}}]",
    "method": "POST",
    "mode": "cors"
});



[{"data":{"redeemCommunityPointsCustomReward":{"error":null,"__typename":"RedeemCommunityPointsCustomRewardPayload"}},"extensions":{"durationMilliseconds":141,"operationName":"RedeemCustomReward","requestID":"01G937QJ7MJHTJB7GA5DXK71MB"}}] 
 
 =========================
 
 json_data = copy.deepcopy(GQLOperations.ChannelPointsContext)
        json_data["variables"] = {"channelLogin": streamer.username}

        response = self.post_gql_request(json_data)
        if response != {}:
            # This if response is None just check for Offline channels... The thing is, we don't care if it's "offline".
            # if response["data"]["community"] is None:
            #     raise StreamerDoesNotExistException
            channel = response["data"]["community"]["channel"]

            channelCustomRewards = channel["communityPointsSettings"]["customRewards"]
            pprint(channel["communityPointsSettings"]["customRewards"])

            logger.info(
                f"Poggers!22"
            )
            pprint(streamer)
            for channelReward in channelCustomRewards:
                pprint(channelReward["title"])
                if (channelReward["title"].__contains__("Catch the")):
                    pprint(channelReward)
                    self.redeem_custom_channel_reward(streamer, channelReward["id"])

----
for loop output some
{'id': '514e7f8f-017b-4f5e-b88f-7c26490d0e73', 'backgroundColor': '#EFB700', 'cooldownExpiresAt': None, 'cost': 2500, 'defaultImage': {'url': 'https://static-cdn.jtvnw.net/custom-reward-images/default-1.png', 'url2x': 'https://static-cdn.jtvnw.net/custom-reward-images/default-2.png', 'url4x': 'https://static-cdn.jtvnw.net/custom-reward-images/default-4.png', '__typename': 'CommunityPointsImage'}, 'image': {'url': 'https://static-cdn.jtvnw.net/custom-reward-images/140918389/514e7f8f-017b-4f5e-b88f-7c26490d0e73/39fa8529-063f-41a2-8290-f24853deef99/custom-1.png', 'url2x': 'https://static-cdn.jtvnw.net/custom-reward-images/140918389/514e7f8f-017b-4f5e-b88f-7c26490d0e73/39fa8529-063f-41a2-8290-f24853deef99/custom-2.png', 'url4x': 'https://static-cdn.jtvnw.net/custom-reward-images/140918389/514e7f8f-017b-4f5e-b88f-7c26490d0e73/39fa8529-063f-41a2-8290-f24853deef99/custom-4.png', '__typename': 'CommunityPointsImage'}, 'maxPerStreamSetting': {'isEnabled': False, 'maxPerStream': 0, '__typename': 'CommunityPointsCustomRewardMaxPerStreamSetting'}, 'maxPerUserPerStreamSetting': {'isEnabled': False, 'maxPerUserPerStream': 0, '__typename': 'CommunityPointsCustomRewardMaxPerUserPerStreamSetting'}, 'globalCooldownSetting': {'isEnabled': True, 'globalCooldownSeconds': 60, '__typename': 'CommunityPointsCustomRewardGlobalCooldownSetting'}, 'isEnabled': True, 'isInStock': True, 'isPaused': False, 'isSubOnly': False, 'isUserInputRequired': False, 'shouldRedemptionsSkipRequestQueue': True, 'redemptionsRedeemedCurrentStream': None, 'prompt': "It's either a tasty treat or a disgusting punishment. If you're out of Friend Points: also automatically redeemed upon subscriptions!", 'title': "It's Bean Time!", 'updatedForIndicatorAt': '2022-06-07T16:40:00.027951858Z', '__typename': 'CommunityPointsCustomReward'}

{'id': 'd061dd74-166d-40f1-bf68-d82244bc59be', 'backgroundColor': '#EFB700', 'cooldownExpiresAt': None, 'cost': 151, 'defaultImage': {'url': 'https://static-cdn.jtvnw.net/custom-reward-images/default-1.png', 'url2x': 'https://static-cdn.jtvnw.net/custom-reward-images/default-2.png', 'url4x': 'https://static-cdn.jtvnw.net/custom-reward-images/default-4.png', '__typename': 'CommunityPointsImage'}, 'image': {'url': 'https://static-cdn.jtvnw.net/custom-reward-images/140918389/d061dd74-166d-40f1-bf68-d82244bc59be/a3de5bdb-4360-4a12-beca-599e05ee90cd/custom-1.png', 'url2x': 'https://static-cdn.jtvnw.net/custom-reward-images/140918389/d061dd74-166d-40f1-bf68-d82244bc59be/a3de5bdb-4360-4a12-beca-599e05ee90cd/custom-2.png', 'url4x': 'https://static-cdn.jtvnw.net/custom-reward-images/140918389/d061dd74-166d-40f1-bf68-d82244bc59be/a3de5bdb-4360-4a12-beca-599e05ee90cd/custom-4.png', '__typename': 'CommunityPointsImage'}, 'maxPerStreamSetting': {'isEnabled': False, 'maxPerStream': 0, '__typename': 'CommunityPointsCustomRewardMaxPerStreamSetting'}, 'maxPerUserPerStreamSetting': {'isEnabled': False, 'maxPerUserPerStream': 0, '__typename': 'CommunityPointsCustomRewardMaxPerUserPerStreamSetting'}, 'globalCooldownSetting': {'isEnabled': True, 'globalCooldownSeconds': 5, '__typename': 'CommunityPointsCustomRewardGlobalCooldownSetting'}, 'isEnabled': True, 'isInStock': True, 'isPaused': True, 'isSubOnly': False, 'isUserInputRequired': False, 'shouldRedemptionsSkipRequestQueue': False, 'redemptionsRedeemedCurrentStream': None, 'prompt': 'When a Pokémon apprears on the screen you can use this reward to try and catch it!', 'title': 'Catch the Pokémon!', 'updatedForIndicatorAt': '2022-07-23T10:48:45.567285246Z', '__typename': 'CommunityPointsCustomReward'}
----


{'__typename': 'Channel',
 'communityPointsSettings': 

    {'__typename': 'CommunityPointsChannelSettings',
    'automaticRewards': [{'__typename': 'CommunityPointsAutomaticReward',
                        'backgroundColor': None,

 //CommunityPointsAutomaticReward

'customRewards': 
    [{'__typename': 'CommunityPointsCustomReward',
    
'backgroundColor': '#FE295C',
'cooldownExpiresAt': None,
'cost': 200000,
'defaultImage': {'__typename': 'CommunityPointsImage',
                    'url': 'https://static-cdn.jtvnw.net/custom-reward-images/default-1.png',
                    'url2x': 'https://static-cdn.jtvnw.net/custom-reward-images/default-2.png',
                    'url4x': 'https://static-cdn.jtvnw.net/custom-reward-images/default-4.png'},
'globalCooldownSetting': {'__typename': 'CommunityPointsCustomRewardGlobalCooldownSetting',
                            'globalCooldownSeconds': 60,
                            'isEnabled': False},
'id': '34a25ae4-4f4d-4b67-8e36-8a8cd2f8025a',
'image': None,
'isEnabled': True,
'isInStock': True,
'isPaused': False,
'isSubOnly': False,
'isUserInputRequired': False,
'maxPerStreamSetting': {'__typename': 'CommunityPointsCustomRewardMaxPerStreamSetting',
                        'isEnabled': False,
                        'maxPerStream': 100},
'maxPerUserPerStreamSetting': {'__typename': 'CommunityPointsCustomRewardMaxPerUserPerStreamSetting',
                                'isEnabled': False,
                                'maxPerUserPerStream': 5},
'prompt': 'Powered by Blerp - '
            'https://blerp.com/soundbites/5d014c83531c0d0006227f03',
'redemptionsRedeemedCurrentStream': None,
'shouldRedemptionsSkipRequestQueue': False,
'title': 'You are not very '
            'good',
'updatedForIndicatorAt': '2022-06-22T23:07:53.937710584Z'},


{'__typename': 'CommunityPointsCustomReward',
'backgroundColor': '#AE1392',
'cooldownExpiresAt': None,
'cost': 10000000,
'defaultImage': {'__typename': 'CommunityPointsImage',
                    'url': 'https://static-cdn.jtvnw.net/custom-reward-images/default-1.png',
                    'url2x': 'https://static-cdn.jtvnw.net/custom-reward-images/default-2.png',
                    'url4x': 'https://static-cdn.jtvnw.net/custom-reward-images/default-4.png'},
'globalCooldownSetting': {'__typename': 'CommunityPointsCustomRewardGlobalCooldownSetting',
                            'globalCooldownSeconds': 0,
                            'isEnabled': False},
'id': '38cea247-1e53-4e92-ab9e-5235f8def510',
'image': None,
'isEnabled': True,
'isInStock': True,
'isPaused': False,
'isSubOnly': False,
'isUserInputRequired': False,
'maxPerStreamSetting': {'__typename': 'CommunityPointsCustomRewardMaxPerStreamSetting',
                        'isEnabled': False,
                        'maxPerStream': 0},
'maxPerUserPerStreamSetting': {'__typename': 'CommunityPointsCustomRewardMaxPerUserPerStreamSetting',
                                'isEnabled': False,
                                'maxPerUserPerStream': 0},
'prompt': "We'll do a round of "
            'fall guys with a '
            'viewer lobby',
'redemptionsRedeemedCurrentStream': None,
'shouldRedemptionsSkipRequestQueue': False,
'title': 'Fall Guys with '
            'viewers round',
'updatedForIndicatorAt': '2022-06-26T15:07:00.635269788Z'},












-----------







Message: '+12 → Streamer(username=waldoandfriends, channel_id=140918389, channel_points=8.55k) - Reason: WATCH.'
Arguments: None
{'message': '{"type":"viewcount","server_time":1658870490.164544,"viewers":7}',
 'topic': 'video-playback-by-id.140918389'}
26/07/22 23:21:30 - INFO - [on_message]: Poggers!
{'message': '{"type":"viewcount","server_time":1658870520.248006,"viewers":7}',
 'topic': 'video-playback-by-id.140918389'}
26/07/22 23:22:00 - INFO - [on_message]: Poggers!
{'message': '{"type":"viewcount","server_time":1658870550.262936,"viewers":7}',
 'topic': 'video-playback-by-id.140918389'}
26/07/22 23:22:30 - INFO - [on_message]: Poggers!
{'message': '{"type":"global-last-viewed-content-updated","data":{"timestamp":"2022-07-26T21:22:43.169452147Z","global_last_viewed_content":{"user_id":"158691158","last_viewed_content":[{"content_type":"AUTOMATIC_REWARD","content_id":"SINGLE_MESSAGE_BYPASS_SUB_MODE","last_viewed_at":"2022-01-07T17:23:00.398067354Z"},{"content_type":"AUTOMATIC_REWARD","content_id":"SEND_HIGHLIGHTED_MESSAGE","last_viewed_at":"2022-07-26T17:09:16.492080207Z"},{"content_type":"AUTOMATIC_REWARD","content_id":"RANDOM_SUB_EMOTE_UNLOCK","last_viewed_at":"2022-01-07T17:23:00.398067354Z"},{"content_type":"AUTOMATIC_REWARD","content_id":"CHOSEN_SUB_EMOTE_UNLOCK","last_viewed_at":"2022-07-26T17:09:16.492080207Z"},{"content_type":"AUTOMATIC_REWARD","content_id":"CHOSEN_MODIFIED_SUB_EMOTE_UNLOCK","last_viewed_at":"2022-07-26T17:09:16.492080207Z"}]}}}',
 'topic': 'community-points-user-v1.158691158'}
26/07/22 23:22:43 - INFO - [on_message]: Poggers!
{'message': '{"type":"channel-last-viewed-content-updated","data":{"timestamp":"2022-07-26T21:22:43.169452147Z","channel_last_viewed_content":{"user_id":"158691158","channel_id":"140918389","last_viewed_content":[{"content_type":"AUTOMATIC_REWARD","last_viewed_at":"2022-07-26T21:22:43.161843855Z"},{"content_type":"CUSTOM_REWARD","last_viewed_at":"2022-07-26T21:22:43.161843855Z"}]}}}',
 'topic': 'community-points-user-v1.158691158'}
26/07/22 23:22:43 - INFO - [on_message]: Poggers!
{'message': '{"type":"viewcount","server_time":1658870580.255973,"viewers":7}',
 'topic': 'video-playback-by-id.140918389'}
26/07/22 23:23:00 - INFO - [on_message]: Poggers!

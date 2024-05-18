import json

#JSON ファイルの読み込み
with open('application_default_credentials.json', 'r') as f:
    json_dict = json.load(f)
print('json_dict:{}'.format(type(json_dict)))
print(f'json_dict:\n{json_dict}')

#JSON データの変換
print('-----辞書型から JSON 形式の文字列へ変換-----')
json_str = json.dumps(json_dict)
print('json_str:{}'.format(type(json_str)))
print(f'json_str:\n{json_str}')

print('-----JSON 形式の文字列から辞書型へ変換-----')
json_dict2 = json.loads(json_str)
print('json_dict2:{}'.format(type(json_dict2)))
print(f'json_dict2:\n{json_dict2}')

#JSON データの書き込み
with open('test2.json', 'w') as f2:
    json.dump(json_dict2, f2)
with open('test2.json','r') as f3:
    f3_dict = json.load(f3)
print(f"f3_dict:\n{f3_dict}")

'''
{
    "account": "",
    "client_id": "764086051850-6qr4p6gpi6hn506pt8ejuq83di341hur.apps.googleusercontent.com",
    "client_secret": "d-FL95Q19q7MQmFpd7hHD0Ty",
    "quota_project_id": "superb-runner-423503-c2",
    "refresh_token": "1//0eF3EqrAQ6qpQCgYIARAAGA4SNwF-L9Ir1-XgqjsK_ktYWgxHxkjeUPCYOwqXgUIdqZiCRb3VL1aJ4ki3HIWdZT0H6YM-NKQ_rSw",
    "type": "authorized_user",
    "universe_domain": "googleapis.com"
}
'''

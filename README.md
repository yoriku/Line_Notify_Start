# Line_Notify_Start
 
## API
``` Python
send_line(message, file_path=None, api_key=None, api_file=None)
```

- message (Required) : メッセージの内容
- file_path (Option, default=None) : メッセージに添付する画像のファイルパス
- api_key (Option, default=None) : API KEYの値そのまま（e.g. sodigerisbje0s9r...）
- api_file (Option, default=None) : API KEYが記載されたファイルのパス（api_keyよりこちらを推奨）

api_keyかapi_fileのいずれかは必須

# Eメールコマンド実行(Ansibleb版)

メールを受信すると、本文に記載されているコマンド列を、
サーバ上で実行し、実行結果の出力をメールで返信する

## 実行方法

インベントリファイルを指定して実行する。

```sh:
$ ansible-playbook -i hosts site.yml
```

コマンド実行の対象となるノードは、インベントリに登録されている必要がある


## 必要なPyPIパッケージ

- easyimap

## 設定方法

IMAPの接続情報はimap_conf.ymlに記述する。

パラメータは以下のとおり

- imap_server: IMAPサーバー名(必須)
- imap_username: IMAPアカウントユーザー名(必須)
- imap_password: IMAPアカウントパスワード(必須)
- imap_mailbox: チェックするメールボックス名(オプショナル: デフォルトはINBOX)
- imap_ssl: SSL接続するかどうか(オプショナル: デフォルトはtrue)
- imap_port: IMAPサーバの接続先ポート番号(オプショナル: デフォルトは993)

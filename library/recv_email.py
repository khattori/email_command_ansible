#!/usr/bin/env python
import easyimap

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            server=dict(required=True),
            username=dict(required=True),
            password=dict(required=True, no_log=True),
            mailbox=dict(requied=False, default='INBOX'),
            ssl=dict(required=False, type=bool, default=True),
            port=dict(required=False, type=int, default=993)
        )
    )
    server = module.params['server']
    user = module.params['username']
    password = module.params['password']
    mailbox = module.params['mailbox']
    ssl = module.params['ssl']
    port = module.params['port']
    imapper = None
    try:
        imapper = easyimap.connect(server, user, password, mailbox, ssl=ssl, port=port)
        mails = imapper.unseen(1)
        if mails:
            [mail] = mails
            result = {
                'subject': mail.title,
                'body': mail.body,
                'from': mail.from_addr,
                'to': mail.to,
                'date': mail.date,
                'reply_to': mail.reply_to
            }
            module.exit_json(changed=True, mail=result)
        else:
            module.exit_json(changed=False)
    except Exception as e:
        module.fail_json(msg="imap failed: {0}".format(e))
    finally:
        if imapper:
            imapper.quit()


if __name__ == '__main__':
    main()

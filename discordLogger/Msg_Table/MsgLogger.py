import pandas as pd


class MsgLogger:

    def __init__(self):
        self.msg_tb = pd.DataFrame(columns=['Time', 'Author', 'Message Content', 'Mentions'])
        self.enabled = False

    def push_msg(self, message):
        if self.enabled:
            new_entry = pd.DataFrame([message])
            self.msg_tb = pd.concat([self.msg_tb, new_entry], ignore_index=True)

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def export_to_csv(self, filename):
        self.msg_tb.to_csv(f'{filename}.csv', encoding='utf-8')

    def clear(self):
        self.msg_tb = self.msg_tb.head(0)

    def get_df(self):
        return self.msg_tb

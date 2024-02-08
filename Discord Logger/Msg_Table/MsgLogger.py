import pandas as pd


class MsgLogger:

    def __init__(self):
        self.msg_tb = pd.DataFrame(columns=['Time', 'Author', 'Message Content'])
        self.enabled = True

    def push_msg(self, message):
        if self.enabled:
            self.msg_tb = self.msg_tb.append(message, ignore_index=True)

    def disable(self):
        self.enabled = False

    def export_to_csv(self, filename):
        self.msg_tb.to_csv(f'{filename}.csv', encoding='utf-8')

    def clear(self):
        self.msg_tb = self.msg_tb.head(0)

    def get_df(self):
        return self.msg_tb

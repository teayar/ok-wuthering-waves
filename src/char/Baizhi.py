from src.char.BaseChar import BaseChar


class Baizhi(BaseChar):

    def count_base_priority(self):
        return -1

    def count_echo_priority(self):
        return 0

    def do_perform(self):
        if self.has_intro:
            self.logger.debug('has_intro wait click 1.2 sec')
            self.continues_normal_attack(1.2, click_resonance_if_ready_and_return=True)
        self.click_liberation(con_less_than=1)
        self.click_resonance()
        if not self.is_con_full():
            self.logger.debug('continues_normal_attack')
            self.continues_normal_attack(1.1 - self.time_elapsed_accounting_for_freeze(self.last_perform),
                                         until_con_full=True)
        if self.get_current_con() > 0.65:
            self.click_echo()
        self.switch_next_char()

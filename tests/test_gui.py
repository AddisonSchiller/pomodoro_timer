import pytest
import time

from ptimer.gui.gui_version import Ptimer


class TestGUIPtimer():

    def test_init_values(self):
        timer = Ptimer()
        assert timer.sequence_times == {
            'round': 1500,
            'break': 300,
            'long break': 1200
        }
        assert timer.started is False
        assert timer.round == 0
        assert timer.last_time == 0
        assert timer.time_elapsed == 0

    def test_reset(self):
        timer = Ptimer()
        timer.toggle_pause()
        time.sleep(1)
        timer.update()
        assert timer.time_elapsed != 0
        assert timer.last_time != 0

        timer.reset()
        assert timer.time_elapsed == 0
        assert timer.last_time == 0
        assert timer.started is False

    def test_pause(self):
        timer = Ptimer()
        assert timer.started is False
        timer.toggle_pause()
        assert timer.started is True
        assert timer.last_time != 0
        timer.toggle_pause()
        assert timer.started is False

    def test_format_time(self):
        timer = Ptimer()
        timer.time_elapsed = 1500
        assert timer.format_time() == '00:00'

    def test_update_round_rollover(self):
        timer = Ptimer()
        timer.toggle_pause()
        assert timer.started is True
        timer.time_elapsed = 8000
        assert timer.round == 0
        timer.update()
        assert timer.round == 1

    def test_update_sequence_rollover(self):
        timer = Ptimer()
        timer.toggle_pause()
        assert timer.started is True
        timer.time_elapsed = 8000
        timer.round = 7
        assert timer.round == 7
        timer.update()
        assert timer.round == 0

    def test_full_round(self):
        timer = Ptimer()
        timer.toggle_pause()

        for i in range(8):
            assert timer.round == i
            timer.time_elapsed = 8000
            timer.update()
        assert timer.time_label.text == "Sequence over! Good job!"
        assert timer.round == 0

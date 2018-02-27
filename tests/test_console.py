import sys
import pytest
from mock import call, Mock
from StringIO import StringIO


from ptimer.console_version import Ptimer


class TestPtimer():

    def test_time_values(self):
        timer = Ptimer(25, 5, 20, False)
        assert timer.round_time == 1500
        assert timer.break_time == 300
        assert timer.large_break_time == 1200

    def test_round(self):
        timer = Ptimer(.025, .025, .025, False)
        timer.round = Mock()
        timer.start()
        calls = []
        for i in range(4):
            message = "\r On round %i. There is" % (i + 1)
            calls.append(call(message, 1.5))
            message = "\r On break %i. There is" % (i + 1)
            calls.append(call(message, 1.5))

        timer.round.assert_has_calls(calls)

    def test_ring(self):
        timer = Ptimer(.025, .025, .025, False)
        timer.ring = Mock()
        timer.round_sleep = 0
        timer.ring_sleep = 0
        timer.start()
        assert timer.ring.call_count == 8

    def test_std_out(self):
        timer = Ptimer(.025, .025, .025, False)
        timer.ring_sleep = 0
        out = StringIO()
        sys.stdout = out
        timer.ring()
        output = out.getvalue().strip()
        assert "ring" in output

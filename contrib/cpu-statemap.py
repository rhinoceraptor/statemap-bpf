#!/usr/bin/env python
# @lint-avoid-python-3-compatibility-imports

from __future__ import print_function
from bcc import BPF

sample_freq = 100

bpf_text = """
#include <uapi/linux/ptrace.h>
#include <linux/sched.h>

BPF_PERF_OUTPUT(events);

int do_perf_event (struct bpf_perf_event_data *ctx) {
}

"""

b = BPF(text=bpf_text)
b.attach_perf_event(
        ev_type=PerfType.SOFTWARE,
        ev_config=PerfSWConfig.CPU_CLOCK,
        fn_name="do_perf_event",
        sample_freq=sample_freq,
        cpu=args.cpu)


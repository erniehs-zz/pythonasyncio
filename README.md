# Python threads and stuff

Some playing around with threads, processes and asyncio

- threading better for IO bound wheras multiprocessing for CPU bound tasks.
- async IO is a style of concurrent programming
- asynchronous routines are able to “pause” while waiting on their result

| Concurrency Type                     | Switching Decision                                                    | Number of Processors |
| ------------------------------------ | --------------------------------------------------------------------- | -------------------- |
| Pre-emptive multitasking (threading) | The operating system decides when to switch tasks external to Python. | 1                    |
| Cooperative multitasking (asyncio)   | The tasks decide when to give up control.                             | 1                    |
| Multiprocessing (multiprocessing)    | The processes all run at the same time on different processors.       | Many                 |

| I/O-Bound Process                                                                                                     | CPU-Bound Process                                                                        |
| --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Your program spends most of its time talking to a slow device, like a network connection, a hard drive, or a printer. | Your program spends most of its time doing CPU operations.                               |
| Speeding it up involves overlapping the times spent waiting for these devices.                                        | Speeding it up involves finding ways to do more computations in the same amount of time. |

multiprocessing atually creates multiple python interpreters.

## Appendix

All taken fron the following links.

https://realpython.com/python-concurrency/

https://realpython.com/python-gil/

https://realpython.com/async-io-python/

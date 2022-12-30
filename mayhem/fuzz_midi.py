#! /usr/bin/env python3
import atheris
import random
import sys

from mido import KeySignatureError

import fuzz_helpers

with atheris.instrument_imports(include=["miditoolkit"]):
    from miditoolkit.midi import parser as midi_parser

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        with fdp.ConsumeMemoryFile(all_data=True, as_bytes=True) as f:
            midi_parser.MidiFile(file=f)
    except (EOFError, IOError, KeySignatureError):
        return -1
    except IndexError:
        if random.random() > 0.99:
            raise
        return -1
    except ValueError as e:
        if 'start message' in str(e):
            return -1
        elif random.random() > 0.999:
            raise e
        else:
            return -1



def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()

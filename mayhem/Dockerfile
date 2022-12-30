# Build Stage
FROM fuzzers/atheris:2.0.7-python3.9

ADD . /src
WORKDIR /src
RUN python3 -m pip install . && python3 -m pip install  matplotlib scipy
RUN python3 -m pip uninstall -y numpy && python3 -m pip install numpy==1.23.3

CMD ["/src/mayhem/fuzz_midi.py"]
